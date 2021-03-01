import sys
import presences

from presencesTools import *
from configtypes import Predefined

config = import_module("config")

def ProcessOfPresenceExists(name):
    presence = import_module("presences." + name)
    process = GetProcessIfExists(presence.process_name)
    return True if process is not None else False

def Use(name):
    global config
    config = import_module("presences." + name)
    return config

def Define(array):
    if hasattr(config, "presences"):
        for presence in config.presences:
            for predef in array:
                if predef[0] == presence and ProcessOfPresenceExists(predef[1]):
                    if Use(predef[1]) is not None:
                        return Use(predef[1])

def program():
    return Define([
        [Predefined.UnrealEngine, "ue4editor"],
        [Predefined.taskmgr, "taskmgr"],
        [Predefined.Notepad, "notepad"]
    ])