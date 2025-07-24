from core.states.BaseState import BaseState
from core.states.PersuasionState import PersuasionState

from time import sleep

class DungeonState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)
        
    def enter(self):
        self.execute()

    def execute(self):
        entered_dungeon: bool = True
        while self.automation_machine.is_quest_energy_available:
            if not entered_dungeon: 
                self.game_interface.click_rerun_dungeon()
                sleep(2)
                if self.game_interface.is_refill_energy_window_open():
                    self.automation_machine.is_quest_energy_available = False
                    break
            else:
                entered_dungeon = False
            self.logger.print("=== DUNGEON STATE ⚔️ ===")
            
            sleep(2)
            if self.game_interface.is_dungeon_auto_pilot_disabled():
                self.game_interface.click_auto_pilot()

            while not self.game_interface.is_dungeon_completed():
                if self.game_interface.is_in_persuasion_state():
                    self.state_machine.change_state(PersuasionState(self.state_machine))
                sleep(0.5)

            sleep(4)
            self.logger.print("=== DUNGEON FINISHED 🏆 ===")
            self.game_stats.increment_dungeons_completed()

        self.exit()

    def exit(self):
        self.game_interface.click_return_home()
        sleep(3)        