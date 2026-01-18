print("Syntax Revision")

#If statement needs to end with a colon and the block of code must be indented
if 5>2:
    print("Five is greater than two!")

#Incorrect indentation will raise an IndentationError
#Python does not use curly braces to define code blocks, instead it uses indentation
#no multiline comments in Python, use # for single line comments
#or triple quotes for multi-line strings that can act as comments

"""This is a multi-line comment, 
though it's actually a multi-line string.
Python will ignore it if it's not assigned to a variable.
"""

#Variable names must start with a letter or an underscore,
#and can only contain letters, numbers, and underscores
my_variable = 10
text= """This whole sentence is being assigned
to the variable called text."""

print(my_variable)
print(text)

#Variable names are case-sensitive
My_Variable = 20
print(My_Variable)

#You cannot use Python reserved words as variable names
#For example, the following would raise a SyntaxError:
# class = "MyClass"  # Uncommenting this line will cause an error   
# Use 'class_name' or another valid identifier instead
class_name = "MyClass"
print(class_name)

#You can assign multiple variables in one line
a, b, c = 1, 2, 3
print(a, b, c)

#You can also assign the same value to multiple variables
x = y = z = 0
print(x, y, z)

#Python uses dynamic typing, so you can change the type of a variable
var = 5       # var is an integer
print(var)
var = "Hello" # var is now a string
print(var)  

#Use type() to check the type of a variable
print(type(var))   
print(type(my_variable))

#Python supports different data types like int, float, str, list, dict, etc.
num = 10          # int
pi = 3.14        # float
name = "Alice"   # str
fruits = ["apple", "banana", "cherry"]  # list
person = {"name": "Bob", "age": 25}      # dict     
print(type(num))
print(type(pi))
print(type(name))
print(type(fruits))
print(type(person))

#You can delete a variable using the del statement
del my_variable
# print(my_variable)  # Uncommenting this line will raise a NameError since my_variable is deleted

#casting variables to different types
num_str = str(num)  # convert int to str
print(num_str)
str_num = int("123")  # convert str to int
print(str_num)
float_num = float("3.14")  # convert str to float
print(float_num)    
print(type(num_str))
print(type(str_num))
print(type(float_num))  

#string variables can use single or double quotes
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, World!"
print(single_quote_str)
print(double_quote_str) 
#both are valid in Python and serve the same purpose.
#triple quotes can be used for multi-line strings

#pascal case, camel case, snake case
PascalCase = "ThisIsPascalCase"
camelCase = "thisIsCamelCase"
snake_case = "this_is_snake_case"
