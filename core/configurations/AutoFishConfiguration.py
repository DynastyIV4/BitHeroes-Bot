from dataclasses import dataclass, field
from core.configurations.BaseSettings import BaseSettings

@dataclass
class AutoFishConfiguration(BaseSettings):

    is_enabled: bool = False
    is_rare: bool = False
    is_legendary: bool = False
    is_epic: bool = False
    is_common: bool = False

    _file_path: str = field(default=None)
