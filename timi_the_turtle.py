from turtle import Turtle
import random

timi = Turtle()
colours = ["light steel blue", "green yellow", "royal blue",
           "teal", "light slate gray", "slate gray", "cadet blue"]
direction = [0, 90, 180, 270]
timi.pensize(15)


"""def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color"""


# Triangle Turtle
"""def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timi.forward(100)
        timi.right(angle)


for shape_side_n in range(3, 11):
    timi.color(random.choice(colours))
    draw_shape(shape_side_n)"""

# Random walk turtle


for _ in range(200):
    timi.color(random.choice(colours))
    timi.forward(30)
    timi.setheading(random.choice(direction))
