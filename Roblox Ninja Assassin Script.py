#Import Libraries (mouse and keyboard control as well as the sleep function)
import keyboard

import mouse

from time import sleep
def startMainLoop():
    dookie=False
    LoopTimesCounter = 0
    print("Starting in 5...")
    sleep(1)
    print("Starting in 4...")
    sleep(1)
    print("Starting in 3...")
    sleep(1)
    print("Starting in 2...")
    sleep(1)
    print("Starting in 1...")
    sleep(1)
    print("Starting...")
    while dookie == False:  #Loop clicking and anti-afk
        mouse.click()
        keyboard.press("w")
        sleep(0.1)
        keyboard.release("w")
        mouse.click()
        keyboard.press("s")
        sleep(0.1)
        keyboard.release("s")
        LoopTimesCounter = LoopTimesCounter+1#counter in case of lvl up
        if LoopTimesCounter==30:
            keyboard.press("1")
            sleep(0.05)
            keyboard.release("1")
            LoopTimesCounter=0
        try:    #Attemps the following yet shows no errors if failed
            if keyboard.is_pressed('0'):    #end loop script
                print("ended loop")
                dookie=True

        except:
            dookie=False
    sleep(10)
    exit()
def MainScriptFunct():
    startinput = input("If ready type 'start' [type 'end' to end]:  ")
    if startinput == "start":
        startMainLoop()
    else:
        if startinput=="end":
            exit()
        else:
            print("retry:")
            MainScriptFunct()
MainScriptFunct()

#//////////////////////////////////////////////////////////////////////////////////////
#                    Made by Hayden with help from Lucas!