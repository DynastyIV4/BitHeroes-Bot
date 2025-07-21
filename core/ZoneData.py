from dataclasses import dataclass

@dataclass
class Zone:
    index: int
    name: str
    dungeon_count: int

    def is_last_dungeon(self, dungeon_index: int) -> bool:
        return dungeon_index == self.dungeon_count

class ZoneData():

    def __init__(self):
        self._data = ZoneData.get_all_zones()

    @staticmethod
    def get_all_zones() -> list[Zone]:
        zones: list[Zone] = []
        zones.append(Zone(1, "Bit Valley", 4))
        zones.append(Zone(2, "Wintermarsh", 4))
        zones.append(Zone(3, "Lakehaven", 4))
        zones.append(Zone(4, "Ashvale", 4))
        zones.append(Zone(5, "Aramore", 4))
        zones.append(Zone(6, "Morgoroth", 4))
        zones.append(Zone(7, "Cambora", 3))
        zones.append(Zone(8, "Galaran", 3))
        zones.append(Zone(9, "Eshlyn", 3))
        zones.append(Zone(10, "Uamor", 4))
        zones.append(Zone(11, "Melvin's Genesis", 4))
        zones.append(Zone(12, "Zord Attacks!", 4))
        zones.append(Zone(13, "Ancient Odyssey", 4))
        zones.append(Zone(14, "Southpeak", 4))
        zones.append(Zone(15, "Fenrir's Omen", 4))
        zones.append(Zone(16, "Steamfunk City", 4))
        zones.append(Zone(17, "Olympian Secret Party", 4))
        zones.append(Zone(18, "Sruxon Attack!", 4))
        zones.append(Zone(19, "Galactic Trials", 4))
        zones.append(Zone(20, "Big Claw", 4))
        return zones

    def get_all_names(self) -> list[str]:
        return [zone.name for zone in self._data]

    def get_zone_by_index(self, index: int) -> Zone:
        for zone in self._data:
            if zone.index == index:
                return zone
        return None
    
    def get_zone_dungeon_count(self, index: int) -> list[str]:
        return self.get_zone_by_index(index).dungeon_count
    
    def get_zone_name(self, index: int) -> list[str]:
        return self.get_zone_by_index(index).name