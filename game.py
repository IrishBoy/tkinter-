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


def movements(number):
	canvas.move('circle' + str(number))
#start circles
def create(number):
	for i in range (number):
		r = random.randint(5, 30)
		x_start = random.randint(40, 730)
		y_start = random.randint(150,420)
		canvas.create_oval([x_start, y_start],[x_start + 2 * r,y_start + 2 * r],fill = 'black', outline = 'green',tag = 'circle' + str(i))

#checking
def check(event):
	click = event.widget
	if click == but1:
		right_ans = red_circles
		attempt = int(ent1.get())
		if attempt == right_ans :
			canvas.create_line(750,10,750,40, width = 3, fill = 'green')
			canvas.create_line(735,25,765,25, width = 3, fill = 'green')
		else:
			canvas.create_line(735,25,765,25, width = 3, fill = 'red')
	elif click == but2:
		right_ans = yellow_circles
		attempt = int(ent2.get())
		if attempt == right_ans :
			canvas.create_line(750,50,750,80, width = 3, fill = 'green')
			canvas.create_line(735,65,765,65, width = 3, fill = 'green')
		else:
			canvas.create_line(735,65,765,65, width = 3, fill = 'red')
	else:
		right_ans = blue_circles
		attempt = int(ent3.get())
		if attempt == right_ans :
			canvas.create_line(750,90,750,120, width = 3, fill = 'green')
			canvas.create_line(735,105,765,105, width = 3, fill = 'green')
		else:
			canvas.create_line(735,105,765,105, width = 3, fill = 'red')

tk = Tk()
tk.title("Just a game 4 fun")

#canvas
canvas = Canvas(tk, width = width_of_the_canvas, height = heiht_of_the_canvas, bg = background_color)
canvas.create_rectangle(rectangle_x_left_corner, rectangle_y_left_corner, rectangle_x_right_corner, rectangle_y_right_corner, outline  = rectangle_border_color)


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

# random number circles
all_circles = random.randint(0, 50)
red_circles = random.randint(0, all_circles)
yellow_circles = random.randint(0, (all_circles - red_circles))
blue_circles =  random.randint(0, (all_circles - red_circles - yellow_circles))

#bind
but1.bind("<Button-1>", check)
but2.bind("<Button-1>", check)
but3.bind("<Button-1>", check)

#creating
create(all_circles)

#repainting
tags = []
for i in range(all_circles):
	tags.append(i)
for i in range(0,red_circles):
	canvas.itemconfig('circle' + str(i), fill = 'red')
for i in range(red_circles,(red_circles + blue_circles)):
	canvas.itemconfig('circle' + str(i), fill = 'blue')
for i in range((red_circles + blue_circles), len(tags)):
	canvas.itemconfig('circle' + str(i), fill = 'yellow')


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
