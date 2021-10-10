import random

number = random.randint(1, 99)
guess = int(input("Try to guess a number between 1 and 99: "))

while number != "guess":
    if guess < number:
        guess = int(input("Try to guess a bigger number: "))
    elif guess > number:
        guess = int(input("Try to guess a smaller number: "))
    else:
        print("it's corrcet!!!!!!!")
        break
