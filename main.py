from utils import automation, file, get, gui, common


if __name__ == "__main__":

    if file.exists():
        print("File found")
        common.printLine()

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
            print("The automation process will start now!\n"+
                "But first make sure to attend to all the items that will be displayed bellow!\n\n"
            )
            for question_index in range(0, len(common.QUESTIONS)):
                if common.answerCheck(answer):
                    print("({}/{}) {}".format(
                        question_index + 1,
                        len(common.QUESTIONS),
                        common.QUESTIONS[question_index]
                    ))
            
                    print("----> Hit 'enter' if this step was completed")
                    print("----> Hit 'n' to cancel automation ")
                    answer = input(print("--> ", end=""))
                    common.clearConsole()
            
            if common.answerCheck(answer):
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
            "and that it is structurally equal to 'model.xlsx' present in project folder."
        )
    common.exitingProgram()