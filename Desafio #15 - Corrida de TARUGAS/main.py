from turtle import Turtle, Screen
import random as rand

screen = Screen()
all_colors = ["red", "yellow", "green", "purple", "blue", "black"]

def game_setup():
    screen.setup(width=500, height=400)
    screen.textinput(title="Bem Vindo!", prompt="Bem vindo à corrida de tarugas, escolha uma cor e reze para o sucesso da sua taruga! \nDigite qualquer coisa pra prosseguir...")
    bet365 = screen.textinput(title="Escolha seu campeão!", prompt=f"Digite uma cor para representar sua taruga \nAs cores permitidas são: {all_colors}").lower().strip()
    return bet365

def create_turtles(num):
    turtles = []
    for index in range(num):
        new_turtle =  Turtle(shape="turtle")
        new_turtle.color(all_colors[index])
        new_turtle.penup()
        turtles.append(new_turtle)
    print(turtles)
    for index, turtle in enumerate(turtles):
        ycoords = [-160, -100, -40, 20, 80, 140]
        turtle.goto(-230, ycoords[index])
    return turtles

bet365 = game_setup()
racers = create_turtles(6)

racing = False
if bet365:
    racing = True

while racing:
    finish_line = (250 - (40//2))
    for racer in racers:
        if racer.xcor() >= finish_line:
            print(f"The {racer.pencolor().capitalize()} turtle won the race!")
            racer.speed(2)
            racer.setheading(180)
            racer.goto(0,0)
            racer.write("😚😚😙!", move=True, align="center", font=('Arial', 22, 'normal'))
            if bet365 == racer.pencolor():
                print("You won!")
            else:
                print("You lost...")
            racing = False
        steps = rand.randint(1,10)
        racer.forward(steps)

screen.exitonclick()