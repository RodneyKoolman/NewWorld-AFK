import threading
import time
import random
from tkinter import *
from pynput.keyboard import Key, Controller
from threading import Thread

keyboard_controller = Controller()

def afk():
    while True:
        if stop == 1:
            text["text"] = "Press start and click inside the game once"
            text2["text"] = "Tip: use 'tab' ingame to get your mouse"
            start["state"] = "normal"   
            break
        
        wait_in_seconds = random.randint(5,25)
        text2["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)
        time.sleep(wait_in_seconds)
        
        takeaction(random.choice(['w', 'a', 's', 'd', 0, Key.space]))
        takeaction(random.choice(['q', 'r', 'f', 0]))

def start():
    global stop
    global current_thread
    stop = 0
    text["text"] = "AFK mode running..."
    start["state"] = "disabled"
   
    current_thread = Thread (target = afk)
    current_thread.start()

def stop():
    global stop
    stop = 1
    text["text"] = "Stopping, please wait..."
    text2["text"] = "Waiting for current actions to complete"

def takeaction(givekey):
    if(givekey == 0):
        text2["text"] = "Current action: performing no key presses"
        time.sleep(random.randint(1,3))
    else: 
        text2["text"] = "Current action: pressing {}".format(givekey)
        keyboard_controller.press(givekey)
        time.sleep(random.randint(1,3))
        keyboard_controller.release(givekey)

root = Tk()
root.title("New World - AFK")
root.geometry('300x100+50+50')
root.resizable(False, False)
root.attributes('-topmost', 1)

frameTop = Frame(root)
frameTop.pack()

frameMiddle = Frame(root)
frameMiddle.pack()

frameBottom = Frame(root)
frameBottom.pack()

text = Label(frameTop, text="Press start and click inside the game once", font=('Helvetica', '9', 'bold'))
text.pack(side=LEFT, pady=5)

text2 = Label(frameMiddle, text="Tip: use 'tab' ingame to get your mouse", font=('Helvetica', '9', 'italic'))
text2.pack(side=LEFT)

start = Button(frameBottom, text='Start', fg='green', font=('Helvetica', '12', 'bold'), command=start)
start.pack(side=LEFT, pady=5, padx=8)

stop = Button(frameBottom, text='Stop', fg='red', font=('Helvetica', '12', 'bold'), command=stop)
stop.pack(side=RIGHT, pady=5, padx=8)

root.mainloop()