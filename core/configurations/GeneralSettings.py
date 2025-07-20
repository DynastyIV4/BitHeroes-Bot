from dataclasses import dataclass, field
from core.configurations.BaseSettings import BaseSettings
from enum import Enum
from core.constants.GuiData import GAME_PATH_DEFAULT_TEXT

class AppearanceMode(Enum):
    SYSTEM = 0
    DARK = 1
    LIGHT = 2

@dataclass
class GeneralSettingsConfiguration(BaseSettings):

    appearance_mode: int = AppearanceMode.SYSTEM.value
    game_path: str = GAME_PATH_DEFAULT_TEXT
    is_always_on_top: bool = False

    _file_path: str = field(default=None)
