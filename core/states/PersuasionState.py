from core.states.BaseState import BaseState
from core.text_identifiers.FamiliarIdentifier import FamiliarIdentifier

from time import sleep
class PersuasionState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        self.logger.print("=== PERSUASION STATE 🐒 ===")
        self.execute()

    def execute(self):
        if self.auto_quest_config.is_persuasion_enabled:
            sleep(1)
            text_screenshot = self.game_interface.take_persuasion_screenshot()
            is_found, name = FamiliarIdentifier.identify(text_screenshot, self.auto_quest_config.familiar_names)
            self.logger.print(f"Familiar found: {name}")
            if is_found:
                self.game_interface.click_accept_familiar()
                self.game_interface.click_confirm_familiar()
                sleep(3)
                if self.game_interface.persuasion_has_succeeded():
                    self.logger.print("Persuasion succeeded! 🎉")
                    self.game_stats.increment_familiar_encountered()
                    self.game_interface.close_window()
                else:
                    self.logger.print("Persuasion failed ❌")
            elif (self.auto_quest_config.auto_decline_familiar):
                self.logger.print("Auto-declining...")
                self.game_interface.click_decline_familiar()
                self.game_interface.click_confirm_familiar()
            else:
                self.logger.print("Auto-decline is disabled. Waiting for user action...")
                self.game_interface.wait_till_ready(self.game_interface.is_not_in_persuasion_state)
        elif self.auto_quest_config.auto_decline_familiar:
            self.logger.print("Auto-declining...")
            self.game_interface.click_decline_familiar()
            self.game_interface.click_confirm_familiar()
        else:
            self.logger.print("Auto-persuade feature is disabled, waiting for user, in-game auto-persuade or auto-decline to take action")
            self.game_interface.wait_till_ready(self.game_interface.is_not_in_persuasion_state)
        self.exit()

    def exit(self):
        self.logger.print("Persuasion Completed! ✅")
