from core.Errors import FamiliarNameDetectionFailed
from core.text_identifiers.BaseIdentifier import BaseIdentifier

from PIL import Image, ImageOps
import pytesseract
import re

class FamiliarIdentifier(BaseIdentifier):
    
    @staticmethod
    def identify(image: Image.Image, familiar_name: list[str]) -> tuple[bool, str]:
        # Persuasion messages start with the familiar name, followed by "SEEMS TO THINK YOU'RE PRETTY COOL !"
        SECOND_WORD = "SEEMS"
        gray = ImageOps.grayscale(image)
        extracted_text = pytesseract.image_to_string(gray)
        if SECOND_WORD in extracted_text:
            first_word = extracted_text.split(SECOND_WORD)[0].strip()
        else:
             raise FamiliarNameDetectionFailed()

        match = False
        for name in familiar_name:
            # Tesseract often misinterprets apostrophes as spaces or one word, so we replace them for comparison
            # Remove spaces and punctuation for comparison
            normalized_first_word = re.sub(r'[\s\W_]+', '', first_word).lower()
            normalized_name = re.sub(r'[\s\W_]+', '', name).lower()
            if normalized_first_word == normalized_name:
                match = True
                break

        return match, first_word.lower()