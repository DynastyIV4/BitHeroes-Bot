from customtkinter import CTkFrame
from customtkinter import CTkLabel, CTkImage
from core.constants.GuiData import TOOLTIP_PARAMETERS
from gui.widgets.MyCTkToolTip import MyCTkToolTip


from PIL import Image

class StatViewModel(CTkFrame):

    def __init__(self, 
                 parent, 
                 image_path: str, 
                 image_size: tuple[int,int], 
                 initial_value: int, 
                 tooltip: str,
                 font : tuple[str,int],
                 *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_path = image_path
        self.image_size = image_size
        self.font = font
        self.tooltip = tooltip
        self.corner_radius = kwargs.get("corner_radius", 0)
        self.value: int = initial_value
        self._initialize_components()

    def _initialize_components(self):
        self.pack_propagate(False)
        ctk_image = CTkImage(Image.open(self.image_path), size=self.image_size)
        image_label = CTkLabel(self, text = "", image=ctk_image)
        self.info_label = CTkLabel(self, text=str(self.value), font=self.font)
        image_label.pack(side = "left", padx = ( self.corner_radius, 5))
        self.info_label.pack(side = "left")

        MyCTkToolTip(self, self.tooltip, **TOOLTIP_PARAMETERS)

    def set_value(self, value: int):
        self.info_label.configure(text = str(value))
    