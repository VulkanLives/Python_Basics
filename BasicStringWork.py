print ("Hello World") # prints the obvious

#Example 1
# below is the same result using a variable
message = 'Hello World, printed through a variable'
print(message, '(Example 1)')

#Example 2
#below uses ".title()" to print string capitalised in sentance case (first letters of each with caps
name = ('ada lovalace')
print(name, '(printed normally)')
print(name.title(), '(Printed using ".title" gives us the caps)', '(Example 2)')

#Example 3
#below is same as above but ".upper()" = ALL CAPS
# and ".lower()" = all lower case
name = "Ada Lovelace"
print(name.upper(), '(Example 3)')
print(name.lower(), '(Example 3)')

#Example 4
#Combining strings: It’s often useful to combine strings. For example,
# if you might want to store a first name and a last name in separate variables,
# and then combine them when you want to display someone’s full name:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name, '(Example 4)' )

#Example 5
#This method of combining strings is called concatenation. You can use
#concatenation to compose complete messages using the information you’ve
#stored in a variable.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!" ,'(Example 5)' )

#Example 6
#use concatenation to compose a message and then store the
#entire message in a variable:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message ,'(Example 6)')
#This code displays the message “Hello, Ada Lovelace!” as well, but storing
#the message in a variable at 1 makes the final print statement at 2 much simpler.

##Example 7
#To add a tab to your text, use the character combination \t as shown:
print("Python", "without tab")
print("\tPython", "with tab")
print("To add a newline in a string, use the character combination \n:")
print("Languages:\nPython\nC\nJavaScript")

#Numbers
print('Mathematics') # the following 4 lines set variable holding the values we want for print statements below
addition = 2 + 3
subtraction = 3 - 2
multiplication = 2 * 3
division = 3 / 2

print('\tThe sum of 2 + 3 =',+addition)
print('\tThe sum of 3 - 2 =',+subtraction)
print('\tThe sum of 2 x 3 =',+multiplication)
print('\tThe sum of 3 / 2 =',+division, 'Number exercise 1')

#Using Strings and integers without confusing python
#When you use integers within strings, you need to specify explicitly that you want Python to use the integer
#as a string of characters.
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message,"still in numbers part of code, just below 'Number exercise 1' ")



