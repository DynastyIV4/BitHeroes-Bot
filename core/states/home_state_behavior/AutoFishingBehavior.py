from core.states.BaseState import BaseState
from core.states.FishingState import FishingState

from time import sleep
class AutoFishingBehavior(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        pass
    
    def execute(self):
        self.game_interface.click_fish_menu()
        self.game_interface.click_fish_play()
        self.game_interface.wait_till_ready(self.game_interface.is_fishing_state)
        self.state_machine.change_state(FishingState(self.state_machine))
    
    def exit(self):
        pass
        