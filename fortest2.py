import random

#to get random number
number = random.randint(1, 100)

# Introduction
print("You Are Welcome To a game of guesses.")
print("Here You Have to guess a number and the number will anywhere between 1-100")
print("Are You Ready !!! Let's start!!!")

#start of game
for i in range(11):
    chance_left = 10-i
    attempt = i+1
    guess = (int(input("Enter your guess: ")))


    if i == 10:
        print("Ohh GAMEOVER!!!!!!!!!! ")
    if guess == number:
        print("WOW!!! You guess the number in ", attempt)
        print("attempts")
        break

    if guess < number:
        print("Your Left chance is",chance_left)
        print("The Number is greater than ", guess)


    if guess > number:
       print("Your Left chance is", chance_left)
       print("The Number Is Smaller than", guess)
