from turtle import Turtle, Screen, colormode
import turtle as t
import random

screen = t.Screen()
screen.setup(width=800, height=600)  # Set the window size
colormode(255)
tib_turt = Turtle()
tib_turt.shape("turtle")
tib_turt.color("red")
tib_turt.pencolor("black")

def overlayed_shapes():
    full_circle = 360
    colors = ["aquamarine1", "cadetblue4", "darkgoldenrod3", "darkslategray", "hotpink4", "lightsalmon3"]

    for shape in range(3,11):
        tib_turt.pencolor(random.choice(colors))
        for sides in range(shape):
            tib_turt.forward(100)
            tib_turt.right(full_circle // shape)
        tib_turt.home()
    
overlayed_shapes()
screen.exitonclick()