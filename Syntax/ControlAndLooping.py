#Get an input from the user and use control if-else to check the value
#We have used int to convert the input string to an integer, since input() returns a string by default.
user_input = int(input("Enter a number: "))

#Check if the number is even or odd using if-else, control structure
#Don't forget the colon (:) at the end of the if and else statements
#Case indentation is important in Python, so make sure to indent the code block under if and else
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
    print("This line is also part of the if block.")
else:
    print(f"{user_input} is an odd number.")    

 #looping using for loop to iterate over a range of numbers
 # range(start, stop, step) generates a sequence of numbers from start to stop-1, incrementing by step
print("Numbers from 0 to 9:")
#loop only even numbers
for i in range(0, 10, 2):  # step of 2 to get even numbers
    print(i, end=' ')  # end=' ' keeps the output on the same line separated by spaces

#looping using for loop to iterate over a range of numbers with step of 1
# range(start, stop, step) generates a sequence of numbers from start to stop-1, incrementing by step
#print a new line for better readability
for i in range(0, 10, 1):
    print(i)

 #check if a number is prime using nested loops
 # A prime number is a number greater than 1 that has no divisors other than 1 and itself   
num_to_check = int(input("Enter a number to check if it's prime: "))
if num_to_check <2:
    print(f"{num_to_check} is not a prime number.")
else:
    for i in range(2,num_to_check):
        if num_to_check % i == 0:
            print(f"{num_to_check} is not a prime number.")
            break #break is used to exit the loop early if a divisor is found
    else:
        print(f"{num_to_check} is a prime number.")

#swapping two variables 
numberOne = int(input("Enter first number to swap: "))
numberTwo = int(input("Enter second number to swap: "))
print(f"Before swapping: numberOne = {numberOne}, numberTwo = {numberTwo}")
sum = numberOne + numberTwo
numberOne = sum - numberOne
numberTwo = sum - numberTwo
print(f"After swapping: numberOne = {numberOne}, numberTwo = {numberTwo}")
#Using a temporary variable to swap
temp = numberOne
numberOne = numberTwo
numberTwo = temp
print(f"After swapping: numberOne = {numberOne}, numberTwo = {numberTwo}")

#fibonacci series using loops
# Fibonacci series is a series where the next term is the sum of the previous two terms
# The series starts with 0 and 1
#For example, the first 10 terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
for i in range (0,21):
    a, b = 0, 1
    fibonacci_series = []
    while a <= i:
        fibonacci_series.append(a)
        a, b = b, a + b
    print(f"Fibonacci series up to {i}: {fibonacci_series}")    

list_fib = [0,1] 
for i in range(1,21):
   list_fib.append(list_fib[i-1] + list_fib[i])
print(f"Fibonacci series up to 20 using list: {list_fib}")

#factorial of a number using loops
# Factorial of a number n is the product of all positive integers less than or equal to n
# It is denoted by n!
# For example, 5! = 5 x 4 x 3 x 2 x 1 = 120
num_factorial = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, num_factorial + 1):
    factorial *= i  # same as factorial = factorial * i
print(f"The factorial of {num_factorial} is {factorial}")   