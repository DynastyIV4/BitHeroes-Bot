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
            img = self.screenshot(focus)
            pixels = img.load()
            abs_x, abs_y = WindowHandler.get_absolute_coordinates(coordinates)
            return pixels[abs_x, abs_y]
        except IndexError:
            raise UnableToFocusError("Bit Heroes")

    def screenshot(self, focus: bool = True, *args, **kwargs) -> Image.Image:
        if focus:
            self.window_handler.focus_window()
        self.notify()
        region = kwargs.get('region')
        return screenshot(region=region) if region else screenshot()

    def matches_expected_color(self, color_coordinates: ColorCoordinates, focus: bool = True) -> bool:
        actual_pixel_color = self.get_color_pixel(color_coordinates, focus)
        expected = (color_coordinates.color.red, color_coordinates.color.green, color_coordinates.color.blue)
        return actual_pixel_color[:3] == expected
    
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