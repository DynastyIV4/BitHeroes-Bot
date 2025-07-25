from core.states.BaseState import BaseState
from core.Errors import GameLaunchedFailError
from core.Process import start_game, kill_game_process

import time

class GameLaunchingState(BaseState):

    def __init__(self, state_machine):
        super().__init__(state_machine)

    def enter(self):
        self.logger.print("=== GAMING LAUNCHING STATE 🚀 ===")
        kill_game_process()
        self.logger.print("Game killed")
        self.execute()
        
    def execute(self):
        self.logger.print("Waiting for the game to launch...")
        start_game(self.general_settings_config.game_path)
        self.logger.print("Game launched")
        self.window_handler.attach_bit_heroes_window()
        self.logger.print("Bit Heroes window attached")
        for attempt in range(3):
            if self.game_interface.wait_till_ready(self.game_interface.is_game_ready, raise_error=False):
                break
            else:
                self.logger.print("Timeout: Game failed to launch within 60 seconds.")
                self.logger.print(f"Attempting to launch the game again (attempt {attempt + 2}/3)...")
                kill_game_process()
                start_game(self.general_settings_config.game_path)
            raise GameLaunchedFailError()
        self.exit()

    def exit(self):
        self.logger.print("Game is ready to go ! ✅")
        
