#THIS PROGRAM IS ALMOST REDUNDENT IN THE WAKE OF Number_Advanced4.py BUT A GOOD REFERNECE POINT FOR THE CHANGES....
# I MADE IN Number_Advanced3-2.py

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

#THE ABOVE ARE JUST THE FUNCTIONS FOR THIS PROGRAM TO USE,
#THE BELOW IS THE ACTUAL PROGRAM

userInput1 = int(input("Enter your first number: "))
userInput2 = int(input("Enter your second number: "))

addition(userInput1,userInput2)
subtraction(userInput1,userInput2)
divide(userInput1,userInput2)
multiply(userInput1,userInput2)
print(addition(userInput1,userInput2),"1st test line") #by printing it this ways it shows I use a var to capture the rseult of addition
#now watch
varExample = int(additionChanged(userInput1,userInput2))
print(varExample,"2nd test line")

#The point of the above 2 lines, using the return command in the addition function "additionChanged" and loading in into
#the newly declared variable 'varExample', now I could stow these fucntions into a different class to make this program more streamlined
#and the call on the data and use how I please

print("THIS IS TAKEN FURTHER IN NEXT CLASS 'Number_Advanced4.py' and will put the functions above into their own class called 'NumberCruncher'")




