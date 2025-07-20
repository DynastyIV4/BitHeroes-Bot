from core.models.Coordinates import Coordinates
from core.models.ColorCoordinates import ColorCoordinates
from core.models.Worms import WormRarity
from core.WindowHandler import WindowHandler
from core.constants.CoordinatesData import COORDINATES, COMMON_WORM_COLOR, RARE_WORM_COLOR, EPIC_WORM_COLOR, LEGENDARY_WORM_COLOR, \
                                           NO_WORM_COLOR

from pyautogui import screenshot
from PIL import Image

class ScreenshotTool:
    
    # ----------------
    # PRIVATE METHODS
    # ----------------

    def __init__(self, window_handler: WindowHandler):
        self.window_handler = window_handler
        
    def _screenshot(self, *args, **kwargs) -> Image.Image:
        self.window_handler.focus_window()
        return screenshot(*args, **kwargs)

    def _get_color_pixel(self, coordinates: Coordinates) -> tuple:
        return self._screenshot().getpixel(WindowHandler.get_absolute_coordinates(coordinates))
    
    def _verify_color_coordinate(self, color_coordinates: ColorCoordinates) -> bool:
        actual_pixel_color = self._get_color_pixel(color_coordinates)
        if (actual_pixel_color[0] == color_coordinates.color.red and \
                actual_pixel_color[1] == color_coordinates.color.green and \
                actual_pixel_color[2] == color_coordinates.color.blue):
            return True
        return False
        
    def _get_screenshot_region(self, top_left: Coordinates, bottom_right: Coordinates) -> tuple:
        left, top, right, bottom = WindowHandler.get_game_dimension()
        x = left + top_left.x
        y = top + top_left.y
        width = left + bottom_right.x - x
        height = top + bottom_right.y - y
        return (x, y, width, height)
    
    # ----------------
    # PUBLIC METHODS
    # ----------------

    def take_persuasion_screenshot(self) -> Image.Image:
        #TODO: FOCUS WINDOW
        return self._screenshot(region=self._get_screenshot_region(COORDINATES["persuasion_top_left"], COORDINATES["persuasion_bottom_right"]))
    
    def get_available_worms(self) -> list[WormRarity]:
        available_worms = []
        screenshot = self._screenshot()
        for i in range(1, 5):
            worm_color = screenshot.getpixel(WindowHandler.get_absolute_coordinates(COORDINATES[f"worm_box_{i}"]))
            if worm_color == COMMON_WORM_COLOR:
                available_worms.append(WormRarity.COMMON)
            elif worm_color == RARE_WORM_COLOR:
                available_worms.append(WormRarity.RARE)
            elif worm_color == EPIC_WORM_COLOR:
                available_worms.append(WormRarity.EPIC)
            elif worm_color == LEGENDARY_WORM_COLOR:
                available_worms.append(WormRarity.LEGENDARY)
        return available_worms
    
    def is_fishing_state(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["is_fishing_state"])

    def is_fish_min_range(self) -> bool:
        return not self._verify_color_coordinate(COORDINATES["fish_minimum_range"])

    def is_fish_max_catch_rate(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["fish_max_catch_rate"])

    def is_trash(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["is_trash"])
    
    def is_home_state(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["is_home_state"])

    def is_dungeon_auto_pilot_disabled(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["is_auto_pilot_disabled"])
    
    def current_worm(self) -> WormRarity:
        worm_color = self._screenshot().getpixel(WindowHandler.get_absolute_coordinates(COORDINATES["worm_bar_box"]))
        if worm_color == COMMON_WORM_COLOR:
             return WormRarity.COMMON
        elif worm_color == RARE_WORM_COLOR:
            return WormRarity.RARE
        elif worm_color == EPIC_WORM_COLOR:
            return WormRarity.EPIC
        elif worm_color == LEGENDARY_WORM_COLOR:
            return WormRarity.LEGENDARY
        elif worm_color == NO_WORM_COLOR:
            return WormRarity.NONE
        raise Exception("Something went wrong, no worms color has been detected")

    def is_disconnected(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["is_disconnected"])

    def persuasion_has_succeeded(self) -> bool:
        return self._verify_color_coordinate(COORDINATES["persuasion_has_succeeded"])