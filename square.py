import turtle
from turtle import Screen, Turtle

turtle = Turtle()


def square(length):
    "have the turtle draw a square of side <lenght>"
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)
        print(side)
turtle.reset()

square(200)
