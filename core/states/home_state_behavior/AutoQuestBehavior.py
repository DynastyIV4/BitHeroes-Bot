from core.states.BaseState import BaseState
from core.states.DungeonState import DungeonState

class AutoQuestBehavior(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        pass

    def execute(self):
        self.game_interface.click_quest()
        self._set_zone()
        self.game_interface.click_dungeon(self.auto_quest_config.zone, self.auto_quest_config.dungeon)

        if not self.zone_data.get_zone_by_index(self.auto_quest_config.zone).is_last_dungeon(self.auto_quest_config.dungeon):
            self.game_interface.click_difficulty(self.auto_quest_config.difficulty.value)
        else:
            self.game_interface.click_run_last_dungeon()
        self.game_interface.click_accept_team()

        if ( self.game_interface.is_refill_energy_window_open() ):
            self.automation_machine.is_quest_energy_available = False
        else:
            self.state_machine.change_state(DungeonState(self.state_machine))
    
    def exit(self):
        pass
    
    def _set_zone(self):
        self.game_interface.click_zone_button()
        while not self.game_interface.is_zone_scrolldown_up():
            self.game_interface.click_zone_up_arrow()
            
        if self.auto_quest_config.zone <= 5:
            self.game_interface.click_zone_box(self.auto_quest_config.zone)
        else:
            self.game_interface.click_zone_down_arrow(self.auto_quest_config.zone - 5)
            self.game_interface.click_zone_box(5)
        
        if self.game_interface.is_zone_window_open():
            self.game_interface.close_window()