#Jordan Kendall
#2/22/2021
#CSS 225

import turtle
Color=input("What color do you want the turtle to be?")

Lamborghini=turtle.Turtle()
Lamborghini.pencolor(Color)
Lamborghini.fillcolor(Color)
for i in range(4):
    Lamborghini.forward(100)
    Lamborghini.right(90)