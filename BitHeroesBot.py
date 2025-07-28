from core.StateMachine import StateMachine
from core.controllers.AutoQuestController import AutoQuestController
from core.controllers.AutoFishController import AutoFishController
from core.controllers.GeneralSettingsController import GeneralSettingsController
from core.controllers.AdvancedSettingsController import AdvancedSettingsController
from core.controllers.LoggerController import LoggerController
from core.controllers.InfoController import InfoController
from core.WindowHandler import WindowHandler
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration
from core.configurations.GeneralSettingsConfiguration import GeneralSettingsConfiguration
from core.configurations.AdvancedSettingsConfiguration import AdvancedSettingsConfiguration
from core.GameStats import GameStats
from core.Logger import Logger
from core.GameInterface import GameInterface
from core.ZoneData import ZoneData
from core.InputHandler import InputHandler
from core.ScreenshotTool import ScreenshotTool
from core.AutoPilotStarter import AutoPilotStarter
from core.controllers.StatsController import StatsController
from core.constants.ConfigData import AUTO_QUEST_DATA_FILE, AUTO_FISH_DATA_FILE, GENERAL_SETTINGS_DATA_FILE, ADVANCED_SETTINGS_DATA_FILE
from core.FamiliarData import FamiliarData
from core.ApplicationSetup import ApplicationSetup
from gui.BitHeroesGui import BitHeroesGui

if __name__ == '__main__':

    ApplicationSetup.load()

    bit_heroes_gui = BitHeroesGui() 

    auto_quest_configuration = AutoQuestConfiguration(AUTO_QUEST_DATA_FILE)  
    auto_fish_configuration = AutoFishConfiguration(AUTO_FISH_DATA_FILE)
    general_settings_configuration = GeneralSettingsConfiguration(GENERAL_SETTINGS_DATA_FILE)
    advanced_settings_configuration = AdvancedSettingsConfiguration(ADVANCED_SETTINGS_DATA_FILE)

    game_stats = GameStats()
    logger = Logger(advanced_settings_configuration)
    zone_data = ZoneData()
    familiar_data = FamiliarData(zone_data)

    quest_controller = AutoQuestController(auto_quest_configuration, bit_heroes_gui.get_auto_quest_tab(), familiar_data, zone_data, logger)
    fish_controller = AutoFishController(auto_fish_configuration, bit_heroes_gui.get_auto_fish_tab(), logger)
    general_settings_controller = GeneralSettingsController(general_settings_configuration, bit_heroes_gui.get_general_settings_tab(), bit_heroes_gui, logger)
    advanced_settings_controller = AdvancedSettingsController(advanced_settings_configuration, bit_heroes_gui.get_advanced_settings_tab())
    info_controller = InfoController(bit_heroes_gui.get_info_tab(), logger)
    stats_controller = StatsController(bit_heroes_gui.get_dungeon_stat(), bit_heroes_gui.get_familiar_stat(), bit_heroes_gui.get_fish_stat(), game_stats)
    logger_controller = LoggerController(logger, bit_heroes_gui.get_ctk_logger())

    window_handler = WindowHandler(bit_heroes_gui.get_game_container_frame_id())
    screenshot_tool = ScreenshotTool(window_handler, logger)
    input_handler = InputHandler(window_handler, logger)
    game_interface = GameInterface(input_handler, screenshot_tool, window_handler, logger)

    state_machine = StateMachine(game_interface, 
                                 auto_quest_configuration, 
                                 auto_fish_configuration, 
                                 general_settings_configuration, 
                                 game_stats, 
                                 window_handler, 
                                 zone_data,
                                 logger)

    game_automation_controllers = [quest_controller, fish_controller]
    setting_configuration_controllers = [general_settings_controller, advanced_settings_controller, info_controller]

    autopilot_starter = AutoPilotStarter(game_automation_controllers, 
                                         setting_configuration_controllers, 
                                         bit_heroes_gui.get_button_on_off(), 
                                         state_machine, 
                                         game_interface,
                                         logger)

    bit_heroes_gui.apply_tab_configurations()
    bit_heroes_gui.mainloop()
  


