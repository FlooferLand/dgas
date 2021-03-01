import pypresence
from time import sleep
from time import time as getTimeNow
import time
import tools

def program():
    #from presences.presences import config
    from presences.presences import program as presencesProgram
    config = presencesProgram()
    #print(config)

    print("""
    WARNING! This project is not finished and code hasn't been documented.\n
    Use with care (and know why my code looks like nonsense).\n
    A finished version should come in a few months. Feel free to contribute however you may.
    """)

    using_predefined_presence = hasattr(config, "implementation_name")

    process = tools.GetProcessIfExists(config.process_name) if config is not None else None
    title = tools.GetWindowTitleIfExists(config)

    client = None
    if process is not None:
        client = pypresence.Presence(client_id=config.client_id)
        print("Connecting to Discord..")
        client.connect()
        if using_predefined_presence:
            print(f"Connected to Discord as the \"{config.implementation_name}\" Rich Presence")
        else:
            print("Connected!")
    else:
        print("Process died before i was even able to get it.")
        return 0

    def rin(var, old, new):
        # Return new if var is old else var
        return var.replace(('$'+old),new)

    dateStarted = getTimeNow()
    programProjectSeparator = config.programProjectSeparator if hasattr(config, "programProjectSeparator") else '-'

    def RIN(var):  # Replace If Needed (to)
        if type(var) == str:
            projectName = title.split(programProjectSeparator)
            if hasattr(config, "projectAliases"):
                for alias in config.projectAliases:
                    if alias[0] == projectName[0] or alias[0] == projectName[0]:
                        projectName = alias[1]
            var = rin(var, "titleFull", title)
            if len(projectName) > 1:
                var = rin(var, "titleLeft", projectName[0])
                var = rin(var, "titleRight", projectName[1])
            var = rin(var, "timeElapsed",
                time.strftime(
                    "%H:%M:%S",time.gmtime(int(getTimeNow() - dateStarted))
                )
            )
        return var

    while True:
        if process.is_running():
            wantsDate = (hasattr(config, "startDate") and config.startDate is not None)
            client.update(
                pid         = RIN(process.pid),
                state       = RIN(config.state),
                details     = RIN(config.details),
                start       = RIN(config.startDate if wantsDate else None),
                end         = RIN(getTimeNow() if wantsDate else None),
                large_text  = RIN(config.large.tooltip),
                large_image = RIN(config.large.image),
                small_text  = RIN(config.small.tooltip),
                small_image = RIN(config.small.image),
                instance = False
            )
        else:
            print(f'Process "{process.name()}" committed aliven\'t!')
            client.close()
            return 0
        sleep(config.sleep)
while True:
    if program() == 0:
        print("Waiting for a known program to be launched..")
        sleep(5)
