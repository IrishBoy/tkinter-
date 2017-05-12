from tkinter import *
import random 
import time

#константы
width_of_the_canvas = 800
heiht_of_the_canvas = 500
background_color = 'pink'


tk = Tk()
tk.title("Just a game 4 fun")
canvas = Canvas(tk, width = width_of_the_canvas, height = heiht_of_the_canvas, bg = background_color)
canvas.pack()
tk.update()
tk.mainloop()
