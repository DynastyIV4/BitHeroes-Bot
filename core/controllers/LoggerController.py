from core.Observer import Subscriber
from core.Logger import Logger
from gui.widgets.CTkLogger import CTkLogger

from datetime import datetime


class LoggerController(Subscriber):

    def __init__(self, logger: Logger, logger_view: CTkLogger):
        super().__init__()
        self._logger = logger
        self._logger_view = logger_view
        self._logger.subscribe(self)
    
    def update(self):
        self._logger_view.print(self.time_header() + self._logger.get_last_line_printed())
    
    def time_header(self) -> str:
        return datetime.now().strftime("%H:%M") + ": "