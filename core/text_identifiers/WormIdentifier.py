import numpy as np
from PIL import Image
import pytesseract
import cv2

class WormIdentifier:
    @staticmethod
    def identify(image: Image.Image) -> int:
        # Step 1: Convert to grayscale
        gray = image.convert("L")
        gray_np = np.array(gray)
        gray.save("step1_gray.png")

        # Step 2: Threshold to get initial digit mask
        THRESHOLD = 200
        digit_mask = (gray_np < THRESHOLD).astype(np.uint8)
        thresholded = digit_mask * 255
        Image.fromarray(thresholded).save("step2_thresh_inverted.png")

        # Step 6: OCR
        extracted_text = pytesseract.image_to_string(thresholded, lang='Edit_Undo_BRK', config='-c tessedit_char_whitelist=0123456789')
        print(f"Extracted text: {extracted_text}")

        first_word = extracted_text.split()[0] if extracted_text.strip() else ""
        return int(first_word) if first_word.isdigit() else None
