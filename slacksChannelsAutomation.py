from utils import file
from utils import get


if __name__ == "__main__":
    if file.fileExists:
        print("File found")

        file.clearForbiddenCategories(file.getFile())
        
        channels_index = get.getChannelNameColumnIndex()
        category_index = get.getCategoryColumnIndex()

        if channels_index != None and category_index != None:
            channels_dict = get.getChannelsDict()

            for key in channels_dict.keys():
                print("{} ({}): ".format(key, len(channels_dict[key])), end="")
                print(channels_dict[key])
                print("--------------------------------------------")
            
        else:
            print("Your sheet doesn't have a 'Channel Name' or a 'Category' header\n"+
                  "Please, check 'model.xlsx' and correct you channels file")
    else:
        print(
            "Channels file wasn't found.\n"+
            "Please, make sure to rename it to 'channels.xlsx' "+
            "and that it is strutcurally equal to 'model.xlsx' present in this folder."
        )