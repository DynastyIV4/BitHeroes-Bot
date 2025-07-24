from core.models.Coordinates import Coordinates
from core.models.ColorCoordinates import ColorCoordinates
from core.WindowHandler import WindowHandler
from core.Observer import Publisher
from core.Errors import UnableToFocusError

from pyautogui import screenshot
from PIL import Image

class ScreenshotTool(Publisher):
    
    # =======================
    # PUBLIC METHODS
    # =======================

    def __init__(self, window_handler: WindowHandler):
        super().__init__()
        self.window_handler = window_handler
    
    def get_color_pixel(self, coordinates: Coordinates, focus: bool = True) -> tuple:
        try:
            return self.screenshot(focus).getpixel(WindowHandler.get_absolute_coordinates(coordinates))
        except IndexError:
            raise UnableToFocusError("Bit Heroes")
        
    def screenshot(self, focus: bool = True, *args, **kwargs) -> Image.Image:
        if focus:
            self.window_handler.focus_window()
        self.notify()
        return screenshot(*args, **kwargs)
        
    
    def matches_expected_color(self, color_coordinates: ColorCoordinates, focus: bool = True) -> bool:
        actual_pixel_color = self.get_color_pixel(color_coordinates, focus)
        if (actual_pixel_color[0] == color_coordinates.color.red and \
                actual_pixel_color[1] == color_coordinates.color.green and \
                actual_pixel_color[2] == color_coordinates.color.blue):
            return True
        return False
    
    # =======================
    # PRIVATE METHODS
    # =======================

    def get_screenshot_region(self, top_left: Coordinates, bottom_right: Coordinates) -> tuple:
        left, top, right, bottom = WindowHandler.get_game_dimension()
        x = left + top_left.x
        y = top + top_left.y
        width = left + bottom_right.x - x
        height = top + bottom_right.y - y
        return (x, y, width, height)