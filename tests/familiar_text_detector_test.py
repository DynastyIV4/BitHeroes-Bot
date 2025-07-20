from core.constants.ConfigData import TESSERACT_PATH
from core.text_identifiers.FamiliarIdentifier import FamiliarIdentifier

import pytest 
import pytesseract
from PIL import Image

def _test_identify_familiar(image_path: str, familiar_name: str) -> tuple[bool, str]:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    
    image = Image.open(f"tests/test_images/{image_path}")
    return FamiliarIdentifier.identify(image, [familiar_name])

def test_familiar_recognizer_recognize_gobby():
    result, name = _test_identify_familiar("familiar_gobby.png", "gobby")  # type: ignore
    assert result is True, "Familiar recognizer failed to recognize the familiar in the screenshot."
    assert name == "gobby", f"Familiar recognizer returned an incorrect familiar name. Name found: {name}"

def test_familiar_recognizer_recognize_moghur():
    result, name = _test_identify_familiar("familiar_moghur.png", "moghur")  # type: ignore
    assert result is True, "Familiar recognizer failed to recognize the familiar in the screenshot."
    assert name == "moghur", f"Familiar recognizer returned an incorrect familiar name. Name found: {name}"

def test_familiar_recognizer_recognize_merlan():
    result, name = _test_identify_familiar("familiar_merlan.png", "mer'lan")  # type: ignore
    assert result is True, "Familiar recognizer failed to recognize the familiar in the screenshot."
    assert name == "mer lan", f"Familiar recognizer returned an incorrect familiar name. Name found: {name}"

def test_familiar_recognizer_recognize_lord_cerulean():
    result, name = _test_identify_familiar("familiar_lord_cerulean.png", "lord cerulean")  # type: ignore
    assert result is True, "Familiar recognizer failed to recognize the familiar in the screenshot."
    assert name == "lord cerulean", f"Familiar recognizer returned an incorrect familiar name. Name found: {name}"

def test_familiar_recognizer_recognize_moghur_not_input():
    result, name = _test_identify_familiar("familiar_moghur.png", "gobby")  # type: ignore
    assert result is False, "Familiar recognizer failed to recognize the familiar in the screenshot."
    assert name == "moghur", f"Familiar recognizer returned an incorrect familiar name. Name found: {name}"