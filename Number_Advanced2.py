def addition (number1 ,number2):
    num1 = number1
    num2 = number2
    result = num1 + num2
    print(result)

def Subtraction (number1 ,number2):
    num1 = number1
    num2 = number2
    result = num1 - num2
    print(result)

def Divide (number1 ,number2):
    num1 = number1
    num2 = number2
    result = num1 / num2
    print(result)

def Multiply (number1 ,number2):
    num1 = number1
    num2 = number2
    result = num1 * num2
    print(result)

userInput1 = int(input("Enter your first number: "))
userInput2 = int(input("Enter your second number: "))

print("what would like to do with these numbers?")
userChoice =int(input("<1> = addition, <2> = subtraction, <3> = divsion, <4> = multiply"))
print(userChoice)

if userChoice == 1:
    print("you chose to add")
    addition(userInput1,userInput2)             # THIS IS NOW OBVIOUS WHAT THESE CALLS DO
else:
    if userChoice == 2:
        print("you chose to subract")
        Subtraction(userInput1,userInput2)          # NOTE TO SELF THOUGH:
    else:
        if userChoice == 3:
            print("you chose to divide")
            Divide(userInput1,userInput2)                   #PRETTY SURE THERE IS A REASON WE DON'T START FUNCTIONS WITH
        else:
            if userChoice ==4:
                print("you chose to multilpy")
                Multiply(userInput1,userInput2)                 # A CAPITAL LETTER, MUST GOOGLE THIS
            else:
                print("that was not a valid choice")









