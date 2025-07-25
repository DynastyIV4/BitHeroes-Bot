from core.models.Coordinates import Coordinates
from core.WindowHandler import WindowHandler
from core.Errors import InputControllerClickError
from core.Observer import Publisher
from core.constants.GuiData import APPLICATION_NAME
from gui.widgets.CTkLogger import CTkLogger


from pyautogui import click, moveTo, press, FailSafeException
from time import sleep

class InputHandler(Publisher):
    
    def __init__(self, window_handler: WindowHandler, logger: CTkLogger):
        super().__init__()
        self.window_handler = window_handler
        self.logger = logger

    # =======================
    # PRIVATE METHODS
    # =======================
    
    def _press(self, key: str):
        self.notify()
        self.window_handler.focus_window()
        press(key)
    
    # =======================
    # PUBLIC METHODS
    # =======================

    def click(self, coordinates: Coordinates, delay: float = 0.5, focus: bool = True):
        if focus:
            self.window_handler.focus_window()
        try:
            self.notify()
            
            left, top, right, bottom = WindowHandler.get_game_dimension()
            rel_x = left + coordinates.x
            rel_y = top + coordinates.y

            moveTo(rel_x, rel_y)
            click()
            sleep(delay)

        except IndexError:
            self.logger.print(f"Window with title '{APPLICATION_NAME}' not found.")
        except FailSafeException:
            raise InputControllerClickError("window")
    
    def click_menu(self, 
                    coordinates: Coordinates, 
                    button_name: str, 
                    is_in_expected_state_callback: callable, 
                    attempts: int = 4):
        self.logger.print(f"Clicking on the {button_name} button")
        for attempt in range(attempts):
            self.click(coordinates)
            sleep(1)
            if is_in_expected_state_callback():
                return
            self.logger.print(f"Waiting for the {button_name} window to open...")
        raise InputControllerClickError(button_name)
    
    def close_windows(self, 
                       is_in_expected_state_callback: callable, 
                       attempts: int = 4):
        if not is_in_expected_state_callback():
            for attempt in range(attempts):
                self.escape()
                sleep(1)
                if is_in_expected_state_callback():
                    self.logger.print("All windows closed")
                    return
                self.logger.print("Waiting for the windows to close...")
            raise InputControllerClickError("window")
        
    def fast_click(self, coordinates: Coordinates):
        self.click(coordinates, delay=0, focus=False)
    
    def escape(self, delay: float = 0.5):
        self._press("esc")
        self.logger.print("Pressed the escape key")
        sleep(delay)
