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
            text_screenshot = self.screenshot_tool.take_persuasion_screenshot()
            is_found, name = FamiliarIdentifier.identify(text_screenshot, self.auto_quest_config.familiar_names)
            self.logger.print(f"Familiar found: {name}")
            if is_found and self.auto_quest_config.is_persuasion_enabled:
                self.input_handler.click_accept_familiar()
                self.input_handler.click_confirm_familiar()
                sleep(3)
                if self.screenshot_tool.persuasion_has_succeeded():
                    self.logger.print("Persuasion succeeded! 🎉")
                    self.game_stats.increment_familiar_encountered()
                    self.input_handler.close_window()
                else:
                    self.logger.print("Persuasion failed ❌")
            elif (self.auto_quest_config.auto_decline_familiar):
                self.logger.print("Auto-declining...")
                self.input_handler.click_decline_familiar()
                self.input_handler.click_confirm_familiar()
        elif self.auto_quest_config.auto_decline_familiar:
            self.logger.print("Auto-declining...")
            self.input_handler.click_decline_familiar()
            self.input_handler.click_confirm_familiar()

        while self.memory_reader.is_in_persuasion_state():
            self.state_machine.check_if_stopped()
            pass
        self.exit()

    def exit(self):
        self.logger.print("Persuasion Completed! ✅")
