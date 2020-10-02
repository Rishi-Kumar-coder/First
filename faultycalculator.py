# 45*3 , 56+9 , 56/6

print("Whelcome To CalCulator!!!")
num_1 = (int(input("Enter First NUmber: ")))
num_2 = (int(input("Enter Second Number: ")))

if num_1 * num_2 == 135 :
    print('555')

elif num_1 + num_2 == 65 :
    print(69)

elif num_1/num_2 == 9.33:
    print(976)

else:
    input = input("Choice one \nAdd---1\nsub---2\nDiv---3\nmultiply---4\n")
    if input == 1:
        ans = num_1+num_2
        print(ans)
    elif input == 2:
        ans = num_1 - num_2
        print(ans)
    elif input == 3:
        ans = num_1 / num_2
        print(ans)
    elif input == 4:
        ans = num_1 * num_2
        print(ans)







