from core.StateMachine import StateMachine
from core.MemoryReader import MemoryReader
from core.controllers.AutoQuestController import AutoQuestController
from core.controllers.AutoFishController import AutoFishController
from core.controllers.GeneralSettingsController import GeneralSettingsController
from core.controllers.InfoController import InfoController
from core.WindowHandler import WindowHandler
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration
from core.configurations.GeneralSettings import GeneralSettingsConfiguration
from core.GameStats import GameStats
from core.InputHandler import InputHandler
from core.ScreenshotTool import ScreenshotTool
from core.AutoPilotStarter import AutoPilotStarter
from core.controllers.StatsController import StatsController
from core.constants.ConfigData import AUTO_QUEST_DATA_FILE, AUTO_FISH_DATA_FILE, GENERAL_SETTINGS_DATA_FILE
from core.FamiliarData import FamiliarData
from core.ApplicationSetup import ApplicationSetup
from gui.BotHeroesGui import BotHeroesGui

if __name__ == '__main__':

    ApplicationSetup.load()

    bot_heroes_gui = BotHeroesGui() 
    logger = bot_heroes_gui.get_ctk_logger()

    auto_quest_model = AutoQuestConfiguration(_file_path=AUTO_QUEST_DATA_FILE)  
    auto_fish_model = AutoFishConfiguration(_file_path=AUTO_FISH_DATA_FILE)
    general_settings_model = GeneralSettingsConfiguration(_file_path=GENERAL_SETTINGS_DATA_FILE)

    memory_reader = MemoryReader()
    game_stats = GameStats()
    familiar_data = FamiliarData()

    quest_controller = AutoQuestController(auto_quest_model, bot_heroes_gui.get_auto_quest_tab(), familiar_data, logger)
    fish_controller = AutoFishController(auto_fish_model, bot_heroes_gui.get_auto_fish_tab(), logger)
    settings_controller = GeneralSettingsController(general_settings_model, bot_heroes_gui.get_settings_tab(), bot_heroes_gui, logger)
    info_controller = InfoController(bot_heroes_gui.get_info_tab(), logger)
    stats_controller = StatsController(bot_heroes_gui.get_dungeon_stat(), bot_heroes_gui.get_familiar_stat(), bot_heroes_gui.get_fish_stat(), game_stats)
    window_handler = WindowHandler(bot_heroes_gui.get_game_container_frame_id())

    input_handler = InputHandler(memory_reader, window_handler, logger)
    screenshot_tool = ScreenshotTool(window_handler)
    
    state_machine = StateMachine(memory_reader, 
                                 input_handler, 
                                 auto_quest_model, 
                                 auto_fish_model, 
                                 general_settings_model, 
                                 game_stats, 
                                 window_handler, 
                                 screenshot_tool,
                                 logger)

    game_automation_controllers = [quest_controller, fish_controller]
    setting_configuration_controllers = [settings_controller, info_controller]

    autopilot_starter = AutoPilotStarter(game_automation_controllers, 
                                         setting_configuration_controllers, 
                                         bot_heroes_gui.get_button_on_off(), 
                                         state_machine, 
                                         screenshot_tool,
                                         memory_reader,
                                         logger)

    bot_heroes_gui.apply_tab_configurations()
    bot_heroes_gui.mainloop()
  


