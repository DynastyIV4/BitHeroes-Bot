from core.states.BaseState import BaseState
from core.states.home_state_behavior.AutoQuestBehavior import AutoQuestBehavior
from core.states.home_state_behavior.AutoFishingBehavior import AutoFishingBehavior
from core.states.home_state_behavior.RefillEnergyBehavior import RefillEnergyBehavior
from core.AutomationMachine import Automation

class HomeState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.behaviors: dict[Automation, BaseState] = {
            Automation.AUTO_QUEST: AutoQuestBehavior(state_machine),
            Automation.AUTO_FISHING: AutoFishingBehavior(state_machine),
            Automation.REFILL_ENERGY: RefillEnergyBehavior(state_machine),
        }
        
    def enter(self):
        self.logger.print("=== HOME STATE 🏠 ===")
        self.input_handler.close_menu_windows()
        self.automation_machine.update_automation()
        self.behaviors.get(self.automation_machine.current_automation).enter()
        self.execute()

    def execute(self):
        self.behaviors.get(self.automation_machine.current_automation).execute()
        self.exit()

    def exit(self):
        self.logger.print("All home tasks done ✅")
        self.behaviors.get(self.automation_machine.current_automation).exit()
