from dataclasses import dataclass, field
from core.configurations.BaseSettings import BaseSettings
from core.FamiliarData import Familiar

from enum import Enum

class DungeonType(Enum):
    NOT_SET = 0
    DUNGEON_1 = 1
    DUNGEON_2 = 2
    DUNGEON_3 = 3

class ZoneType(Enum):
    NOT_SET = 0
    ZONE_1 = 1
    ZONE_2 = 2
    ZONE_3 = 3
    ZONE_4 = 4
    ZONE_5 = 5
    ZONE_6 = 6
    ZONE_7 = 7
    ZONE_8 = 8

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
    is_persuasion_enabled: bool = True
    familiar_names: list[str] = field(default_factory=list)
    zone: int = 0
    dungeon: int = 0
    difficulty: DungeonDifficulty = DungeonDifficulty.HEROIC
    auto_decline_familiar: bool = True

    _file_path: str = field(default=None)