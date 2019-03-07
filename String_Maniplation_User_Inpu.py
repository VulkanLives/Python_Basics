#printCaps below takes what it is passed converts it to caps
# e.g. if it's fed 'spoon' it will return 'SPOON'
# food for thought: what if pass it a number
def printCaps(subjectText):
    text = subjectText.upper()
    print(text)

#below function will print first letter in caps for each word in sentence
def printSentenceCase(subjectText):
    text = subjectText.title()
    print(text)

def reverseText(subjectText):
    text = subjectText
    reversed_text = text.split()
    reversed_text.reverse()
    print(reversed_text)  # prints 'reversed_text' as an array/list as we haven't joined back together
    reversed_text_joined = "".join(reversed_text)
    print(reversed_text_joined, " <---- THIS IS ALL ONE WORD BECAUSE WHEN WE JOINED WE DID ADD A SPACE BETWEEN SPEECH MARKS, see the line of code above")
    reversed_text_joined = " ".join(reversed_text)
    print(reversed_text_joined)
    print("\033[1;32;40m Bright Green  \n")   # The above ANSI escape code will set the text colour to bright green. The format is;
    print("\033[1;32;40m Bright Green]")      # \033[  Escape code, this is always the same
    print("\033[", reversed_text_joined)       #  1 = Style, 1 for normal.
                                              #32 = Text colour, 32 for bright green.
                                              #40m = Background colour, 40 is for black.


#---------------------------------------------------------------------------------------------
#
#       The above are my functions
#       The below prompts the user then calls the the functions
#----------------------------------------------------------------------------------------------




#below prompts user to enter text, no limit totext as I have set none
# I used the same variables for functions 'subjectText' and for input on purpose to see if if affected the outcome
# it didn't, but I would usually have different var name for everything appropiately named so not to cause confusion



UserInput = str(input("enter some text:\n"))
printCaps(UserInput)
printSentenceCase(UserInput)
reverseText(UserInput)


# IN CLOSING, THIS CAN BE DONE MUCH MORE EFFICIENTLY USING CLASSES, WHICH I INTEND TO DO LATER, BUT GOOD TO KEEP THE BASICS
# SAVED BEFORE YOUR PROGRAMS START GETTING TOO SMART, LIKE HANSEL AND GRETTEL LEAVING BREADCRUMBS
