from core.states.BaseState import BaseState
from core.configurations.AutoQuestConfiguration import ENERGY_DIFFICULTY, ENERGY_COOLDOWN
from core.Errors import NoAutomationAvailableToRefill

import time

class RefillEnergyBehavior(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        pass

    def execute(self):
        if self.auto_quest_config.is_enabled:
            self.logger.print("Waiting for energy to refill...")
            energy = self.automation_machine.get_energy()
            for remaining in range(ENERGY_COOLDOWN*(ENERGY_DIFFICULTY[self.auto_quest_config.difficulty] - energy), 0, -1):
                self.state_machine.check_if_stopped()
                minutes, seconds = divmod(remaining, 60)
                self.logger.print_override(f"\rTime left: {minutes:02}:{seconds:02} minutes")
                time.sleep(1)
        else:
            self.logger.print("Auto questing is not enabled and you don't have enough worms")
            raise NoAutomationAvailableToRefill()
            
    def exit(self):
        self.logger.print("Energy refilled!")
        
        
        
