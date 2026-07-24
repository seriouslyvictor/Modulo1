import turtle, time, random

# Set up screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) 

# Lista com a cabeça mais o corpo da cobra
segments = []

# "Comida"
comida = turtle.Turtle()
comida.shape('circle')
comida.color('blue')
comida.penup()
def flicker():
    if comida.color()[0] == "blue":
        comida.color("black")
    else:
        comida.color("blue")
    screen.ontimer(flicker, 500)
flicker()

def mover_comida():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    comida.teleport(x,y)

# Cabeça da Cobra
head = turtle.Turtle(shape="square")
head.color("green")
head.penup()
segments.append(head)

#Corpo da Cobra
def criar_segmento():
    if len(segments) <= 0:
        last_pos = (0,0)
    else:
        last_pos = segments[-1].pos()
    segment = turtle.Turtle(shape="square")
    segment.color("yellow")
    segment.penup()
    segment.goto(last_pos)
    segments.append(segment)

for i in range(2):
    criar_segmento()

# Movimenta o corpo em relação à cabeça
def mover():
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    head.forward(20)

def move_up():
    head.setheading(90)
def move_left():
    head.setheading(180)
def move_down():
    head.setheading(270)
def move_right():
    head.setheading(0)

def atualizar():
    scoreboard.clear()
    scoreboard.write(f"Scoreboard: {score}", move=False, align='center', font=("Fixedsys", 20 , 'normal'))
# Scoreboard
score = 0
scoreboard = turtle.Turtle(visible=False)
scoreboard.penup()
scoreboard.color("white")
scoreboard.goto(0, 270)
atualizar()


screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")

game_running = True
mover_comida()
while game_running:
    time.sleep(0.1)
    mover()
    screen.update()
    # Colisão com o corpo
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            print("Game Over: Bati em mim mesmo!")
            game_running = False
            break
    # Colisão com a comida
    if head.distance(comida) <= 18:
        print("Nhom Nhom Nhom!!!")
        score += 1
        criar_segmento()
        mover_comida()
        atualizar()
    #Colisão com a 'parede'
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        print("Bati na parede!")
        game_running = False
        break


screen.mainloop()