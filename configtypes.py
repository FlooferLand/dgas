#from presences.presences import Predefined

class Predefined:
    UnrealEngine = 0
    taskmgr = 1
    Notepad = 2


class Image:
    image, tooltip = "", ""
    def __init__(self, image, tooltip):
        self.image   = image
        self.tooltip = tooltip

