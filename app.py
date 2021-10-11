import os, time, random, pydirectinput
from threading import Thread
from tkinter import *

def start():
    start_button["state"] = "disabled"
    info_label["text"] = "AFK mode active"
    info_label["fg"] = "green"

    thread_control = Thread (name="control", target=control)
    thread_timer = Thread (name="timer", target=timer)
    
    thread_control.start()
    thread_timer.start()

def exit():
    exit_button["state"] = "disabled"
    start_button["state"] = "disabled"

    #TODO: Gracefully stop thread
    os._exit(0)

def wait(range_start, range_stop):
    wait_in_seconds = round(random.uniform(range_start, range_stop), 1)
    while wait_in_seconds > 0:
        wait_in_seconds = round(wait_in_seconds-0.1, 1)
        time.sleep(0.1)
        tooltip_label["text"] = "Current action: waiting {} seconds".format(wait_in_seconds)

def mouse(range_lr_start, range_lr_stop, range_ud_start, range_ud_stop):
    if(random.randint(0,1) > 0):
        mouse_direction_lr = random.randint(range_lr_start, range_lr_stop)
        mouse_direction_ud = random.randint(range_ud_start, range_ud_stop)
        pydirectinput.moveRel(mouse_direction_lr, mouse_direction_ud, relative=True)

def timer():
    time_start = time.time()
    seconds = 0
    minutes = 0
    hours = 0

    while True:
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
        if minutes >= 60:
            hours += 1
            minutes = 0
        start_button["text"] = "AFK time: {}:{}:{}".format(hours, minutes, seconds)

def action(key):
    if(key == 0):
        mouse(-30, 30, -5, 5)
    elif (key == 'tab'):
        pydirectinput.press(key)
        wait(25.0,300.0)
        pydirectinput.press(key)
    else:
        mouse(-30, 30, -5, 5)
        pydirectinput.keyDown(key)
        wait(0.2, 1.2)
        pydirectinput.keyUp(key)

def control():
    while True:        
        wait(60.0, 300.0)
        movement_list = ['w', 'a', 's', 'd', 'space', 'tab', 0]
        random.shuffle(movement_list)

        for key in movement_list:
            tooltip_label["text"] = "Current action: pressing {}".format(key)
            action(key)
            wait(0.5, 5.0)

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

start_button = Button(frame_bottom, text='Start', fg='green', font=('Helvetica', '9', 'bold'), command=start)
start_button.pack(side=LEFT, pady=5, padx=8)

exit_button = Button(frame_bottom, text='Exit', fg='red', font=('Helvetica', '9', 'bold'), command=exit)
exit_button.pack(side=RIGHT, pady=5, padx=8)

root.mainloop()