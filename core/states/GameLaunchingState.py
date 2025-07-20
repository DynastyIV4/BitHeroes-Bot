from core.states.BaseState import BaseState
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
        self.memory_reader.start()
        start_time = time.time()
        while not self.memory_reader.is_game_running():
            if time.time() - start_time > 60:
                self.logger.print("Timeout: Game failed to launch within 60 seconds.")
                if self.attempts == 3:
                    raise Exception("Game failed to launch after 3 attempts.")
                self.attempts += 1
                self.logger.print("Killing game...")
                kill_game_process()
                self.change_state(self.state_machine.game_launching_state)
        self.attempts = 0
        time.sleep(5)
        self.exit()

    def exit(self):
        self.logger.print("Game is ready to go ! ✅")
        
