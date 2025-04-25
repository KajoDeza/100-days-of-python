import turtle
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")

my_screen = Screen()
timmy.color("coral")
timmy.speed(3)

while True:
    timmy.forward(100)
    timmy.left(180)
    timmy.forward(200)

    print(my_screen.canvheight)
    turtle.exitonclick()
