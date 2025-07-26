from core.states.BaseState import BaseState
from core.models.Worms import WormRarity

from time import sleep

class FishingState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        self.logger.print("=== FISHING STATE 🎣 ===")
        self.execute()

    def execute(self):
        while self.automation_machine.is_any_worm_available:
            current_worm: WormRarity = self.game_interface.current_worm()
            worms_to_select: list[WormRarity] = self.automation_machine.get_worm_to_select()
            if current_worm == WormRarity.NONE:
                self.automation_machine.is_any_worm_available = False
            elif current_worm not in worms_to_select:
                self.game_interface.click_worm_window()
                available_worms = self.game_interface.get_available_worms()
                first_matching_worm = next((worm for worm in worms_to_select if worm in available_worms), None)
                if first_matching_worm is None:
                    self.automation_machine.is_any_worm_available = False
                    break
                self.game_interface.select_worm(first_matching_worm, available_worms)
            else:
                self.game_interface.click_fish_start()
                self.game_interface.wait_till_ready(self.game_interface.is_fish_min_range, screenshot_cooldown=0.1)
                sleep(0.37) # Exact time needed to reach 40
                self.game_interface.click_fish_cast()
                sleep(6)
                if not self.game_interface.is_trash():
                    sleep(0.5) # To not start catching the fish if it begins in green area
                    self.game_interface.wait_till_ready(self.game_interface.is_fish_max_catch_rate, screenshot_cooldown=0)
                    self.game_interface.click_fish_catch()
                    sleep(4)
                    self.game_stats.increment_fish_caught()
                    self.logger.print("=== FISH CATCHED 🐟 ===")
                else:
                    self.logger.print("=== TRASH FOUND 🗑️ ===")
                self.game_interface.close_fish_window()
        self.exit()

    def exit(self):
        self.game_interface.close_window()

        
