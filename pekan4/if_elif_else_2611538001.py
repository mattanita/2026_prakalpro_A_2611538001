# Create a file named if_elif_else_nim.py
# Create a program using if-elif-else conditional statements
# Add the last 4 digits of your student ID to the variable name, e.g., ipk_1234
# This program uses the input() function

age = int(input("Enter your age: "))
sim = input("Do you have a Class C driver's license (y/n): ")[0]

if age >= 17 and sim == 'y':
    print("You are an adult and allowed to ride a motorcycle")

elif age >= 17 and sim != 'y':
    print("You are an adult but not allowed to ride a motorcycle")

elif age < 17 and sim == 'y':
    print("You are not old enough to have a driver's license")

else:
    print("You are not old enough and not allowed to ride a motorcycle")

print("Program completed") 