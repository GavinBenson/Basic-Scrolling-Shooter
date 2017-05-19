# Data Types
# Native data types in Python
count = 5           # Integer
gpa = 3.9           # Float
name = 'Phred'      # String
isPassing = True    # Boolean
print(count)
aStringOfNumbers = '341'
# print(aStringOfNumbers + count)
# CONVERT
# Convert the string into an integer
# int() - convert something into an integer
# str() - convert something into a string
# float() - convert something into a fraction
print(aStringOfNumbers + str(count))
print('The count is:', count)
print('The count as a float is:', float(count))
print('The gpa as an integer is:', int(gpa))
# print('A string of float as an int:', int("3.14"))

# INPUT
booger = input('What is your name? ') # Bad variable name, but valid!
print('Hello', booger, 'nice to meet you!')
money = input('How much money do you have?')
print('Really? $' + money + ' is that all?')

# MATH
# + - addition
# - - subtraction
# * - multiply
# / - float division
# // - integer division
# % - modulus (remainder)
# ** - exponents
print(3 ** 2)




# FUNCTIONS & CLASSES
# Functions are mini python programs
def sayLotsOfStuff ():
    # Indent all your code that belongs to the function!
    print("Lots of\nStuff")
    # print("Stuff")
    
# MAIN PROGRAM!!
sayLotsOfStuff()

# A function with parameters
def sayThreeTimes(word1, word2):
    print(word1 + "\n" + word1 + "\n" + word1)
    print(word2 + "\n" + word2 + "\n" + word2)

sayThreeTimes("Repeat","Do again")

# Write a function and call it that prints the cube of a number.
def cube (num):
    print(num*num*num)

cube(5)

# CLASSES
# Use classes when you want to group data together!
class Student:
    def __init__(self, name, grade, course):
        # Initialize the data in the class
        self.name = name
        self.grade = grade
        self.course = course
        self.id = 34
        
    # Accessor function to class data
    def getGrade(self):
        print('getGrade()')
        return(self.grade)
        
    # Accessor function to grade level
    # Write the accessor function to set a new grade level
    def setGrade(self, level):
        self.grade = level
        
    def increaseGrade(self):
        self.grade = self.grade + 1
        
student1 = Student("Sarah", 11, "Math")
print(student1.name)
print(student1.grade)
print("Sarah's grade level is:", student1.getGrade())
# Create a student with name "Tim", senior, "Computer Sci Prin"
# Print Tim's student id
student2 = Student("Tim", 12, "Computer Sci Prin")
print('New student ID: ',student2.id)

# Give Sarah a new grade level
print(student1.grade)
student1.setGrade(12)
print(student1.grade)
student1.increaseGrade()
print(student1.grade)

# Create a new class for schools
# Constructor will take name of school, number of students, city
# Write a class accessor to change the number of students




# Python IF Statement
# IF is the keyword
# indentation really really matters!
# Indent all the code under the IF
# Indent all the code under the ELSE
# End your IF with a colon!
# DO NOT USE '{' or '}' !!!
num = 60
if (num >= 90):
    print("Greater!")
print('The end')

# The comparison operators
# (==) - equality
# (>=) (>) - greater than or equal
# (<=) (<) - less than or equal
# (!=) - inequality

#  Example of an IF .. ELSE
answer = int(input('Enter a integer: '))
if (answer >= 60): 
    print('That\'s over a minute.')
else:
    print('Under a minute')
print('the end again')

# Example of IF .. ELIF .. ELSE
if (answer < 60):
    print('less than a minute')
elif (answer < 120):
    print('less than two minutes.')
elif (answer < 300):
    print('less than five minutes')
else:
    print('over five minutes!')
print('the final end')

# LOGICAL Operators
# () and () - AND operator
# () or () - OR operator
# not () - NOT operator (reverses the true / false)
if (answer < 0) or (answer > 1000):
    print('invalid input')
print('truely the end')
    
    
    
    
# Python LISTS and ARRAY
grocery = []
print(grocery)
grocery = ['eggs', 'MILK', 'cheese', 3.1415]
print(grocery)
print(grocery[1])
# Print the 8th thing in the list
# print(grocery[7])

# Write the code to create a list of student names
# Initialize the list to at least 3 names.
students = ['Phred', 'Bob', 'bone head', 'brillent', 'motor mouth']

# Create a list of numbers
numbers = [-23, 3.14, 65, 22, 75]
# You can do math for INDEX
print(numbers[6-4])
index = 1
print(numbers[index])

# Cool functions associated with lists
numbers.append(-9.25)
print(numbers)
numbers.insert(2, 674632)
print(numbers)
numbers.remove(22)
print(numbers)
# This won't work because the number is not in the list!
# numbers.remove(338404982348239)

# A related function is len() - short for length!
print('The list has', len(numbers), 'items in it.')

# LOOPing through lists!
# Hint: Don't use the while loop -- instead use the for
index = 0
while (index < len(numbers)):
    print(numbers[index])
    index += 1

for item in numbers:
    print(item)
    
# Write a program that asks the user for a list of cool software games.
# Store the names of the games in a list.
# Have the user type "done" when no more cool software will be entered
# Print each software title individually use a for loop
games = []
title = input('Favorite game: ')
while (title != 'done'):
    games.append(title)
    title = input('Favorite game: ')
for item in games:
    print(item)
 
    


	
# Python Loops
# WHILE
# while (comparison):
#   Indent the code you want to repeat
# Stop the loop by unindenting.
# Write a program that counts to 5.
counter = 1
while (counter < 6):
    print(counter)
    counter += 1
print('the end of the while')

# Write a program that asks the user to keep looping.
# Acceptable answers are 'y' and 'n'.
# Your program keeps asking the question until 'n' is entered
response = 'y'
while (response == 'y'):
    response = input('Keep looping?')
print('Ok. All done.')

num = 342
digit = num % 10
print(digit)
num = num // 10
digit = num % 10
print(digit)
num = num // 10
digit = num % 10
print(digit)
num = num // 10

# Write the above program using a loop!
# It prints the digits in an integer in reverse order
num = 342
while (num > 0):
    digit = num % 10
    print(digit)
    num = num // 10

# Write a fuction called 'power' that take an integer parameter
# Return the value of 2 to the power of the parameter
# Do not use the exponent operator!  Use a loop to repeat multiplication















