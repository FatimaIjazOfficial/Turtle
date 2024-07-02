from turtle import Turtle, Screen
tim_turtle = Turtle()  # class
tim_turtle.shape("turtle")  # turtle
tim_turtle.color("Black")  # colors

# Dashed Line
for t in range(15):
    tim_turtle.forward(5)  # right side steps
    tim_turtle.penup()
    tim_turtle.forward(5)
    tim_turtle.pendown()


# Calling a screen from Screen class
screen = Screen()
screen.exitonclick()