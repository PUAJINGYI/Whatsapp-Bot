import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]


# Gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 60, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 25)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: "+whatsapp_message)

    return whatsapp_message

# posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/smiley_paperclip.png",
                                 confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval=.01)


# processes response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    else:
        if random_no == 0:
            return "ok"
        elif random_no == 1:
            return "okk"
        else:
            return "哦哦"

# Check for new message
def check_for_new_message():
    pt.moveTo(x+55, y-25, duration=.5)

    while True:      #Continuously checks for green dot and new messages
        try:
            position = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/green_circle.png", confidence=.9)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new message")

        if pt.pixelMatchesColor(int(x+55), int(y-25), (255,255,255),tolerance=10):
            print("is_white")
            processed_message = process_response(get_message())
            post_response(processed_message)

        else:
            print("No new message yet...")
        sleep(5)

check_for_new_message()


