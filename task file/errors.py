# Compulsory Task 1

print ("Welcome to the error program") # Syntax error - Print was missing parentheses.

# Syntax error - There were some lines of code unnecessarily indented.
print ("\n") # Syntax error - Again print was missing parentheses.

ageStr = 24 # Syntax error - String should only contain the number and not words to be changed to an int and used in
# mathematical equations and the = should only be one = and not two.
age = ageStr # Runtime error - Integers cannot be concatenated with string.
print("I'm "+str(age)+" years old.") # Runtime Error - Age needed to be cast to string to be concatenated. Syntax error
# - There needs to be spaces for the sentence to read properly.
age = int(age)
three = 3

answerYears = age + three # Logical Error - The addition of two strings will only concatenate them.
# These needed to be integers.

print ("The total number of years: " + str(answerYears)) # Syntax error - Print was missing parentheses and
# answerYears in a variable and cannot be in inverted commas and needs to be a string.
answerMonths = (answerYears*12)+ 6 # Syntax error - answer needs to be answerYears and 6 months needs to be
# added to the equation
print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") # Print was missing parentheses and
# answerMonths needed to be cast to a string to be printed.



