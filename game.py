from tkinter import *
import random
import time

#константы
width_of_the_canvas = 800
heiht_of_the_canvas = 500
background_color = 'pink'
width_of_the_input_field = 30
borderwidth_of_the_input_field = 1
rectangle_x_left_corner = 10
rectangle_y_left_corner = 490
rectangle_x_right_corner = 790
rectangle_y_right_corner = 60
rectangle_border_color = 'black'
button_texts = 'Проверить'
common_font = 'Arial 18'

tk = Tk()
tk.title("Just a game 4 fun")

#canvas
canvas = Canvas(tk, width = width_of_the_canvas, height = heiht_of_the_canvas, bg = background_color)
canvas.create_rectangle(rectangle_x_left_corner, rectangle_y_left_corner, rectangle_x_right_corner, rectangle_y_right_corner, outline  = rectangle_border_color,)

#input fields
ent1 = Entry(tk, width = width_of_the_input_field, bd = borderwidth_of_the_input_field)
ent2 = Entry(tk, width = width_of_the_input_field, bd = borderwidth_of_the_input_field)
ent3 = Entry(tk, width = width_of_the_input_field, bd = borderwidth_of_the_input_field)

#buttons
but1 = Button(tk,text = button_texts)
but2 = Button(tk,text = button_texts)
but3 = Button(tk,text = button_texts)

#captions
lab1_first_color = Label(tk, text = "Количество красных шариков:", font = common_font)
lab1_right = Label(tk, text = "Attempts left:", font = common_font)
lab2_second_color = Label(tk, text = "Количество желтых шариков:", font = common_font)
lab2_right = Label(tk, text = "Attempts left:", font = common_font)
lab3_third_color = Label(tk, text = "Количество синих шариков:", font = common_font)
lab3_right = Label(tk, text = "Attempts left:", font = common_font)

#first string(red)
# ent1.grid(row = 0, column = 0, padx = 20)

#packs
lab1_first_color.pack()
lab1_right.pack()
lab2_second_color.pack()
lab2_right.pack()
lab3_third_color.pack()
lab3_right.pack()
but1.pack()
but2.pack()
but3.pack()
ent1.pack()
ent2.pack()
ent3.pack()
canvas.pack()
tk.mainloop()
