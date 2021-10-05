import os, time, random, pydirectinput
from threading import Thread
from tkinter import *

def start():
    start_button["state"] = "disabled"
    info_label["text"] = "AFK mode running..."

    thread = Thread (name="afk", target=afk)
    thread.start()

def exit():
    exit_button["state"] = "disabled"
    start_button["state"] = "disabled"

    #TODO: Gracefully stop thread
    os._exit(0)

def action(key):
    if(key == 0):
        tooltip_label["text"] = "Current action: no or mouse only movement"
        if(random.randint(0,1) > 0):
            mouse_direction_lr = random.randint(-30,30)
            mouse_direction_ud = random.randint(-5,5)
            pydirectinput.moveRel(mouse_direction_lr, mouse_direction_ud, relative=True)
    elif (key == 'tab'):
        pydirectinput.press(key)
        wait_in_seconds = random.randint(25,300)
        tooltip_label["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)
        time.sleep(wait_in_seconds)
        pydirectinput.press(key)
    else:
        if(random.randint(0,1) > 0):
            mouse_direction_lr = random.randint(-30,30)
            mouse_direction_ud = random.randint(-5,5)
            pydirectinput.moveRel(mouse_direction_lr, mouse_direction_ud, relative=True)
        pydirectinput.keyDown(key)
        wait_in_seconds = round(random.uniform(0.2, 1.5), 1)
        tooltip_label["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)
        time.sleep(wait_in_seconds)
        pydirectinput.keyUp(key)

def afk():
    while True:        
        wait_in_seconds = random.randint(60,300)
        tooltip_label["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)
        time.sleep(wait_in_seconds)

        movement_list = ['w', 'a', 's', 'd', 'space', 'tab', 0]
        random.shuffle(movement_list)
        for key in movement_list:
            tooltip_label["text"] = "Current action: pressing {}".format(key)
            action(key)
            wait_in_seconds = random.randint(1,6)
            tooltip_label["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)
            time.sleep(wait_in_seconds)

root = Tk()
root.title("New World - AFK")
root.geometry('300x100+50+50')
root.resizable(False, False)
root.attributes('-topmost', 1)

frame_top = Frame(root)
frame_top.pack()

frame_middle = Frame(root)
frame_middle.pack()

frame_bottom = Frame(root)
frame_bottom.pack()

info_label = Label(frame_top, text="Press start and click inside the game once", font=('Helvetica', '9', 'bold'))
info_label.pack(side=LEFT, pady=5)

tooltip_label = Label(frame_middle, text="Tip: use 'tab' in-game to get your mouse pointer", font=('Helvetica', '9', 'italic'))
tooltip_label.pack(side=LEFT)

start_button = Button(frame_bottom, text='Start AFK', fg='green', font=('Helvetica', '12', 'bold'), command=start)
start_button.pack(side=LEFT, pady=5, padx=8)

exit_button = Button(frame_bottom, text='Exit', fg='red', font=('Helvetica', '12', 'bold'), command=exit)
exit_button.pack(side=RIGHT, pady=5, padx=8)

root.mainloop()