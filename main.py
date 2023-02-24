import os
from utils import automation, file, get, gui
from utils.image import image, limiarization, text

QUESTIONS = [
    "The automation process will start now!\n"+
    "But first, make sure the slack is open and that"+
    "its shortcut is pinned at the 4th position on the task bar!\n"+
    "If the position is different or the program isn't open, nothing will work!\n",

    "Now please make sure you are at the right Slack Workspace\n"+
    "The workspace should be the account you were assigned to (e.g. MileZero)\n",

    "You need to set:\n"+
    "----> Monitor Resolution set to 1920 x 1080 pixels\n"+
    "----> Screen scale set to 125% (windows scale)\n",

    "You need to use SLACK DESKTOP APP "+
    "AND let it's WINDOW MAXIMIZED\n",

    "You need to let the all the CHANNELS and DIRECT MESSAGES in Slack MINIMIZED\n"+
    "They need to have an → (right arrow) symbol to represent that they are minimized\n"+
    "instead of a ↓ (down arrow)"
]

def printLine():
    print("--------------------------------------------")


def printChannelsDict(channels_dict):
    for key in channels_dict.keys():
        print("{} ({} channels): ".format(key, len(channels_dict[key])), end="")
        print(channels_dict[key])
        printLine()


def exitingProgram():
    print("Exiting program...")


def answerCheck():
    return answer == "" or answer.capitalize() == "Y"


def clearConsole():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


if __name__ == "__main__":
    # gui.time.sleep(5)
    # img = image.imgToGray(
    #     image.printScreen(
    #         automation.COORDINATES["search_input_item"][0],
    #         automation.COORDINATES["search_input_item"][1],
    #         automation.COORDINATES["search_input_item"][2],
    #         automation.COORDINATES["search_input_item"][3],
    #     )
    # )
    # img = image.expand(limiarization.otsu(img), 2)
    # x, y, w, h, img, achou = text.findTextOnImg(text.extractDict(img),img, "clm-cnc-dispatch")

    # image.showImage(img, "")

    # gui.click(
    #     automation.COORDINATES["search_input_item"][0] + (x / 2) + (w / 4),
    #     automation.COORDINATES["search_input_item"][1] + (y / 2) + (h / 4)
    # )

    if file.exists():
        print("File found")
        printLine()

        print("Loading File")
        file = file.get()
        sheet = file.active
        
        channels_index = get.channelNameColumnIndex(sheet)
        category_index = get.categoryColumnIndex(sheet)

        if channels_index != None and category_index != None:
            channels_dict = get.channelsDict(sheet)
            file.close()
            answer = ""
            
            spaces = "========================"
            print("\n\n{0} ATTENTION {0}\n".format(spaces))
            for question_index in range(0, len(QUESTIONS)):
                if answerCheck():
                    print("({}/{}) {}".format(
                        question_index + 1,
                        len(QUESTIONS),
                        QUESTIONS[question_index]
                    ))
                    answer = input(print("\n\nIs this step finished? (Y/n)", end=" "))
                    clearConsole()
            
            if answerCheck():
                print("DON'T SWITCH BACK TO SLACK")
                print("DON'T TOUCH THE KEYBOARD OR MICE")
                print("\nGo grab a coffee and come back again to check up if everything is working fine")
                print("Automation will start in... ")
                gui.countdown(3)
                automation.start(channels_dict)
        else:
            print("Your sheet doesn't have a 'Channel Name' or a 'Category' header\n"+
                  "Please, check 'model.xlsx' and correct you channels file")
    else:
        print(
            "Channels file wasn't found.\n"+
            "Please, make sure to rename it to 'channels.xlsx' "+
            "and that it is strutcurally equal to 'model.xlsx' present in this folder."
        )
    exitingProgram()