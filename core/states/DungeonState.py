from core.states.BaseState import BaseState
from core.states.PersuasionState import PersuasionState

from time import sleep

class DungeonState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)
        
    def enter(self):
        self.execute()

    def execute(self):
        entered_dungeon = True
        while self.automation_machine.has_enough_quest_energy():
            if not entered_dungeon: 
                self.input_handler.click_rerun_dungeon()
                sleep(3)
            else:
                entered_dungeon = False
            self.logger.print("=== DUNGEON STATE ⚔️ ===")
            
            sleep(2)
            if self.screenshot_tool.is_dungeon_auto_pilot_disabled():
                self.input_handler.click_auto_pilot()

            while not self.memory_reader.is_dungeon_completed():
                self.state_machine.check_if_stopped()
                if self.memory_reader.is_in_persuasion_state():
                    self.state_machine.change_state(PersuasionState(self.state_machine))
            sleep(4)
            self.logger.print("=== DUNGEON FINISHED 🏆 ===")
            self.automation_machine.set_energy(self.memory_reader.get_energy())
            self.game_stats.increment_dungeons_completed()

        self.exit()

    def exit(self):
        self.input_handler.click_return_home()
        sleep(3)
        