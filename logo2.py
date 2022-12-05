import turtle
import math

turtle.title('Hi! I\'m Bob the turtle!')
turtle.setup(width=1000, height=1000)

bob = turtle.Turtle(shape='turtle')


bob.speed("slowest")

for x in range(4):
    bob.left(90)
    bob.forward(80)
    bob.right(90)
    bob.forward(80)
    bob.right(90)
    bob.forward(80)
    bob.right(90)
    bob.forward(80)
    bob.right(90)
turtle.exitonclick()