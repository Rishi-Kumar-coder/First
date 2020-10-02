import turtle

pen = turtle.Turtle()
sr = turtle.Screen()

a = (int(sr.textinput("Angle's", "Enter The Angle: ")))

pen.forward(150)
pen.stamp()
pen.goto(0, 0)
pen.setheading(0)
pen.left(a)
pen.write(a)
pen.forward(150)
pen.stamp()

input()