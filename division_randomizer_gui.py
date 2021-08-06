import tkinter
from tkinter import *
import random

frame = tkinter.Tk()
frame.title("Division Randomizer")
frame.geometry('400x200')
label1 = tkinter.Label(
    text="Welcome to the division randomizer!",
    fg = "black",
    bg = "white",
)
label1.pack()

label2 = tkinter.Label(
    text="A shitty little tool that you really don't need to randomize a group of names.",
    fg = "black",
    bg = "white",
)
label2.pack()

#create textbox(es)
player_labels = [Label(frame, text='Player1: '), Label(frame, text='Player2: '), Label(frame, text='Player3: '), Label(frame, text='Player4: '), Label(frame, text='Player5: '), Label(frame, text='Player6: '), Label(frame, text='Player7: '), Label(frame, text='Player8: '), Label(frame, text='Player9: '), Label(frame, text='Player10: ')]
player_entries = [Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame), Entry(frame)]

for label, entry in zip(player_labels, player_entries):
    label.pack()
    entry.pack()

input_list = []
def randomize_names():
    input_list = [entry.get() for entry in player_entries]
    random.shuffle(input_list)
    input_list1 = input_list[:len(input_list)//2]
    input_list2 = input_list[len(input_list)//2:]
    lbl1.config(text=" ".join(input_list1))
    lbl2.config(text=" ".join(input_list2))

btn1 = tkinter.Button(frame, text="Randomize!", command = randomize_names).pack()
lbl1 = tkinter.Label(frame, text ="Here's your randomized list: ".join(input_list))
lbl2 = tkinter.Label(frame, text ="Here's your randomized list: ".join(input_list))
lbl1.pack()
lbl2.pack()


frame.mainloop()
