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
        while self.automation_machine.has_available_worms():
            self.state_machine.check_if_stopped()
            current_worm: WormRarity = self.screenshot_tool.current_worm()
            worms_to_select: list[WormRarity] = self.automation_machine.get_worm_to_select()
            if current_worm == WormRarity.NONE:
                self.automation_machine.set_has_available_worm(False)
                self.logger.print("No worm is available 🪱")
                self.logger.print("Fish automation will be disabled until an auto pilot restart")
            elif current_worm not in worms_to_select:
                self.input_handler.click_worm_window()
                available_worms = self.screenshot_tool.get_available_worms()
                if available_worms == None:
                    self.logger.print("You have used every worms you have enabled into the configuration. 🪱")
                    self.logger.print("Fish automation will be disabled until an auto pilot restart")
                    self.automation_machine.set_has_available_worm(False)
                self.input_handler.select_worm(worms_to_select[0], available_worms)
            else:
                self.input_handler.click_fish_start()
                while not self.screenshot_tool.is_fish_min_range():
                    self.state_machine.check_if_stopped()
                    pass
                sleep(0.38)
                self.input_handler.click_fish_cast()
                sleep(6)
                if not self.screenshot_tool.is_trash():
                    while not self.screenshot_tool.is_fish_max_catch_rate():
                        self.state_machine.check_if_stopped()
                        pass
                    self.input_handler.click_fish_catch()
                    sleep(4)
                    self.game_stats.increment_fish_caught()
                    self.logger.print("=== FISH CATCHED 🐟 ===")
                else:
                    self.logger.print("=== TRASH FOUND 🗑️ ===")
                self.input_handler.close_fish_window()
        self.exit()

    def exit(self):
        self.input_handler.close_window()

        
