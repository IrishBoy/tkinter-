from tkinter import *
import random 
import time

tk = Tk()
win_width = 360
win_height = 380
config_string = "{0}x{1}".format(win_width, win_height + 32)
tk.title("Just a game 4 fun")
canvas = Canvas(tk, width=550, height=400, bd=5, highlightthickness=0)
canvas.pack()
tk.update()

