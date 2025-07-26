# Job: Switch between different automations considering if you have enough resources or energy, if not go in an automation state of refilling the ressources

from core.Logger import Logger
from core.models.Worms import WormRarity
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration

from enum import Enum

class Automation(Enum):
    REFILL_ENERGY = "refill_energy"
    AUTO_QUEST = "auto_quest"
    AUTO_FISHING = "auto_fishing"

class AutomationMachine:

    @property
    def is_quest_energy_available(self) -> bool:
        return self._is_quest_energy_available
    
    @is_quest_energy_available.setter
    def is_quest_energy_available(self, value: bool):
        self._is_quest_energy_available = value
        if not value:
            self.logger.print("You have used every quest energy available. Look for a refill. ⚡️")

    @property
    def is_any_worm_available(self) -> bool:
        return self._is_any_worm_available

    @is_any_worm_available.setter
    def is_any_worm_available(self, value: bool):
        self._is_any_worm_available = value
        if not value:
            self.logger.print("You have used every worms you have enabled into the configuration. 🪱")

    def __init__(self, auto_quest_model: AutoQuestConfiguration, auto_fishing_model: AutoFishConfiguration, logger: Logger):
        self.auto_quest_config = auto_quest_model
        self.auto_fishing_model = auto_fishing_model
        self.logger = logger
        self.current_automation = None
        self._is_quest_energy_available = True
        self._is_any_worm_available = True

    def update_automation(self):
        if self.is_quest_energy_available and self.auto_quest_config.is_enabled:
            if self.current_automation != Automation.AUTO_QUEST:
                self.logger.print("Switching to AUTO QUEST mode ⚙️")
                self.current_automation = Automation.AUTO_QUEST
        elif self.is_any_worm_available and self.auto_fishing_model.is_enabled:
            if self.current_automation != Automation.AUTO_FISHING:
                self.logger.print("Switching to AUTO FISHING mode ⚙️")
                self.current_automation = Automation.AUTO_FISHING
        else:
            if self.current_automation != Automation.REFILL_ENERGY:
                self.logger.print("Switching to REFILL ENERGY mode 🪫")
                self.current_automation = Automation.REFILL_ENERGY
    
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
    
    def reset_ressources(self):
        self._is_quest_energy_available = True 
        self._is_any_worm_available = True