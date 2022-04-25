import random

score = 0

# Functions
def StartGuessingGame():
    # For the Scoring
    global score
    print(f'Your Score: {score}')

    # Variables
    age = random.randint(1, 100)
    lives = 3

    print(f"You can guess {lives} times")
    while lives > 0: 
        try:
            guess = int(input("Guess the number : "))   # The int converts the string from input to an int | If the input is an invalid integer (input is letter), it will throw an error
        except ValueError:                              # Skip the if-else statements and repeat if error
            print("Invalid Guess")
            continue                

        if guess > age:
            print("your guess is higher.")
            lives -= 1
        elif guess < age:
            print("your guess is lower.")
            lives -= 1
        else: 
            print("your guess is correct")
            lives *= 100
            score += lives
            break

        print(f'You have {lives} lives left')

    # Game Over Outputs
    print(f'\nmy generated age is = {age}')
    print(f'your last guess = {guess}\n')
    print(f'You won: {lives}')
    print(f'Your Score: {score}')
    tryAgainInput = int(input("Want to play again? (1 for yes | Any for no) : "))
    if tryAgainInput == 1:
        StartGuessingGame()
    else:
        return()


StartGuessingGame()
