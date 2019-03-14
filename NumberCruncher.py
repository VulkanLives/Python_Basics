def addition (number1 ,number2): # function to add to the numbers it is passed and return result
    num1 = number1
    num2 = number2
    result = num1 + num2
    return result

def subtraction (number1 ,number2):  # function to subtract to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 - num2
    return result

def divide (number1 ,number2):  # function to divide to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 / num2
    return result

def multiply (number1 ,number2):  # function to multiply to the numbers it is passed
    num1 = number1
    num2 = number2
    result = num1 * num2
    return result

def notZero (number):  #checks if number is 0
    num = number
    if num == 0:
        zero_check = True
    else:
         zero_check = False
    return zero_check

def confirmInt(userResponse): #CHECKS THAT WHATEVER ITS PASSED IS A INT/NUMBER, NEEDS TWEAKING TO CHECK FOR OTHER DATA/VAR TYPES
    response = userResponse #takes data it has been passed and stores it in variable "response"
    check = bool = False      #creates a true or false variable
    try:
        val = int(response) #simply checks that response is an INT
        check = True
    except ValueError:   # ValueError is pre-defined, hence the caps on V and E , basically says anything "Try" can't do then its an error
       check = False
       print("That's not an int!")
       print("No.. input string is not an Integer. It's a string")
    return check

