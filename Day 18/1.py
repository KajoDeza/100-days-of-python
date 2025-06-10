from turtle import Turtle , Screen

tom = Turtle()
mark = Turtle()

mark.shape("arrow")
mark.color("green")

for _ in range(4):
    mark.forward(80)
    mark.left(90)

tom.shape("arrow")
tom.color("blue")

for _ in range(4):

    tom.forward(80)
    tom.right(90)






screen = Screen()
screen.exitonclick()