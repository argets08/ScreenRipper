# import pygetwindow as gw
# from PIL import ImageGrab

# class ScreenCapturer:
#     def __init__(self, window_title):
#         self.window_title = window_title

#     def capture(self):
#         screen = gw.get_windows_with_title(self.window_title)[0]
#         if screen is not None:
#             screen._hWnd = screen._hWnd  # PyGetWindow fix
#             screenshot = ImageGrab.grab(bbox=(screen.left, screen.top, screen.right, screen.bottom))
#             return screenshot
#         return None
# from PIL import ImageGrab

# class ScreenCapturer:
#     def capture_fullscreen(self):
#         screenshot = ImageGrab.grab()
#         return screenshot
import Quartz
from PIL import ImageGrab

def get_chrome_window_bounds():
    window_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window in window_list:
        if window['kCGWindowOwnerName'] == 'Google Chrome' and 'kCGWindowName' in window:
            return window['kCGWindowBounds']
    return None

class ScreenCapturer:

    def capture_fullscreen(self):
        screenshot = ImageGrab.grab()
        return screenshot

    def capture_chrome_content(self):
        bounds = get_chrome_window_bounds()
        if not bounds:
            return None

        # Adjust dimensions
        top_adjustment = 100  # Adjust as needed
        left = bounds['X']
        top = bounds['Y'] + top_adjustment
        right = left + bounds['Width']
        bottom = top + bounds['Height'] - top_adjustment

        # Capture the content
        # screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        screenshot = ImageGrab.grab(bbox=(int(left), int(top), int(right), int(bottom)))

        return screenshot
