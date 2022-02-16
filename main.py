import tkinter as tk
import math

def position(data):
    center_x, center_y, r, distance, angle, angle_speed, x, y = data
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))
    data[6] = x
    data[7] = y
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    return x1, y1, x2, y2

def create_object(data):
    x1, y1, x2, y2 = position(data)
    return canv.create_oval(x1, y1, x2, y2, fill="white")

def move_object(object_id, data):
    x1, y1, x2, y2 = position(data)
    canv.coords(object_id, x1, y1, x2, y2)

def animation():
    second_oval[4] += second_oval[5]
    move_object(e_id, second_oval)
    main.after(move_speed_control, animation)

width = 600
height = 600

move_left_right = 1 #выберите 1 или -1 (1 движение по часовой -1 против часовой), но это может вызвать ошибку в связи
# с количеством ресурсов выделеных под рекурсию, можно выделить дополнительное место с помощью sys.setrecursionlimit(5000)
move_speed_control = 10 #переменная отвечает за скорость движения круга

center_x = width//2
center_y = height//2

first_oval = [center_x, center_y, 200, 0, 0, 0, 0, 0]
second_oval = [center_x, center_y, 20, 200, 0, move_left_right, 0, 0]

main = tk.Tk()
main.title("tkinter")

canv = tk.Canvas(main, width=width, heigh=height, bg="blue")
canv.pack()

create_object(first_oval)
e_id = create_object(second_oval)

animation()
main.mainloop()