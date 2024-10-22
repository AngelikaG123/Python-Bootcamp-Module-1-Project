from random import randint

win = False
number = randint(1, 100)

while not win:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("It's not a number!")

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You win!")
        win = True
