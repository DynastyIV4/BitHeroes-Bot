from core.states.BaseState import BaseState
from core.states.GameLaunchingState import GameLaunchingState
from core.states.HomeState import HomeState
from core.AutomationMachine import AutomationMachine
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration
from core.configurations.GeneralSettingsConfiguration import GeneralSettingsConfiguration
from core.WindowHandler import WindowHandler
from core.GameInterface import GameInterface
from core.Errors import CustomException, AutoPilotStoppedByButtonError
from core.Observer import Subscriber
from core.ZoneData import ZoneData
from core.GameStats import GameStats
from core.Logger import Logger

class StateMachine(Subscriber):
    
    def __init__(self, 
                 game_interface: GameInterface,
                 auto_quest_config: AutoQuestConfiguration,
                 auto_fish_config: AutoFishConfiguration,
                 general_settings_config: GeneralSettingsConfiguration,
                 game_stats: GameStats,
                 window_handler: WindowHandler,
                 zone_data: ZoneData,
                 logger: Logger):
        super().__init__()
        self.game_interface = game_interface
        self.auto_quest_config = auto_quest_config
        self.auto_fish_config = auto_fish_config
        self.general_settings_config = general_settings_config
        self.game_stats = game_stats
        self.window_handler = window_handler
        self.zone_data = zone_data
        self.logger = logger
        self.automation_machine = AutomationMachine(auto_quest_config, auto_fish_config, logger)
        self._current_state = None
        self.is_stop_checking_enabled = False
        self.is_stopped = False
        self.game_interface.subscribe(self)
    
    def start(self, initial_state: BaseState):
        self._current_state = initial_state
        self._current_state.enter()

    def change_state(self, new_state: BaseState):
        self.check_if_stopped()
        self._current_state = new_state
        self._current_state.enter()

    def run(self):
        try:
            while True:
                if not self.game_interface.is_game_running() or self.game_interface.is_disconnected():
                    self.change_state(GameLaunchingState(self))
                else:
                    self.change_state(HomeState(self))
        except CustomException as e:
            self.logger.print(str(e))
        
        self.is_stopped = True

    def stop(self):
        self.is_stopped = True
    
    def check_if_stopped(self):
        if self.is_stopped and self.is_stop_checking_enabled:
            raise AutoPilotStoppedByButtonError()
    
    def update(self):
        self.check_if_stopped()