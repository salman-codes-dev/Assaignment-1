# 1. Ask the users for their name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# 2. Ask the users for two numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number:"))

# 3. Calculate addition, subtraction, multiplication and division 
addition = num1 + num2 
subtraction = num1 - num2 
multiplication = num1 * num2 
division = num1 / num2 

# 4. Display all information using f-strings
print(f"\nHello, {name} !")
print(f"Your age is {age} .")
print(f"\nAddition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")



