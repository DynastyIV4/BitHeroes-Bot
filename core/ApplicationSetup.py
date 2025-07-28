from core.constants.ConfigData import EDIT_UNDO_FONT_PATH, PIXEL_DIGIVOLVE_FONT_PATH, TESSERACT_PATH, APPDATA_FOLDER
from core.ExecutableUtilities import ExecutableUtilities

from customtkinter import deactivate_automatic_dpi_awareness, set_appearance_mode
from pytesseract import pytesseract

class ApplicationSetup:

    @staticmethod
    def load():
        deactivate_automatic_dpi_awareness()
        set_appearance_mode("dark") # Until Appearance Mode gets fixed
        ExecutableUtilities.load_font(EDIT_UNDO_FONT_PATH)
        ExecutableUtilities.load_font(PIXEL_DIGIVOLVE_FONT_PATH)
        ExecutableUtilities.setup_appdata_folder(APPDATA_FOLDER)
        pytesseract.tesseract_cmd = TESSERACT_PATH