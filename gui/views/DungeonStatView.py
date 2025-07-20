from core.constants.GuiData import DUNGEON_PATH, DUNGEON_SIZE, STAT_FRAME_FONT, STAT_FRAME_SIZE, \
                                   FRAME_CORNER_RADIUS, DUNGEON_STAT_TOOLTIP
from gui.view_models.StatViewModel import StatViewModel

from customtkinter import CTkBaseClass
class DungeonStatView(StatViewModel):

    def __init__(self, parent: CTkBaseClass):
        if not hasattr(self, "_initialized"): 
            super().__init__(parent=parent, 
                             image_path=DUNGEON_PATH, 
                             image_size=DUNGEON_SIZE, 
                             initial_value=0, 
                             font=STAT_FRAME_FONT,
                             width=STAT_FRAME_SIZE[0], 
                             height=STAT_FRAME_SIZE[1], 
                             corner_radius=FRAME_CORNER_RADIUS,
                             tooltip=DUNGEON_STAT_TOOLTIP)
            
            self._initialized = True