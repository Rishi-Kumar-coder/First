import datetime

def gertime():
    return datetime.datetime.now()

foex = (int(input("What you want to add\npress 1 to add food\npress 2 to add Exersise\n:")))

if foex is 1:
    name = input("Who are you\n press 1 for rohan\npress 2 for harry\npress 3 for Rishi\n:")
    if name is 1:
        what = input("What you have ate: ")
        f = open("rohan.txt", "a")
        f.write(gertime(), what )
        f.close()
        print("Written Suseccfull!!!!")

    elif name is 2:
        what = input("What you have ate: ")
        f = open("harry.txt","a")
        f.write(gertime(), what)
        f.close()
        print("Written Suseccfull!!!!")

    elif name is 3:
        what = input("What you have ate: ")
        f = open("rishi.txt", "a")
        f.write(gertime(), what)

        f.close()
        print("Written Suseccfull!!!!")

    else:
        print("Wrong Input!")

elif foex is 2:
    name = input("Who are you\n press 1 for rohan\npress 2 for harry\npress 3 for Rishi\n:")
    if name is 1:
        what = input("What you have done: ")
        f = open("rohan.txt", "a")
        f.write(gertime(), what)

        f.close()
        print("Written Suseccfull!!!!")

    elif name is 2:
        what = input("What you have done: ")
        f = open("harry.txt", "a")
        f.write(gertime(), what)
        f.close()
        print("Written Suseccfull!!!!")

    elif name is 3:
        what = input("What you have done: ")
        f = open("rishi.txt", "a")
        f.write(gertime(), what)
        f.close()
        print("Written Suseccfull!!!!")

    else:
        print("Wrong Input!")


else:
    print("Wrong Input!")

