from dataclasses import dataclass, field
from core.configurations.BaseSettings import BaseSettings

@dataclass
class AutoFishConfiguration(BaseSettings):

    is_enabled: bool = True
    is_rare: bool = True
    is_legendary: bool = True
    is_epic: bool = True
    is_common: bool = True

    _file_path: str = field(default=None)
