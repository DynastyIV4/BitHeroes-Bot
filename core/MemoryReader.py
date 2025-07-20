from core.models.PointerAddress import PointerAddress
from core.Errors import GameNotLaunchedError
from core.constants.ConfigData import BIT_HEROES_PROCESS_NAME
from core.constants.MemoryPointersData import MEMORY_POINTERS

from pymem.exception import MemoryReadError
from pymem import Pymem 

class MemoryReader:
    
    def __init__(self):
        self.process = None
        self.base_address = None

    def start(self):
        try:
            self.process = Pymem(BIT_HEROES_PROCESS_NAME)
        except Exception as e:
            raise Exception(f"Failed to attach to process '{BIT_HEROES_PROCESS_NAME}'. Please ensure the game is running.") from e
        self.base_address = self.process.process_base.lpBaseOfDll

    def get_module_base_address(self, module_name: str):
        try:
            for module in self.process.list_modules():
                if module.name == module_name:
                    return module.lpBaseOfDll
            raise GameNotLaunchedError() 
        except Exception as e:
            raise GameNotLaunchedError() from e

    def get_pointer_address(self, pointer: PointerAddress):
        module_address = self.get_module_base_address(pointer.module)
        address = self.process.read_longlong(module_address + pointer.base)
        for offset in pointer.offsets:
            if offset == pointer.offsets[-1]:
                return address + offset
            else:
                address = self.process.read_longlong(address + offset)
    
    def read_memory(self, pointer: PointerAddress):
        if self.process is None:
            raise GameNotLaunchedError("MemoryReader has not been started. Call start() method first.")
        
        address = self.get_pointer_address(pointer)
        return self.process.read_longlong(address) & 0xFFFFFFFF

    def write_memory(self, pointer: PointerAddress, value: int):
        address = self.get_pointer_address(pointer)
        return self.process.write_longlong(address, value) 

    # 📌 Getters
    def get_gems(self) -> int:
        return self.read_memory(MEMORY_POINTERS["gems"])

    def get_energy(self) -> int:
        return self.read_memory(MEMORY_POINTERS["energy"])

    def get_money(self) -> int:
        return self.read_memory(MEMORY_POINTERS["money"])
    
    def get_zone(self) -> int:
        return self.read_memory(MEMORY_POINTERS["zone"])
    
    def is_auto_pilot_enabled(self) -> bool:
        value = self.read_memory(MEMORY_POINTERS["is_auto_pilot_enabled"])
        return value == 1
    
    def get_window_level(self) -> int:
        """
        IN DUNGEON:
        1: Idle
        2: In combat
        3: Combat finished or Familiar bribed

        IN MENU:
        0: Idle or Chat opened
        1: A window is opened
        2: ?
        3: ?
        4: ?
        5: Shop
        """
        return self.read_memory(MEMORY_POINTERS["window_level"])
    
    """
    IN DUNGEON:
    """
    def is_in_combat(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_in_combat"]) in [0, 8]
    
    def is_combat_finished(self) -> bool:
        return self.get_window_level() != 3
    
    def is_idle(self) -> bool:
        return self.get_window_level() == 1
    
    def is_in_dungeon_state(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_in_dungeon_state"]) == 1
    
    def is_in_persuasion_state(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_in_persuasion_state"]) == 3
    
    def is_dungeon_completed(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_dungeon_completed"]) != 0
    
    def is_in_menu_state(self) -> bool:
        return self.is_in_dungeon_state() == False
    
    def is_settings_opened(self) -> bool:
        try:
            self.is_auto_pilot_enabled()
            return True
        except MemoryReadError:
            return False
    
    def is_game_running(self) -> bool:
        try:
            self.get_energy()
            return True
        except (MemoryReadError, GameNotLaunchedError):
            return False
    
    def is_max_fish_range(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_max_fish_range"]) < 1030000000
    
    def is_fishing_state(self) -> bool:
        return self.read_memory(MEMORY_POINTERS["is_fishing_state"]) & 0x0000FFFF != 0
    
    # 📌 Setters
    def set_auto_pilot(self):
        self.write_memory(MEMORY_POINTERS["auto_pilot"], 1)

    def set_zone(self, zone: int):
        if zone < 1 or zone > 20:
            raise ValueError("Zone must be between 1 and 20.")
        self.write_memory(MEMORY_POINTERS["zone"], zone)
    