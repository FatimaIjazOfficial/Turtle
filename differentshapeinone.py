import random
import turtle as t

tim = t.Turtle()
colours = ["SkyBlue", "purple", "red", "pink", "yellow", "SeaGreen", "wheat", "grey", "black"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(side)
