# Job: Switch between different automations considering if you have enough resources or energy, if not go in an automation state of refilling the ressources

from enum import Enum
from gui.widgets.CTkLogger import CTkLogger
from core.models.Worms import WormRarity
from core.configurations.AutoQuestConfiguration import ENERGY_DIFFICULTY
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration

class Automation(Enum):
    REFILL_ENERGY = "refill_energy"
    AUTO_QUEST = "auto_quest"
    AUTO_FISHING = "auto_fishing"

class AutomationMachine:

    def __init__(self, auto_quest_model: AutoQuestConfiguration, auto_fishing_model: AutoFishConfiguration, logger: CTkLogger):
        self.auto_quest_config = auto_quest_model
        self.auto_fishing_model = auto_fishing_model
        self.logger = logger
        self.current_automation = None
        self._quest_energy = None 
        self._worms_available = None
        self.reset_game_ressources()

    def reset_game_ressources(self):
        # Initialize game resources to default available values before actual game updates them
        self._quest_energy = 30 
        self._worms_available = True

    def update_automation(self):
        if self.has_enough_quest_energy() and self.auto_quest_config.is_enabled:
            if self.current_automation != Automation.AUTO_QUEST:
                self.logger.print("Switching to AUTO QUEST mode ⚙️")
                self.current_automation = Automation.AUTO_QUEST
        elif self.has_available_worms() and self.auto_fishing_model.is_enabled:
            if self.current_automation != Automation.AUTO_FISHING:
                self.logger.print("Switching to AUTO FISHING mode ⚙️")
                self.current_automation = Automation.AUTO_FISHING
        else:
            if self.current_automation != Automation.REFILL_ENERGY:
                self.logger.print("Switching to REFILL ENERGY mode 🪫")
                self.current_automation = Automation.REFILL_ENERGY

    def set_energy(self, energy: int):
        self._quest_energy = energy
        self.logger.print(f"Resources updated: {self._quest_energy} quest energy left")
    
    def get_energy(self) -> int:
        return self._quest_energy
    
    def get_worm_to_select(self) -> list[WormRarity]:
        worms_to_select = []
        if self.auto_fishing_model.is_common:
            worms_to_select.append(WormRarity.COMMON)
        if self.auto_fishing_model.is_rare:
            worms_to_select.append(WormRarity.RARE)
        if self.auto_fishing_model.is_epic:
            worms_to_select.append(WormRarity.EPIC)
        if self.auto_fishing_model.is_legendary:
            worms_to_select.append(WormRarity.LEGENDARY)
        return worms_to_select
    
    def set_has_available_worm(self, is_available: bool):
        self._worms_available = is_available
    
    def has_available_worms(self) -> bool:
        return self._worms_available

    def has_enough_quest_energy(self) -> bool:
        return self._quest_energy >= ENERGY_DIFFICULTY[self.auto_quest_config.difficulty] and self.auto_quest_config.is_enabled