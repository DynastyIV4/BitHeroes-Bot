from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import CTkTextbox

class CTkLogger(CTkTextbox):

    def __init__(self, parent, tooltip=None, tooltip_parameters=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.insert("1.0", "GAME LOG\n")
        self.configure(state="disabled")
        MyCTkToolTip(self, tooltip, **tooltip_parameters)

    def print(self, text: str):
        self.configure(state="normal")
        self.insert("end", text + "\n")
        self.see("end")
        self.configure(state="disabled")
    
    def print_override(self, text: str):
        self.configure(state="normal")
        lines = self.get("1.0", "end-1c").split("\n")
        if len(lines) > 1:  
            last_line_start = f"{len(lines) - 1}.0"
            self.delete(last_line_start, "end-1c")
        self.insert("end", self.time_header() + text + "\n")
        self.configure(state="disabled")