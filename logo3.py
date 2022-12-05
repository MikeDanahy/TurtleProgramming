import turtle

turtle.title('Hi! I\'m Bob the turtle!')
turtle.setup(width=1000, height=1000)

bob = turtle.Turtle(shape='turtle')
bob.speed("fastest")
bob.pencolor("green")
for z in range(4):
    for x in range(4):
        bob.left(90)
        for y in range(4):
            bob.forward(80)
            bob.right(90)
    bob.right(36)
turtle.exitonclick()