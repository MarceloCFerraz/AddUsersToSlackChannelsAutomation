from utils import file, get, gui


def printLine():
    print("--------------------------------------------")


def printChannelsDict(channels_dict):
    for key in channels_dict.keys():
        print("{} ({} channels): ".format(key, len(channels_dict[key])), end="")
        print(channels_dict[key])
        printLine()


if __name__ == "__main__":
    if file.fileExists:
        print("File found")
        printLine()

        print("Loading File", end="\n{}".format(printLine()))

        file = file.getFile()
        sheet = file.active
        
        channels_index = get.getChannelNameColumnIndex(sheet)
        category_index = get.getCategoryColumnIndex(sheet)

        if channels_index != None and category_index != None:
            channels_dict = get.getChannelsDict(sheet)
            
            # printChannelsDict(channels_dict)

            # for key in channels_dict.keys():
                # gui.createCategoriesAtSlack(channels_dict.keys())
                # gui.enterSlackChannels(key, channels_dict[key])
            
        else:
            print("Your sheet doesn't have a 'Channel Name' or a 'Category' header\n"+
                  "Please, check 'model.xlsx' and correct you channels file")
    else:
        print(
            "Channels file wasn't found.\n"+
            "Please, make sure to rename it to 'channels.xlsx' "+
            "and that it is strutcurally equal to 'model.xlsx' present in this folder."
        )