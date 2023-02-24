import time
from utils import gui, common
from utils.image import text, image, limiarization


COORDINATES = {
    "top_of_slack": (1505, 26),
    "channels": (140, 379),
    "channels_manage": (210, 460),
    "channels_explore": (491, 543),
    "search_input": (485, 513),
    "search_input_item": (488, 565),
    "enter_channel_button": (1843, 619),
}


def openSlack():
    print("Opening Slack...")
    gui.hotKey("win", "4")
    
    time.sleep(1)


def start(channels_dict):
    openSlack()

    gui.rightClickSleep( # right clicking at the channels menu
        COORDINATES["channels"][0], # x position
        COORDINATES["channels"][1], # y position
        common.STANDARD_SLEEP_TIME # seconds to wait after having clicked
    )

    gui.pressKey("esc")

    gui.rightClickSleep( # right clicking at the channels menu
        COORDINATES["channels"][0], # x position
        COORDINATES["channels"][1], # y position
        common.STANDARD_SLEEP_TIME # seconds to wait after having clicked
    )

    gui.click( # clicking at the 'manage channels' menu
        COORDINATES["channels_manage"][0], # x position
        COORDINATES["channels_manage"][1], # y position
    )

    gui.clickSleep( # clicking at the 'explore channels' option in menu
        COORDINATES["channels_explore"][0], # x position
        COORDINATES["channels_explore"][1], # y position
        common.STANDARD_SLEEP_TIME # seconds to wait after having clicked
    )

    for category in channels_dict.keys():
        print("------> Searching for channels of {} category <------".format(category))
        for channel_index in range (0, len(channels_dict[category])):
            channel = channels_dict[category][channel_index]
            print("> searching for {} <".format(channel))

            gui.clickSleep( # clicking at the search input
                COORDINATES["search_input"][0], # x position
                COORDINATES["search_input"][1], # y position,
                common.STANDARD_SLEEP_TIME # seconds to wait after having clicked 
            )
            
            gui.hotKey("ctrl", "a") # to select any remaining text in search input
            gui.pressKey("del") # to delete any remaining text in search input
            gui.printlessCountdown(common.STANDARD_SLEEP_TIME)

            # typing the channel name on the search input
            gui.typeSleep(channel, common.STANDARD_SLEEP_TIME*1.5)

            # either hit 'enter' or click at the channel searched. 
            # slack automatically recommends the best match for the input
            # so if there is any other channel with similar name like
            # 'financial' was searched but exists 'financial-result'
            # slack automatically recommends the best match for the searched name
            gui.pressKey("enter")
            gui.printlessCountdown(common.STANDARD_SLEEP_TIME)
            # gui.clickSleep(
            #     COORDINATES["search_input_item"][0], # x position
            #     COORDINATES["search_input_item"][1], # y position
            #     common.STANDARD_SLEEP_TIME/2 # seconds to wait after having clicked 
            # )

            gui.clickSleep( # click 'join channel' button
                COORDINATES["enter_channel_button"][0], # x position
                COORDINATES["enter_channel_button"][1], # y position
                common.STANDARD_SLEEP_TIME # seconds to wait after having clicked
            )
    print("Automation finished. Please just double check if all the channels were entered correctly")
