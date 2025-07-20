from core.constants.GuiData import STAT_FRAME_FONT, STAT_FRAME_SIZE, FRAME_CORNER_RADIUS, \
                                   FAMILIAR_ENCOUNTERED_PATH, FAMILIAR_ENCOUNTERED_SIZE, FAMILIAR_STAT_TOOLTIP
from gui.view_models.StatViewModel import StatViewModel

from customtkinter import CTkBaseClass

class FamiliarStatView(StatViewModel):

    def __init__(self, parent: CTkBaseClass):
        if not hasattr(self, "_initialized"): 
            super().__init__(parent=parent, 
                             image_path=FAMILIAR_ENCOUNTERED_PATH, 
                             image_size=FAMILIAR_ENCOUNTERED_SIZE, 
                             initial_value=0, 
                             font=STAT_FRAME_FONT,
                             width=STAT_FRAME_SIZE[0], 
                             height=STAT_FRAME_SIZE[1], 
                             corner_radius=FRAME_CORNER_RADIUS,
                             tooltip=FAMILIAR_STAT_TOOLTIP)
            self._initialized = True
