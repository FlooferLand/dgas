import os
import psutil
import pygetwindow

def GetProcesses():
    processList = []
    processListLines = os.popen("wmic process get description, processid").read().split('\n')
    for processLine in processListLines:
        if len(processLine) < 1: continue
        process = ' '.join(processLine.strip().split()).split(' ')
        if process[1].isnumeric():
            if ProcessExists(process[1]):
                processList.append(psutil.Process(int(process[1])))
    return processList

def GetProcessIfExists(name):
    processList = GetProcesses()
    for i in range(0, len(processList)):
        process = processList[i]
        if process.name().lower() == name.lower():
            if process is not None:
                return process
        if process.name() != name and i == len(processList):
            print(f"Process \"{name}\" wasn't found")
            exit()

def ProcessExists(process):
    if process is None:
        return False
    elif type(process) is int:
        return psutil.pid_exists(pid=process)
    elif type(process) is str:
        return psutil.pid_exists(pid=int(process))
    return psutil.pid_exists(pid=process.pid)

def GetProcessName(pid):
    p = psutil.Process(pid)
    return p.name()

def GetWindowTitleIfExists(config):
    __configContainsTitle__ = hasattr(config, "title_contains")
    for _title in pygetwindow.getAllTitles():
        if __configContainsTitle__:
            if len(_title) < 1: continue
            if config.title_contains.lower() in _title.lower():
                return _title
