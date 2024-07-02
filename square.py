from turtle import Turtle, Screen

tim_turtle = Turtle()  # class
tim_turtle.shape("turtle")  # turtle
tim_turtle.color("red")  # colors

# Square
tim_turtle.forward(100)  # right side steps
tim_turtle.right(90)  # Direction change
tim_turtle.forward(100)
tim_turtle.right(90)
tim_turtle.forward(100)
tim_turtle.right(90)
tim_turtle.forward(100)


# Calling a screen from Screen class
screen = Screen()
screen.exitonclick()
