from dataclasses import dataclass, field
from core.configurations.ConfigurationBase import ConfigurationBase
from enum import Enum
from core.constants.GuiData import GAME_PATH_DEFAULT_TEXT

class AppearanceMode(Enum):
    SYSTEM = (0, "system")
    DARK = (1, "dark")
    LIGHT = (2, "light")

    def __init__(self, value: int, ctk_string_command: str):
        self.index = value
        self.ctk_string_command = ctk_string_command
 
@dataclass
class GeneralSettingsConfiguration(ConfigurationBase):

    appearance_mode: int = AppearanceMode.SYSTEM.value
    game_path: str = GAME_PATH_DEFAULT_TEXT
    is_always_on_top: bool = False

    def __init__(self, file_path):
        super().__init__(file_path)