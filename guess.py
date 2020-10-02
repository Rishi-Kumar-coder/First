import random

num = random.randint(1, 100)

for i in range(10):
    guess = (int(input("Enter Your Guess: ")))

    if guess == num:
        print("Wow You Choice The Correct number !!!")
        print("You completed it in", i+1, "Attempts!!")
        break

    if guess > num:
        print("You have only", 9 - i, "Chances left")
        print("Try A smaller Number. ")
        continue

    if guess < num:
        print("You have only", 9-i, "Chances left")
        print("Try A Bigger Number.")
        continue

    if i == 9:
        break