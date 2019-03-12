import NumberCruncher #using the class "NumberCruncher"

userInput1 = int(input("Enter your first number: "))
userInput2 = int(input("Enter your second number: "))

print("Your entries added together = ",(NumberCruncher.addition(userInput1,userInput2)))
#The above print line gives the user entries to the function 'addition' inside 'NumberCruncher'
#The below print lines to the same with their respected functions

print("Your entries subtracted from one another = ",(NumberCruncher.subtraction(userInput1,userInput2)))
print("Your entries divided by each other = ",(NumberCruncher.divide(userInput1,userInput2)))
print("Your entries multiplied together = ",(NumberCruncher.multiply(userInput1,userInput2)))

#Below displays same answers but in sum form
print(userInput1," + ", userInput2, " = ",(NumberCruncher.addition(userInput1,userInput2)))
print(userInput1," - ", userInput2, " = ",(NumberCruncher.subtraction(userInput1,userInput2)))
print(userInput1," / ", userInput2, " = ",(NumberCruncher.divide(userInput1,userInput2)))
print(userInput1," * ", userInput2, " = ",(NumberCruncher.multiply(userInput1,userInput2)))


#NOW TO USE THE DATA IN A DIFFERENT WAY


addtionAnswer = (NumberCruncher.addition(userInput1,userInput2)) #loads answer from addition function and so on for the 3 lines
subAnswer = (NumberCruncher.subtraction(userInput1,userInput2))
divAnswer = (NumberCruncher.divide(userInput1,userInput2))
timesAnswer =(NumberCruncher.multiply(userInput1,userInput2))

#Loads new variables with data to pass test for zero function
subZeroCheck =(NumberCruncher.notZero(subAnswer)) #passes subAnswer to zeroCheck function in NumberCruncher class
addZeroCheck =(NumberCruncher.notZero(addtionAnswer)) #passes addAnswer to zeroCheck function in NumberCruncher class
divZeroCheck =(NumberCruncher.notZero(divAnswer)) #passes divAnswer to zeroCheck function in NumberCruncher class
timesZeroCheck =(NumberCruncher.notZero(timesAnswer)) #passes timesAnswer to zeroCheck function in NumberCruncher class

#prints zero check results
print("Did adding give zero as an answer? :",addZeroCheck)  #these lines should explain themselves
print("Did subtracting give zero as an answer? :",subZeroCheck)
print("Did dividing give zero as an answer? :",divZeroCheck)
print("Did multiplyinh give zero as an answer? :",timesZeroCheck)












