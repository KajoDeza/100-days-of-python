# from turtle import *

import turtle as t

tim = t.Turtle()

t.shape("arrow")
t.color("purple")

for _ in range(6):

    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

