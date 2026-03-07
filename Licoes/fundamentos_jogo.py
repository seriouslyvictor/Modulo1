# Event Listeners
# Basicamente, funcionam do mesmo jeito que JavaScript, espera algo acontecer para disparar uma função.
# No python isso acontece através de Higher Order Functions, ou funções de ordem superior, que essencialmente atribuem uma função como paramêtro para que sejam disparadas quando a Função de ordem superior for invocada.

from turtle import Turtle, Screen

tiburcio = Turtle()
screen = Screen()

def mov_fw():
    tiburcio.forward(10)

def mov_bw():
    tiburcio.back(10)

def rotate(key):
   current_h = tiburcio.heading()
   if key == "a":
        tiburcio.setheading(current_h + 10)
   else:
        tiburcio.setheading(current_h - 10)

screen.listen()
screen.onkeypress(key='c', fun=tiburcio.reset)
screen.onkeypress(key='w', fun=mov_fw)
screen.onkeypress(key='s', fun=mov_bw)
screen.onkeypress(key='a', fun=lambda: rotate('a'))
screen.onkeypress(key='d', fun=lambda: rotate('d'))

screen.exitonclick()