import turtle

sr = turtle.Screen()
pen = turtle.Turtle()
sr.setup(500, 500)
pen.speed(100)
pen.hideturtle()
sr.title("Graph")

lcm = 10
width =2
cm = (int(sr.textinput("Input", "Enter how many cm you want [5-25]: ")))

if lcm >= 25:
    lcm = 25

else:
    lcm = lcm


if width >= 12:
    width = 12

else:
    width = width

if cm >= 25:
    cm = 25
else:
    cm = cm

if lcm < 2:
    lcm = 2
else:
    lcm = lcm

if width > 2:
    width = 2
else:
    width = width

if cm < 5 :
    cm = 5
else:
    cm = cm

angle = 0

#onlyone line
def segment(angle, lcm, width, cm):
    for i in range(cm):
        pen.setheading(angle)
        pen.forward(lcm)
        pen.rt(90)
        pen.forward(width)
        pen.bk(width*2)
        pen.forward(width)
        pen.setheading(angle)
#make whole graph
def makegraph():
    segment(angle,lcm,width,cm)
    pen.goto(0, 0)
    segment(angle+90, lcm, width, cm)
    pen.goto(0, 0)
    segment(angle+180, lcm, width, cm)
    pen.goto(0, 0)
    segment(angle+270, lcm, width, cm)
#x and y input
x_variable = (int(sr.textinput("Input", "Enter the value of X: ")))
y_variable = (int(sr.textinput("Input", "Enter The Value of Y: ")))

if x_variable >= 25:
    x_variable = 25
else:
    x_variable = x_variable

if y_variable >= 25:
    y_variable = 25
else :
    y_variable = y_variable

if x_variable <= -25:
    x_variable = -25
else:
    x_variable = x_variable

if y_variable <= -25:
    y_variable = -25
else :
    y_variable = y_variable


tomove_x = (int(x_variable)*lcm)
tomove_y = (int(y_variable)*lcm)

#to mark the points in graph
def x_tomove_1(tomove_x, tomove_y):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(tomove_x, 0)
    pen.setheading(90)
    pen.forward(tomove_y)
    pen.goto(0, tomove_y)
    pen.dot(2)

makegraph()
x_tomove_1(tomove_x, tomove_y)

input()