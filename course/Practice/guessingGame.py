import random

randNum= random.randrange(1,10)

userGuess = int(input("Guess a number from 1 and 10: "))

while(userGuess != randNum):
    print("You guessed wrongly\n Try again!")
    userGuess = int(input("Guess a number from 1 and 10: "))


print("Congrats! You guessed the right number")
 


