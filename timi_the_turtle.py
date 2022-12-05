from turtle import Turtle
import random

timi = Turtle()
colours = ["light steel blue", "green yellow", "royal blue",
           "teal", "light slate gray", "slate gray", "cadet blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timi.forward(100)
        timi.right(angle)


for shape_side_n in range(3, 11):
    timi.color(random.choice(colours))
    draw_shape(shape_side_n)
