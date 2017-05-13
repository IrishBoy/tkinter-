from tkinter import *
import random
import time

#константы
width_of_the_canvas = 800
heiht_of_the_canvas = 500
background_color = 'pink'
width_of_the_input_field = 30
borderwidth_of_the_input_field = 3
rectangle_x_left_corner = 10
rectangle_y_left_corner = 490
rectangle_x_right_corner = 790
rectangle_y_right_corner = 120
rectangle_border_color = 'black'
button_texts = 'Проверить'
common_font = 'Arial 14'
lab_left_x_place = 10
lab_right_x_place = 600
ent_x_place = 300
but_x_place = 600
str1_y_place = 10
str2_y_place = 50
str3_y_place = 90

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
but1 = Button(tk,text = button_texts, height = 1)
but2 = Button(tk,text = button_texts)
but3 = Button(tk,text = button_texts)

#captions
lab1_first_color = Label(tk, text = "Количество красных шариков:", font = common_font, bg = background_color)
lab2_second_color = Label(tk, text = "Количество желтых шариков:", font = common_font, bg = background_color)
lab3_third_color = Label(tk, text = "Количество синих шариков:", font = common_font, bg = background_color)



#packs and places
lab1_first_color.place(x = lab_left_x_place, y = str1_y_place)
lab2_second_color.place(x = lab_left_x_place, y = str2_y_place)
lab3_third_color.place(x = lab_left_x_place, y = str3_y_place)
but1.place( x = but_x_place, y = str1_y_place)
but2.place( x = but_x_place, y = str2_y_place)
but3.place( x = but_x_place, y = str3_y_place)
ent1.place( x = ent_x_place, y = str1_y_place)
ent2.place( x = ent_x_place, y = str2_y_place)
ent3.place( x = ent_x_place, y = str3_y_place)
canvas.pack()
tk.mainloop()
