import random

# Variables
age = random.randint(1, 100)
guess = int(input('enter your guess : '))
print(f'my generated age is = {age}')
# The int converts the string from input to an int
# If the input is an invalid integer (input is letter), it will throw an error

if guess > age:
    print("your guess is higher.")
elif guess < age:
    print("your guess is lower.")
else: 
    print("your guess is correct")
    guess = int(input('enter your guess : '))

