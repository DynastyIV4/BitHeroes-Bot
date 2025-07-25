from gui.widgets.CTkLogger import CTkLogger
from core.models.Coordinates import Coordinates
from core.constants.ConfigData import BIT_HEROES_WINDOW_TITLE, BIT_HEROES_BOT_WINDOW_TITLE
from core.constants.GuiData import APPLICATION_NAME, GAME_FRAME_INTERNAL_PADDING, GAME_FRAME_PADDING, WINDOWS_TOP_BAR_HEIGHT, WINDOWS_LEFT_BAR_WIDTH, \
                                   RECTANGLE_MASK, CONTAINER_FRAME_RADIUS, BIT_HEROES_SIZE, BIT_HEROES_SIZE_2
from core.Errors import UnableToFocusError, UnableToFindWindow

from pygetwindow import getWindowsWithTitle
import win32gui
import win32con
from time import sleep


class WindowHandler:
    
    def __init__(self, game_container_frame_id: str):
        self._game_container_frame_id = game_container_frame_id
        self._hwnd = None

    def focus_window(self, attempts: int = 3):
        for _ in range(attempts):
            try:
                bot_windows = getWindowsWithTitle(BIT_HEROES_BOT_WINDOW_TITLE)
                if not bot_windows:
                    raise UnableToFindWindow("BitHeroes-Bot")
                bot_windows[0].activate()
                sleep(0.01)

                if self._hwnd is None:
                    raise UnableToFindWindow("Bit Heroes")

                if win32gui.IsIconic(self._hwnd):
                    win32gui.ShowWindow(self._hwnd, win32con.SW_RESTORE)

                win32gui.SetForegroundWindow(self._hwnd)
                return
            except Exception:
                continue
        raise UnableToFocusError("Bit Heroes")
    

    def attach_bit_heroes_window(self):
        def enum_windows_callback(hwnd, windows: list):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == BIT_HEROES_WINDOW_TITLE:
                windows.append(hwnd)

        bit_heroes_windows = []
        win32gui.EnumWindows(enum_windows_callback, bit_heroes_windows)

        if not bit_heroes_windows:
            CTkLogger._instance.print(f"Window with title '{BIT_HEROES_WINDOW_TITLE}' not found.")
            return

        # Resize the Bit Heroes window before attaching and styling
        win32gui.SetWindowPos(
            bit_heroes_windows[0],
            None,
            0,
            0,
            BIT_HEROES_SIZE_2[0],
            BIT_HEROES_SIZE_2[1],
            win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE
        )

        self._hwnd = bit_heroes_windows[0]
        win32gui.SetParent(self._hwnd, self._game_container_frame_id)
        win32gui.SetWindowLong(
            self._hwnd,
            win32con.GWL_STYLE,
            win32gui.GetWindowLong(self._hwnd, win32con.GWL_STYLE) & ~win32con.WS_CAPTION
        )
        win32gui.SetWindowRgn(
            self._hwnd,
            win32gui.CreateRoundRectRgn(0, 0, RECTANGLE_MASK[0], RECTANGLE_MASK[1], CONTAINER_FRAME_RADIUS, CONTAINER_FRAME_RADIUS),
            True
        )
        win32gui.SetWindowPos(
            self._hwnd,
            None,
            0,
            0,
            BIT_HEROES_SIZE[0],
            BIT_HEROES_SIZE[1],
            win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE
        )
        win32gui.ShowWindow(self._hwnd, win32con.SW_SHOW)

        try:
            win32gui.SetForegroundWindow(self._hwnd)
        except Exception:
            raise UnableToFocusError("Bit Heroes")
    
    def is_game_running(self):
        bit_heroes_windows = []
        win32gui.EnumWindows(
            lambda hwnd, windows: windows.append(hwnd) if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == BIT_HEROES_WINDOW_TITLE else None,
            bit_heroes_windows
        )
        return bool(bit_heroes_windows)

    @staticmethod
    def get_game_dimension() -> tuple:
        window = getWindowsWithTitle(APPLICATION_NAME)[0]
        left = WINDOWS_LEFT_BAR_WIDTH + window.left + GAME_FRAME_INTERNAL_PADDING + GAME_FRAME_PADDING
        top = WINDOWS_TOP_BAR_HEIGHT + window.top + GAME_FRAME_INTERNAL_PADDING + GAME_FRAME_PADDING
        right = left + BIT_HEROES_SIZE[0] - GAME_FRAME_INTERNAL_PADDING * 2
        bottom = top + BIT_HEROES_SIZE[1] - GAME_FRAME_INTERNAL_PADDING * 2
        return int(left), int(top), int(right), int(bottom)

    @staticmethod
    def get_absolute_coordinates(coordinates: Coordinates) -> tuple:
        left, top, right, bottom = WindowHandler.get_game_dimension()
        return left + coordinates.x, top + coordinates.y
    
