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

# Tuple = ()
# Tuples são imutáveis, uma vez iniciadas, não podem ser alteradas.
# Dito isso, podemos facilmente converter uma tuple em lista: list(my_tuple)
# List = []
def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
print(random_rgb())


def moon_walk():
    tib_turt.pensize(7)
    tib_turt.speed(14)
    directions = [0, 90, 180, 270]
    for walk in range(500):
        tib_turt.seth(random.choice(directions))
        tib_turt.pencolor(random_rgb())
        tib_turt.forward(20)

moon_walk()
screen.exitonclick()