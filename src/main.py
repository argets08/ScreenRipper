from capture import ScreenCapturer
from ocr import OCRProcessor
from pynput import keyboard
import Quartz
from datetime import datetime

# capturer = ScreenCapturer('Your Meeting/Online Course Window Title')capturer = ScreenCapturer()
# capturer = ScreenCapturer()
capturer = ScreenCapturer()
processor = OCRProcessor()

current_keys = set()

def get_chrome_window_bounds():
    window_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window in window_list:
        if window['kCGWindowOwnerName'] == 'Google Chrome' and 'kCGWindowName' in window:
            return window['kCGWindowBounds']
    return None


def on_key_press(key):
    if key == keyboard.Key.cmd or key == keyboard.Key.shift or key == keyboard.KeyCode.from_char('x'):
        current_keys.add(key)
        check_for_combination()

def on_key_release(key):
    if key in current_keys:
        current_keys.remove(key)

def check_for_combination():
    if keyboard.Key.cmd in current_keys and keyboard.Key.shift in current_keys and keyboard.KeyCode.from_char('x') in current_keys:
        capture_and_save()

def capture_and_save():
    # screenshot = capturer.capture()
    # screenshot = capturer.capture_fullscreen()
    screenshot = capturer.capture_chrome_content()
    if screenshot:
        extracted_text = processor.extract_text(screenshot)
        # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # with open('../notes/notes.txt', 'a') as file:
        #     file.write(f"Timestamp: {timestamp}\n")
        #     file.write(f"{extracted_text}\n\n")
         # Create a timestamp for naming the file and logging within the file
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = f"../notes/{timestamp}.txt"  # This will create a new file each time

        with open(filename, 'w') as file:
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"{extracted_text}\n\n")

if __name__ == '__main__':
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()


