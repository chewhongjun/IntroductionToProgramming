sumInput=countInput=0                           #First we initalise 2 variables we will be using sum of the user input(sumInput) and count of user inputs(countInput)

userInput = input("Enter User Input:")          #Reads in the user input


while(userInput!='q'):                          #this loop breaks when the userInput is 'q'

    sumInput = sumInput+int(userInput)          #Adds the userInput value to the sum 
    countInput = countInput + 1                 #Increase the counter by 1

    userInput=input("Enter User Input:")        #This asks for the user to enter again and the loop restarts till you hit the value 'q'

print(str(countInput)+" Integers has been entered, with an summation value of "+str(sumInput))    #This is the print statement it is not complete if you can try to fix it!
