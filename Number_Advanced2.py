def addition(number1, number2):  # function to add to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 + num2
    print("Your answer is: ", result)


def Subtraction(number1, number2):  # function to subtract to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 - num2
    print("Your answer is: ", result)


def Divide(number1, number2):  # function to divide to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 / num2
    print("Your answer is: ", result)


def Multiply(number1, number2):  # function to multiply to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 * num2
    print("Your answer is: ", result)


userInput1 = int(input("Enter your first number: "))
userInput2 = int(input("Enter your second number: "))

print("what would like to do with these numbers?")
userChoice = int(input("<1> = addition, <2> = subtraction, <3> = divsion, <4> = multiply"))
print(userChoice, "<----TEST CASE, FOR DEBUG PURPOSES ONLY")

if userChoice == 1:
    print("you chose to add")
    addition(userInput1, userInput2)
else:
    if userChoice == 2:
        print("you chose to subract")
        Subtraction(userInput1, userInput2)
    else:
        if userChoice == 3:
            print("you chose to divide")
            Divide(userInput1, userInput2)
        else:
            if userChoice == 4:
                print("you chose to multilpy")
                Multiply(userInput1, userInput2)
            else:
                print(
                    "guess you don't play by the rules")  # IF THE USER DOESN'T A PRE-DESCRIBED OPTION, EVERYTHING ELSE SHOULD SPEAK FOR ITSELF


