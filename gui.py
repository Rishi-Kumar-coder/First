import tkinter

r = tkinter.Tk()
def print():
    w = tkinter.Label(r, text = "hello")
    w.pack()
button = tkinter.Button(r, text = "Enter",command = print() )
button.pack()

r.mainloop()



