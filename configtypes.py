#from presences.presences import Predefined

class Predefined:
    UnrealEngine = "ue4editor"
    taskmgr = "taskmgr"
    Notepad = "notepad"


class Image:
    image, tooltip = "", ""
    def __init__(self, image, tooltip):
        self.image   = image
        self.tooltip = tooltip

