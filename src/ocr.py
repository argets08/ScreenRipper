import pytesseract
from PIL import Image

class OCRProcessor:
    def extract_text(self, image):
        return pytesseract.image_to_string(image)
