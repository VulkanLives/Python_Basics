#WHAT'S DIFFERENT!!!!
    # THIS PROGRAM has the same goal as "Number_Advanced3" except while testing the original program
    # it became apparent that if the user doesn't enter a number and presses <Enter>
    # it causes it to crash, so I will add an "if" statement to check somthing has been entered.
    # I will try two different methods, one using Python's equivelent to "null" which is "none"
    # second method I will try checking for empty quotation marks



def addition (number1 ,number2): # function to add to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 + num2
    return result  #IMPORTANT: this and the function below use returns, the other functions, include their own print statement
                    # WHY is this better? I may not want to print everytime I use these functions I may just want the result

def additionChanged (number1 ,number2): # function to add to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 + num2
    return result

def subtraction (number1 ,number2):  # function to subtract to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 - num2
    print("Your answer is: ",result)

def divide (number1 ,number2):  # function to divide to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 / num2
    print("Your answer is: ",result)

def multiply (number1 ,number2):  # function to multiply to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 * num2
    print("Your answer is: ",result)

def checkAnswer(userResponse):
    response = userResponse #takes data it has been passed and stores it in variable "response"
    check = bool = False      #creates a true or false variable
    try:
        val = int(response)
        check = True
    except ValueError:
       check = False
       print("That's not an int!")
       print("No.. input string is not an Integer. It's a string")
    return check


#THE ABOVE ARE JUST THE FUNCTIONS FOR THIS PROGRAM TO USE,
#THE BELOW IS THE ACTUAL PROGRAM

userInput1 = (input("Enter your first number: "))
validAnswer = checkAnswer(userInput1)   #use my function 'checkAnswer' above to make sure it's a number
while validAnswer == False:  #Creates a while loop that follows the indented instruction below
        print("No.. that is not avalid entry")
        userInput1 = (input("Enter your first number again: "))
        validAnswer = checkAnswer(userInput1) #this updates the validAnswer variable, eventually allowing us to break this loop
                                            # when the user enter an actual integer


userInput2 = (input("Enter your second number: "))
validAnswer = checkAnswer(userInput2)   #use my function 'checkAnswer' above to make sure it's a number
while validAnswer == False:  #Creates a while loop that follows the indented instruction below
        print("No.. that is not avalid entry")
        userInput2 = (input("Enter your second number again: "))
        validAnswer = checkAnswer(userInput2) #this updates the validAnswer variable, eventually allowing us to break this loop
                                            # when the user enter an actual integer



print("THIS IS TAKEN FURTHER IN NEXT CLASS 'Number_Advanced4.py' and will put the functions above into their own class called 'NumberCruncher'")










