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

def make_spirogram(radius, angle):
    tib_turt.speed(0)
    num_passes = 360 // angle
    for a_pass in range(num_passes):
        print(a_pass)
        tib_turt.setheading(a_pass * angle)
        tib_turt.pencolor(random_rgb())
        tib_turt.circle(radius)
        
    
make_spirogram(100,20)
screen.exitonclick()