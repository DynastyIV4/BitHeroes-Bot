from core.models.Coordinates import Coordinates
from core.models.Worms import WormRarity
from core.MemoryReader import MemoryReader
from core.WindowHandler import WindowHandler
from core.Errors import InputControllerClickError
from core.Observer import Publisher
from core.constants.GuiData import APPLICATION_NAME
from core.constants.CoordinatesData import COORDINATES
from gui.widgets.CTkLogger import CTkLogger


from pyautogui import click, moveTo, press, FailSafeException
from time import sleep

class InputHandler(Publisher):
    
    def __init__(self, memory_reader: MemoryReader, window_handler: WindowHandler, logger: CTkLogger):
        super().__init__()
        self.memory_reader = memory_reader
        self.window_handler = window_handler
        self.logger = logger

    def _click(self, coordinates: Coordinates, delay: float = 0.5):
        self.window_handler.focus_window()
        try:
            self.notify()
            sleep(delay)
            
            left, top, right, bottom = WindowHandler.get_game_dimension()
            rel_x = left + coordinates.x
            rel_y = top + coordinates.y

            moveTo(rel_x, rel_y)
            click()

        except IndexError:
            self.logger.print(f"Window with title '{APPLICATION_NAME}' not found.")
        except FailSafeException:
            raise InputControllerClickError("window")


    def _fast_click(self, coordinates: Coordinates):
        self._click(coordinates, 0)

    def _press(self, key: str):
        self.notify()
        self.window_handler.focus_window()
        press(key)

    def _escape(self):
        self._press("esc")
        self.logger.print("Pressed the escape key")
            
    def _click_menu(self, coordinates, button_name, initial_levels, expected_level, error_message):
        if not isinstance(initial_levels, list):
            initial_levels = [initial_levels]
        if self.memory_reader.get_window_level() not in initial_levels:
            raise Exception(error_message)
        self.logger.print(f"Clicking on the {button_name} button")
        for attempt in range(4):
            self._click(coordinates)
            sleep(1)
            if self.memory_reader.get_window_level() == expected_level:
                return
            self.logger.print(f"Waiting for the {button_name} window to open...")
        raise InputControllerClickError(button_name)
    
    def _close_windows(self, expected_level: int):
        if self.memory_reader.get_window_level() != expected_level:
            for attempt in range(10):
                self._escape()
                sleep(1)
                if self.memory_reader.get_window_level() == expected_level:
                    self.logger.print("All windows closed")
                    return
                self.logger.print("Waiting for the windows to close...")
            raise InputControllerClickError("window")

    # =======================
    # PUBLIC METHODS
    # =======================

    def click_quest(self):
        self._click_menu(COORDINATES["quest"], "quest", 0, 1, "Not in the main window.")
    
    def click_dungeon(self, zone: int, dungeon: int):
        self._click_menu(COORDINATES["dungeon"][str(zone)][str(dungeon)], "dungeon", 1, 3, "Not in the quest window.")

    def click_difficulty(self, difficulty: str):
        self._click_menu(COORDINATES[str(difficulty).lower()], "difficulty", 3, 4, "Not in the difficulty window.")

    def click_auto_team(self):
        self._click_menu(COORDINATES["auto_team"], "auto team", 4, 4, "Not in the difficulty window.")
    
    def click_accept_team(self):
        self._click_menu(COORDINATES["accept_team"], "accept team", 4, 1, "Not in the difficulty window.")

    def click_settings(self):
        self._click_menu(COORDINATES["menu_settings"], "settings", 0, 1, "Not in the main window.")
    
    def close_menu_windows(self):
        self._close_windows(0)

    def close_fish_window(self):
        self._close_windows(1)

    def close_persuasion_window(self):
        self._close_windows(1)
    
    def click_fish_menu(self):
        self._click_menu(COORDINATES["fishing"], "fishing", 0, 1, "Not in the fishing window.")

    def click_fish_play(self):
        self._click(COORDINATES["fish_play"])
    
    def click_fish_start(self):
        self._click(COORDINATES["fish_start"])
    
    def click_fish_cast(self):
        self._fast_click(COORDINATES["fish_cast"])
    
    def click_fish_catch(self):
        self._fast_click(COORDINATES["fish_catch"])

    def click_auto_pilot(self):
        self._click(COORDINATES["auto_pilot"])

    def click_return_home(self):
        self._click(COORDINATES["return_home"])
    
    def click_rerun_dungeon(self):
        self._click(COORDINATES["rerun_dungeon"])

    def click_decline_familiar(self):
        self._click(COORDINATES["decline_familiar"])
    
    def click_accept_familiar(self):
        self._click(COORDINATES["accept_familiar"])
        
    def click_confirm_familiar(self):
        self._click(COORDINATES["confirm_familiar"])
    
    def click_worm_window(self):
        self._click_menu(COORDINATES["select_worm"], "select worm", [0,1], 2, "Not in the fishing state window.")
    
    def close_window(self):
        self._escape()

    def select_worm(self, rarity: WormRarity, available_worms: list[WormRarity]):
        rarity_weights = {
            WormRarity.LEGENDARY: 1,
            WormRarity.EPIC: 2,
            WormRarity.RARE: 3,
            WormRarity.COMMON: 4,
        }

        available_weights = {worm: rarity_weights[worm] for worm in available_worms}
        sorted_worms = sorted(available_weights, key=available_weights.get)

        box_index = sorted_worms.index(rarity) + 1
        self._click(COORDINATES[f"worm_box_{box_index}"])
    