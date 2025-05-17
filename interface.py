import turtle

# Create a screen
screen = turtle.Screen()
screen.title("My First Turtle Program")
screen.setup(width=800, height=600)  # Set the window size
screen.bgcolor("lightblue")  # Set background color

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")  # Options: "arrow", "turtle", "circle", "square", "triangle", "classic"
t.color("green")
t.pensize(3)

# Basic movement commands
t.forward(100)  # Move forward 100 pixels
t.left(90)      # Turn left 90 degrees
t.forward(100)
t.right(90)     # Turn right 90 degrees
t.backward(50)  # Move backward 50 pixels

# Pen control
t.penup()       # Stop drawing while moving
t.goto(100, 50) # Move to x=100, y=50
t.pendown()     # Resume drawing while moving

def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(360 // 4)

def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(360 // 3)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.left(360 // 5)


draw_square(50)
draw_triangle(100)
draw_star(100)

t = turtle.Turtle()
t.speed(0)  # 0=fastest, 1=slowest, 10=fast

# Drawing with fill
t.fillcolor("red")
t.begin_fill()
draw_square(100)  # Using our previously defined function
t.end_fill()

# Random colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.penup()
t.goto(-200, 0)
t.pendown()

for color in colors:
    t.color(color)
    t.forward(50)
    t.left(60)
# Keep the window open until clicked
screen.exitonclick()