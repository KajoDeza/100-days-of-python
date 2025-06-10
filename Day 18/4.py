import turtle as t
import random


tim = t.Turtle()

colors = ["CadetBlue4", "DarkOliveGreen4", "DarkGoldenrod2", "brown4", "DarkOrchid", "azure3", "AntiqueWhite2"]
directions = [0, 90, 180, 270]
size = [7, 10, 11]

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
    tim.width(random.choice(size))
    tim.speed("fastest")

