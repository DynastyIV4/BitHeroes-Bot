from core.Observer import Publisher
from core.constants.ConfigData import LOG_FILE_PATH
from core.configurations.AdvancedSettingsConfiguration import AdvancedSettingsConfiguration

import os
from datetime import datetime

class Logger(Publisher):

    def __init__(self, avanced_settings_configuration: AdvancedSettingsConfiguration):
        super().__init__()
        self._last_line_printed: str = ""
        self._all_lines_printed: list[str] = []
        self._file_name = self._generate_file_name()
        self._avanced_settings_configuration = avanced_settings_configuration

    def print(self, text: str, is_debug: bool = False):
        if is_debug and not self._avanced_settings_configuration.enable_debug_logging:
            return

        self._last_line_printed = text
        self._all_lines_printed.append(text)
        if self._avanced_settings_configuration.enable_export_logging:
            self.export_logs()
        self.notify()

    def get_last_line_printed(self) -> str:
        return self._last_line_printed
    
    def _generate_file_name(self) -> str:
        ext: str = ".txt"
        base_file_name:str = f"log_{datetime.now().strftime('%Y-%m-%d')}"
        filename: str = base_file_name + ext
        counter: int = 1

        while os.path.exists(os.path.join(LOG_FILE_PATH, filename)):
            filename = f"{base_file_name}_{counter}{ext}"
            counter += 1
        return filename

    def export_logs(self):
        os.makedirs(LOG_FILE_PATH, exist_ok=True)
        file_path = os.path.join(LOG_FILE_PATH, self._file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            for line in getattr(self, 'all_lines_printed', []):
                f.write(line + "\n")
    