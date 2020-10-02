import turtle

pen = turtle.Turtle()
sr = turtle.Screen()

ans = (int(sr.textinput("Free Fire Diamond Price Converter.", "Choice one: \n To Convert Diamond in ₹ ----1\nTo convert ₹ into diamond-----2\n")))

if ans == 1:
    dia = (int(sr.textinput("Diamonds to ₹ Converter.", "Enter Amount of Diamonds: ")))
    price = dia/1.25
    sr.textinput("Diamonds to ₹ Converter.", price)

elif ans == 2:
    money = (int(sr.textinput("To convert ₹ in diamond", "Enter The Amount Of ₹ : ")))
    price = money * 1.25
    sr.textinput("To convert ₹ in diamond", price)

retry = sr.textinput("Free Fire Diamond Price Converter.", "Choice one: \n Retry -----1\nExit ------2\n")

if retry == 2:
    exit()
    



