import re

class TextFilter:
    @staticmethod
    def extract_questions(text):
        return re.findall(r'(?<=\? )\w+', text)
