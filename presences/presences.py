from configtypes import Predefined
from tools import ProcessExists
from tools import GetProcessIfExists
from importlib import import_module

config = import_module("config")

def ProcessOfPresenceExists(name):
    presence = import_module("presences." + name)
    process = GetProcessIfExists(presence.process_name)
    return True if process is not None else False

def Use(name):
    global config
    config = import_module("presences." + name)
    return config

def Define(python_files):
    if hasattr(config, "presences"):
        for presence in config.presences:
            for file in python_files:
                if file == presence and ProcessOfPresenceExists(file):
                    if Use(file) is not None:
                        return Use(file)

def program():
    return Define([
        Predefined.UnrealEngine,
        Predefined.taskmgr,
        Predefined.Notepad
    ])