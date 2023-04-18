import time, re
from utils import gui, common


COORDINATES = {
    "search_input": (879, 21),
    "channels_menu_tab": (564, 111),
    "only_my_channels": (803, 165),
    "first_channel": (396, 256),
    "members": (1873, 65),
    "add_people": (717, 356),
    "emails_input": (857, 489),
    "from_another_organization": (815, 556),
    "from_another_organization_next": (1198, 750),
    "only_post": (691, 628),
    "only_post_next": (1198, 683),
    "notes": (829, 544),
    "notes_send_invitation": (1198, 703)
}


def openSlack():
    print("Opening Slack...")
    gui.hotKey("win", "4")
    
    time.sleep(common.STANDARD_SLEEP_TIME * 2)


def checkIfNeedsRepetition(emailList):
    # if the e-mail provider is not one in your workspaces 
    # e.g "@milezero.com", "@capstonelogistics.com" and "@lean-tech.io"
    # and if one of those were added to the e-mails list for the channel
    # that the script is currently working on, it means that the script
    # must confirm "From other organization" and "Only Post" twice. This
    # is how slack works 🤷🏻‍♂️
    other_providers = []
    common_providers = [
        "@milezero.com",
        "@capstonelogistics.com",
        "@lean-tech.io"
    ]
    common_providers_count = 0

    for email in emailList:
        email_provider = re.search("@[a-zA-Z0-9_.-]+.[a-zA-Z]{2,}", email).group()
        if email_provider in common_providers:
            common_providers_count += 1
        elif email_provider not in other_providers:
            other_providers.append(email_provider)

    return len(other_providers) > 0 and common_providers_count > 0
            

def start(channels_dict):
    openSlack()

    for channel in channels_dict.keys():
        emails = channels_dict[channel]
        
        common.cprint(
            "E-Mails for channel {}: ".format(channel),
            "light_blue"            
        )
        for email in emails:
            print("-> {}".format(email))

        # click search input 2x to make sure it was clicked
        for i in range (0, 2):
            gui.clickSleep(
                COORDINATES["search_input"][0], # x
                COORDINATES["search_input"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
        # select and delete all text in the search field
        gui.hotKey("ctrl", "a")
        gui.pressKey("del")
        # type channel name on search input
        gui.typeSleep(
            channel, # channel name
            common.STANDARD_SLEEP_TIME * 1 # 1s
        )
        # press enter to search for it
        gui.pressKeySleep(
            "enter",
            common.STANDARD_SLEEP_TIME
        )
        # click "Channels" category
        gui.clickSleep(
            COORDINATES["channels_menu_tab"][0], # x
            COORDINATES["channels_menu_tab"][1], # y
            common.STANDARD_SLEEP_TIME * 1 # 1s
        )
        # open channel
        gui.clickSleep(
            COORDINATES["first_channel"][0], # x 
            COORDINATES["first_channel"][1], # y
            common.STANDARD_SLEEP_TIME * 2 # 2s
        )
        # click members button
        gui.clickSleep(
            COORDINATES["members"][0], # x
            COORDINATES["members"][1], # y
            common.STANDARD_SLEEP_TIME * 1 # 1s
        )
        # click add people
        gui.clickSleep(
            COORDINATES["add_people"][0], # x
            COORDINATES["add_people"][1], # y
            common.STANDARD_SLEEP_TIME # 1s
        )
        # click the e-mails input 2x to make sure it was clicked
        for i in range (0, 2):
            gui.clickSleep(
                COORDINATES["emails_input"][0], # x
                COORDINATES["emails_input"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
        for email in emails:
            # type e-mail to add to the channel
            gui.typeSleep(
                email,
                common.STANDARD_SLEEP_TIME * 1 # 1s
            )
            # press enter
            gui.pressKeySleep(
                "enter", 
                common.STANDARD_SLEEP_TIME # 1s
            )
        # press enter to go to next section
        gui.pressKeySleep(
            "enter", 
            common.STANDARD_SLEEP_TIME # 1s
        )
        # steps bellow can repeat up to 2 times 👇🏻 (if the e-mail provider is not one in your workspaces e.g "@milezero.com", "@capstonelogistics.com" and "@lean-tech.io")
        repeats = 1
        if checkIfNeedsRepetition(emails):
            repeats = 2
        for i in range (0, repeats):
            # click "From another organization"
            gui.clickSleep(
                COORDINATES["from_another_organization"][0], # x
                COORDINATES["from_another_organization"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            # click "Next"
            gui.clickSleep(
                COORDINATES["from_another_organization_next"][0], # x
                COORDINATES["from_another_organization_next"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            # click "Got it" (same position as Next)
            gui.clickSleep(
                COORDINATES["from_another_organization_next"][0], # x
                COORDINATES["from_another_organization_next"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            # click "Only post"
            gui.clickSleep(
                COORDINATES["only_post"][0], # x
                COORDINATES["only_post"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            # click "Next"
            gui.clickSleep(
                COORDINATES["only_post_next"][0], # x
                COORDINATES["only_post_next"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            # type "Requested by dispatcher" on Note text field
            gui.clickSleep(
                COORDINATES["notes"][0], # x
                COORDINATES["notes"][1], # y
                common.STANDARD_SLEEP_TIME # 1s
            )
            gui.hotKey("ctrl", "a")
            gui.pressKey("del")
            gui.typeSleep(
                "Requested by dispatcher", # note message
                common.STANDARD_SLEEP_TIME * 1 # 1s
            )
            # click "Send invitations"/"Next" (changes accordingly to the position of the user on the list)
            gui.clickSleep(
                COORDINATES["notes_send_invitation"][0], # x
                COORDINATES["notes_send_invitation"][1], # y
                common.STANDARD_SLEEP_TIME * 1 # 1s
            )
        # click Done or press enter
        gui.pressKeySleep(
            "enter",
            common.STANDARD_SLEEP_TIME * 1 # 1s
        )
        # Close add member modal by clicking out of it
        gui.clickSleep(
            COORDINATES["members"][0], # x
            COORDINATES["members"][1], # y
            common.STANDARD_SLEEP_TIME # 1s
        )
    common.cprint("AUTOMATION FINISHED!", "light_red", attrs=["bold"])
    print()
    print("Please just double check if all users were invited by accessing")
    common.cprint("More > Slack Connect > View Invitations", "light_green", attrs=["bold"])
