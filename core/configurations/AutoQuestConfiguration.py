from dataclasses import dataclass, field
from core.configurations.BaseSettings import BaseSettings

from enum import Enum

class DungeonDifficulty(Enum):
    NORMAL = "NORMAL"
    HARD = "HARD"
    HEROIC = "HEROIC"

ENERGY_DIFFICULTY = {
    DungeonDifficulty.NORMAL: 10,
    DungeonDifficulty.HARD: 20,
    DungeonDifficulty.HEROIC: 30
}

ENERGY_COOLDOWN = 240 # in seconds

@dataclass
class AutoQuestConfiguration(BaseSettings):

    is_enabled: bool = True
    zone: int = 0
    dungeon: int = 0
    difficulty: DungeonDifficulty = DungeonDifficulty.HEROIC
    is_persuasion_enabled: bool = False
    auto_decline_familiar: bool = False
    familiar_names: list[str] = field(default_factory=list)

    _file_path: str = field(default=None)