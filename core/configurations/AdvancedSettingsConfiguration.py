from dataclasses import dataclass, field
from core.configurations.ConfigurationBase import ConfigurationBase

@dataclass
class AdvancedSettingsConfiguration(ConfigurationBase):

    enable_debug_logging: bool = False
    enable_export_logging: bool = False

    def __init__(self, file_path):
        super().__init__(file_path)