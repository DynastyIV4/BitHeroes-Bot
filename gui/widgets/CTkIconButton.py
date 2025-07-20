from customtkinter import CTkButton, CTkImage, CTkBaseClass, ThemeManager
from PIL import Image

class CTkIconButton(CTkButton):
    def __init__(self, master: CTkBaseClass, image: CTkImage, *args, **kwargs):
        super().__init__(master, image=image, text="", *args, **kwargs)
        self.master = master
        self.image = image
        self.darken_image = self._darken_image(image)

    def _darken_image(self, image: CTkImage) -> CTkImage:
        pil_image = image._light_image  # Access the underlying PIL.Image
        darkened_pil = pil_image.point(lambda p: p * 0.5)
        return CTkImage(darkened_pil, size=image._size)

    def deselect(self):
        self.configure(image=self.darken_image, fg_color=self.master.cget("fg_color"))
    
    def select(self):
        self.configure(image=self.image, fg_color=ThemeManager.theme["CTkButton"]["fg_color"])
        
