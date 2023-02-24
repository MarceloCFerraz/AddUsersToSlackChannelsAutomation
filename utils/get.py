import openpyxl
from utils.file import FORBIDDEN_CATEGORIES
from utils.common import printLine

categories_index = 2
channels_index = 1


def channelNameColumnIndex(sheet):
    print("Searching for the 'Channel Name' column index")
    printLine()

    for row_index in range(1, sheet.max_row):
        for column_index in range(1, sheet.max_column):
            cell = sheet.cell(row=row_index, column=column_index)
            value = cell.value

            if "Channel Name" == value:
                print("'Channel Name' found at column {}".format(column_index))
                printLine()
                return column_index
    
    print("COLUMN NOT FOUND!")
    return None
    

def categoryColumnIndex(sheet):
    print("Searching for the 'Category' column index")
    printLine()

    for row_index in range(1, sheet.max_row):
        for column_index in range(1, sheet.max_column):
            cell = sheet.cell(row=row_index, column=column_index)
            value = cell.value

            if "Category" == value:
                print("'Category' found at column {}".format(column_index))
                printLine()
                return column_index
    
    print("COLUMN NOT FOUND!")
    return None


def channelsListFromCategory(sheet, category, category_row_index):
    channels_list = []

    for row_index in range(category_row_index, sheet.max_row):
        #it jumps the first line because it's where the header is located
        channel_name = sheet.cell(row=row_index, column=channels_index).value
        category_name = sheet.cell(row=row_index, column=categories_index).value
        
        if category == category_name:
            channels_list.append(channel_name)

    print("Channels list for {} filled successfully with ".format(category)+
          "{} items".format(len(channels_list)))
    printLine()

    return channels_list


def channelsDict(sheet):
    # channels_dict = 
    # {
    #   "category name": [ "channel 1", "channel 2", ... ] 
    # }

    channels_dict = {}
    past_category = ""

    print("This function will avoid all the channels "+
          "on the FORBIDDEN_CATEGORIES list")
    print("The avoided categories are: ")
    for item in FORBIDDEN_CATEGORIES:
        if item == FORBIDDEN_CATEGORIES[len(FORBIDDEN_CATEGORIES) - 2]:
            # if it is the penultimate item in list
            print("{}".format(item), end=" and ")
        elif item == FORBIDDEN_CATEGORIES[len(FORBIDDEN_CATEGORIES) - 1]:
            # if it is the last item in list
            print("{}".format(item), end="\n\n")
        else:
            print("{}".format(item), end=", ")

    print("Starting filling the channels dictionary")
    printLine()

    for row_index in range(2, sheet.max_row):
        # it jumps the first line because it's where the header is located

        channel_name = sheet.cell(row=row_index, column=channels_index).value
        category = sheet.cell(row=row_index, column=categories_index).value
        
        if channel_name != None and category != None and category not in FORBIDDEN_CATEGORIES:
            if category != past_category:
                print("Getting Channels list from {}".format(category) + "category")
                past_category = category
                channels_dict[category] = channelsListFromCategory(sheet, category, row_index)
    
    print("Finished filling the dictionary")
    printLine()
    return channels_dict