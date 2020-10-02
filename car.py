import turtle
sr = turtle.Screen()

myfile = open("text", "w")

un = sr.textinput("Email", "Enter Your New User Name\n Or press 5 If you have account")
myfile.write(un)
ps = sr.textinput("Email", "Enter Your Password: ")
myfile.write(ps)
ac = sr.textinput("Email", "You have created Your Account.\nEnter 1 to continue.")

if ac != 1:
    sr.textinput("Email", "Wrong input")

else:
    un2 = sr.textinput("Emain login.", "Enter Your Username: ")
    if un2 != un:
            sr.textinput("Login Failed!!!", "Wrong Username.")
            sr.resetscreen()
    else:
            ps2 = sr.textinput("Email Login", "Enter Your Password: ")

            if ps2 != ps:
                sr.textinput("Login faild...", "Wrong password!!!")
                sr.resetscreen()

            else:
                sr.textinput("Login succecfull!!!", "Login succesfull!!! ")