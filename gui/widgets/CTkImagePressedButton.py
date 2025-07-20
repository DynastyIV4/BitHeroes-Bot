from abc import abstractmethod
from customtkinter import CTkButton, CTkImage, CTkBaseClass
from PIL import Image

class CTkImagePressedButton(CTkButton):
    def __init__(self, parent: CTkBaseClass, image_normal_path: str, image_normal_dark_path: str, image_pressed_path: str, 
                 image_dark_pressed_path: str, image_size: tuple[int, int], *args, **kwargs):
        self.is_pressed = False
        self.is_hovered = False
        self.image_normal = CTkImage(Image.open(image_normal_path), size=image_size)
        self.image_pressed = CTkImage(Image.open(image_pressed_path), size=image_size)
        self.image_normal_dark = CTkImage(Image.open(image_normal_dark_path), size=image_size)
        self.image_pressed_dark = CTkImage(Image.open(image_dark_pressed_path), size=image_size)
        super().__init__(parent, image=self.image_normal, text="", fg_color=parent.cget("fg_color"), 
                         hover_color=parent.cget("fg_color"), cursor="hand2", *args, **kwargs)
        
        self.bind("<Enter>", self._on_enter_hover)
        self.bind("<Leave>", self._on_leave_hover)
    
    def _on_enter_hover(self, event):
        self.configure(image=self.image_pressed_dark if self.is_pressed else self.image_normal_dark)
        self.is_hovered = True

    def _on_leave_hover(self, event):
        self.configure(image=self.image_pressed if self.is_pressed else self.image_normal)
        self.is_hovered = False

    def press(self):
        self.is_pressed = not self.is_pressed
        if self.is_hovered:
            self.configure(image=self.image_pressed_dark if self.is_pressed else self.image_normal_dark)
        else:
            self.configure(image=self.image_pressed if self.is_pressed else self.image_normal)
