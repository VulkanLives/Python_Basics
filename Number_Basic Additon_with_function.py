def addition (number1 ,number2):
    num1 = number1
    num2 = number2
    result = num1 + num2
    print(result)



userInput1 = input("Enter your first number: ")
userInput2 = input("Enter your second number: ")

addition(userInput1,userInput2)
print(" ^^^^ This happened becuase we didn't define the inputs to be numbers or more specifically wholes number i.i 'ints'")

print("lets try that again and declare the inputs as 'ints'")
userInput1 = int(input("Enter your first number: "))
userInput2 = int(input("Enter your second number: "))
addition(userInput1,userInput2)



