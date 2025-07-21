from core.states.BaseState import BaseState
from core.states.DungeonState import DungeonState

class AutoQuestBehavior(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        pass

    def execute(self):
        self.automation_machine.set_energy(self.memory_reader.get_energy())
        if self.automation_machine.has_enough_quest_energy(): 
            self.memory_reader.set_zone(self.auto_quest_config.zone)
            self.input_handler.click_quest()
            self.input_handler.click_dungeon(self.auto_quest_config.zone, self.auto_quest_config.dungeon)
            if not self.zone_data.get_zone_by_index(self.auto_quest_config.zone).is_last_dungeon(self.auto_quest_config.dungeon):
                self.input_handler.click_difficulty(self.auto_quest_config.difficulty.value)
            else:
                self.input_handler.click_run_last_dungeon()
            self.input_handler.click_accept_team()
            self.state_machine.change_state(DungeonState(self.state_machine))
    
    def exit(self):
        pass
            