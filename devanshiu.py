import random

print("Welcome to Number Guessing Game!")

number = random.randrange(1, 100)
attempts = 0

while True:
    guess = int(input("Enter the number you think it is (1-100): "))
    attempts += 1

    if guess < number:
        print("greater than this no ")

    elif guess > number:
        print("less than this one ")

    else:
        print("Congratulation ! you won this game in",attempts,"attempts")
        break