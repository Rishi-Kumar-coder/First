a = (int(input("enter a number: ")))


if a <= 10:
    for i in range(a):
        z = '*'
        print(z*(i+1))

else:
    for i in range(a):
        z = '*'
        print(z*(a-i))
