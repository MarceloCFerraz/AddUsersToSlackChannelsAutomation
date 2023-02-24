import os
import openpyxl

CHANNELS_LIST_DEFAULT_NAME = "channels.xlsx"
FORBIDDEN_CATEGORIES = [
    "Automated Notices",
    "Defunct",
    "Social",
    "Target Dispatch"
]

def exists():
    current_dir = os.listdir()
    if CHANNELS_LIST_DEFAULT_NAME in current_dir:
        return True
    return False


def get():
    file = openpyxl.load_workbook(CHANNELS_LIST_DEFAULT_NAME)
    return file


def clearForbiddenCategories(file):
    print("need to implement this!")