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
#Using a temporary variable to swap
temp = numberOne
numberOne = numberTwo
numberTwo = temp
print(f"After swapping: numberOne = {numberOne}, numberTwo = {numberTwo}")

        