from configtypes import *

# Process
process_name = "ue4editor.exe"
#process_name = "wordpad.exe"
title_contains = "Unreal Editor"

# Discord Rich Presence
client_id = 813881021383573574
implementation_name = "Unreal Engine"


# Styling
state = "Time spent: $timeElapsed"
details = "Working on $project"
projectAliases = [
    ["SurvivalGame", "UNTITLED SANDBOX GAME"],
    ["InterstateDriftr2006", "Interstate Drifter 2006 (fangame)"]
]

large = Image(image="ue4_white", tooltip="Unreal Engine 4.26.1")
small = Image(image=None, tooltip="Unreal Engine 4.26.1")
sleep = 1.0
wantsDate = True
