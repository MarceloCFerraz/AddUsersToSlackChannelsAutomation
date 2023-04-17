import os
from termcolor import cprint, colored

STANDARD_SLEEP_TIME = 1 # seconds

QUESTIONS = [
    "Make sure that slack is open and that "+
    "its shortcut is pinned at the 4th position on the task bar!\n"+
    "If the position is different or the program isn't open, nothing will work!\n",

    "Now please make sure you are at the right Slack Workspace\n"+
    "The workspace should be the account you were assigned to (e.g. MileZero)\n",

    "You need to set:\n"+
    "** Monitor Resolution set to 1920 x 1080 pixels **\n"+
    "** Screen scale set to 100% (windows scale) **\n",

    "You need to use SLACK DESKTOP APP "+
    "AND let its WINDOW MAXIMIZED but not in FULL SCREEN MODE\n",

    "It is important that you ARE a member of any channel on the list\n"+
    "If you're not, please join the channels and come back",

    "Make sure to disable any notifications on your computer!\n"
]

def printLine():
    
    print("--------------------------------------------")


def printChannelsDict(channels_dict):
    for key in channels_dict.keys():
        print("{} ({} channels): ".format(key, len(channels_dict[key])), end="")
        print(channels_dict[key])
        printLine()


def exitingProgram():
    print("\nExiting program...")


def answerCheck(answer):
    return answer == "" or answer.capitalize() == "Y"


def clearConsole():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
