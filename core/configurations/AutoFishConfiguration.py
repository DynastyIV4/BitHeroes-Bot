from dataclasses import dataclass, field
from core.configurations.ConfigurationBase import ConfigurationBase

@dataclass
class AutoFishConfiguration(ConfigurationBase):

    is_enabled: bool = True
    is_rare: bool = False
    is_legendary: bool = False
    is_epic: bool = False
    is_common: bool = False

    def __init__(self, file_path):
        super().__init__(file_path)
        