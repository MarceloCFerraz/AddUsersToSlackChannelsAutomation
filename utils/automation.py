import time
from utils import gui
from utils.image import text, image, limiarization


COORDINATES = {
    "search_input": (531, 26),
    "search_input_item": (446, 210, 1480, 331),
    "enter_channel_button": (1190, 950),
}


def openSlack():
    print("Opening Slack...")
    gui.hotKey("win", "4")


def start(channels_dict):
    time.sleep(1)
    openSlack()

    standard_sleep = 2


    for category in channels_dict.keys():
        # print("\n\n{} ({} items): ".format(category, len(channels_dict[category])), end=" ")
        for channel_index in range (0, len(channels_dict[category])):
            channel = channels_dict[category][channel_index]

            gui.clickSleep( # clicking at the search bar
                COORDINATES["search_input"][0], # x position
                COORDINATES["search_input"][1], # y position
                standard_sleep # seconds to wait after having clicked
            )

            gui.hotKey("ctrl", "a") # to select any text on the search bar
            gui.pressKeySleep("del", standard_sleep) # to delete any text on the search bar

            gui.typeSleep(channel, standard_sleep) # type the channel name at the search bar

            search_print = image.imgToGray(
                image.printScreen(
                    COORDINATES["search_input_item"][0],
                    COORDINATES["search_input_item"][1],
                    COORDINATES["search_input_item"][2],
                    COORDINATES["search_input_item"][3],
                )
            )

            search_print = limiarization.basic(search_print)

            # image.showImage(search_print)
            
            x, y, w, h, search_print, found = text.findTextOnImg(
                text.extractDict(search_print),
                search_print,
                channel
            )

            if x != None and y != None and w != None and h != None:
                gui.clickSleep( # clicking at channel searched
                    446 + x + (w / 2), # x position
                    210 + y + (h / 2), # y position
                    standard_sleep # seconds to wait after having clicked
                )

                gui.clickSleep( # clicking at the "Enter Channel" button
                    COORDINATES["enter_channel_button"][0], # x position
                    COORDINATES["enter_channel_button"][1], # y position
                    standard_sleep # seconds to wait after having clicked
                )
            else:
                print("Couldn't find the channel on that image")

