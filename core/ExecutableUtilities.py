import ctypes
import os
import sys

class ExecutableUtilities:
    # This class is important for packaging your application as a .exe file.
    # It provides methods to load fonts and resources correctly, especially when using PyInstaller.
    # The methods ensures that files are found whether running as a script or as a packaged executable.

    @staticmethod
    def load_font(font_path: str):
        FR_PRIVATE = 0x10
        if os.name == "nt":  # Windows
            ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
        else:
            raise NotImplementedError("This operating system is not supported. Please use a Windows OS")
    
    @staticmethod
    def resource_path(relative_path: str):
        # Get path to file whether it's running as .py or .exe
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    @staticmethod
    def setup_appdata_folder(folder_name: str):
        appdata_path = os.getenv('APPDATA')
        bit_heroes_bot_folder = os.path.join(appdata_path, folder_name)

        if not os.path.exists(bit_heroes_bot_folder):
            os.makedirs(bit_heroes_bot_folder)
