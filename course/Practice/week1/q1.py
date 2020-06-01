#Take in 10 user input(integers), and print the average on screen


numOfTries=0

inputNumber = 0
sumNumber = 0

while numOfTries < 10:
    inputNumber = input("User input: ")
    sumNumber = sumNumber + int(inputNumber)

    numOfTries = numOfTries + 1

print("sum: "+ str(sumNumber))