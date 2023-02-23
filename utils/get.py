import openpyxl
from .file import FORBIDDEN_CATEGORIES, getFile

sheet = getFile().active
categories_index = 2
channels_index = 1


def getChannelNameColumnIndex():
    for row_index in range(1, sheet.max_row):
        for column_index in range(1, sheet.max_column):
            cell = sheet.cell(row=row_index, column=column_index)
            value = cell.value

            if "Channel Name" == value:
                channels_index = column_index
                return column_index
    return None
    

def getCategoryColumnIndex():
    for row_index in range(1, sheet.max_row):
        for column_index in range(1, sheet.max_column):
            cell = sheet.cell(row=row_index, column=column_index)
            value = cell.value

            if "Category" == value:
                categories_index = column_index
                return column_index
    return None


def getCategoriesList():
    categories_list = []
    
    for row_index in range(2, sheet.max_row):
        #it jumps the first line because it's where the header is located
        
        cell = sheet.cell(row=row_index, column=categories_index)
        value = cell.value

        if value != None and value not in categories_list and value not in FORBIDDEN_CATEGORIES:
            categories_list.append(value)
    
    return categories_list


def getChannelsList(category):
    channels_list = []
    firstCategoryRow = getCategoryFirstRow(category)

    if firstCategoryRow != None:
        for row_index in range(firstCategoryRow, sheet.max_row):
            #it jumps the first line because it's where the header is located
            channel_name = sheet.cell(row=row_index, column=channels_index).value
            category_name = sheet.cell(row=row_index, column=categories_index).value
            
            if category != category_name:
                return channels_list

            channels_list.append(channel_name)


def getCategoryFirstRow(category):
    for row_index in range (2, sheet.max_row):
        category_name = sheet.cell(row=row_index, column=categories_index).value

        if category == category_name:
            return row_index
    return None


def getChannelsDict():
    # channels_dict = 
    # {
    #   "category name": [
    #                       "channel 1", 
    #                       "channel 2", 
    #                       ...
    #                   ] 
    # }

    channels_dict = {}
    channels_list = []
    past_category = ""

    for row_index in range(2, sheet.max_row):
        # it jumps the first line because it's where the header is located

        channel_name = sheet.cell(row=row_index, column=channels_index).value
        category = sheet.cell(row=row_index, column=categories_index).value
        
        if channel_name != None and category != None and category not in FORBIDDEN_CATEGORIES:
            if category != past_category:
                past_category = category
                channels_dict[category] = getChannelsList(category)
            else:
                # print(category, end=" - ")
                # print(channel_name)
                channels_list.append(channel_name)
    
    return channels_dict