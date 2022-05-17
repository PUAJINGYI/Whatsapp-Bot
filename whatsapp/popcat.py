import pyautogui as pt
from time import sleep

sleep(3)

position1 = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/popcat.png", confidence=.6)


# Click bot
def autoClick():
    #global x, y

    position = pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/popcat.png", confidence=.6)
#   x=position[0]
#   y=position[1]
    pt.tripleClick()
    pt.tripleClick()
    pt.tripleClick()
    pt.click

while True:
    autoClick()

    if pt.locateOnScreen("C:/Users/Asus User/PycharmProjects/whatsapp_bot/whatsapp/exit.png", confidence=.6)==True:
        break
