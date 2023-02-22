import os
import pandas
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import string

CHANNELS_LIST_DEFAULT_NAME = "channels.xlsx"

def fileExists():
    current_dir = os.listdir()
    if CHANNELS_LIST_DEFAULT_NAME in current_dir:
        return True
    return False


if __name__ == "__main__":
    if fileExists:
        print("File found")
        file = pandas.read_excel(CHANNELS_LIST_DEFAULT_NAME)
    else:
        print(
            "Channels file wasn't found.\n"+
            "Please, make sure to rename it to 'channels.xlsx' "+
            "and that it is strutcurally equal to 'model.xlsx' present in this folder."
        )