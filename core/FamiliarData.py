from core.constants.ConfigData import FAMILIAR_DATA_PATH
from core.ZoneData import ZoneData, Zone

from enum import Enum
import json

class FamiliarRarity(Enum):
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

class Familiar:

    def __init__(self, name: str, rarity: FamiliarRarity):
        self.name = name
        self.rarity = rarity

class FamiliarData:

    def __init__(self, zone_data: ZoneData):
        self._data = None
        self._load_data()
        self._zone_data = zone_data

    def _load_data(self):
        with open(FAMILIAR_DATA_PATH, "r") as file:
            self._data = json.load(file)

    def get_data(self):
        return self._data
    
    def familiars_in_dungeon(self, zone: int, dungeon: int) -> list[Familiar]:
        GOBBY = Familiar("Gobby", FamiliarRarity.LEGENDARY)
        matching_familiars = []
        zone_found: Zone = self._zone_data.get_zone_by_index(zone)
        if zone_found:
            is_last_dungeon = zone_found.is_last_dungeon(dungeon)
            dungeon_available = [dungeon]
            if is_last_dungeon:
                dungeon_available = [i for i in range(1, zone_found.dungeon_count)]
                
            for familiar, quest_raid_rarity in self._data.items():
                zones = quest_raid_rarity.get("quest").get("zone")
                dungeons = quest_raid_rarity.get("quest").get("dungeon")
                rarity = quest_raid_rarity.get("rarity")

                for i in range (len(zones)):
                    if int(zones[i]) == zone and int(dungeons[i]) in dungeon_available:
                        matching_familiars.append(Familiar(familiar, FamiliarRarity(rarity)))
        
        # TEMPORY FIX: Every dungeon and every zone has Gobby, should be fixed in familiars.json
        matching_familiars.append(GOBBY)
        return matching_familiars
    
    def get_familiars_by_name(self, names: list[str]) -> list[Familiar]:
        familiars: list[Familiar] = []
        for name in names:
            familiars.append(self.get_familiar_by_name(name))
        return familiars

    def get_familiar_by_name(self, name: str) -> Familiar:
        if name in self._data:
            rarity = self._data[name].get("rarity")
            return Familiar(name, FamiliarRarity(rarity))
        return None