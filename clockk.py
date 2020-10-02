import turtle

#defining turtle and screen

pen = turtle.Turtle()
sr = turtle.Screen()
a = 10
def pin_1():
    pen.forward(100)
    a = a+10
    pen.forward(100)

def pin_2():
    pen.forward(100)
    a = a - 10
    pen.forward(100)

sr.onkey(pin_1, "Left")
sr.onkey(pin_2, "Right")
input()