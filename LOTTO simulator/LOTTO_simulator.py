from random import randint

player_num = []
computer_num = []

counter = 1
computer_counter = 1
win_number = 0

while counter < 7:
    try:
        number = (int(input(f'Give #{counter} number: ')))
        if number in player_num:
            print("This number was already stated.")
            raise ValueError
        if number < 1 or number > 49:
            raise ValueError
        else:
            player_num.append(number)
            counter += 1
    except ValueError:
        print("Please type a number in the range 1-49.")

player_num.sort()

print(f"Your numbers: {player_num}")

while computer_counter < 7:
    number = randint(1, 49)
    if number in computer_num:
        continue
    else:
        computer_num.append(number)
        computer_counter += 1


computer_num.sort()
print(f"Computer numbers: {computer_num}")

for i in player_num:
    if i in computer_num:
        win_number += 1

if win_number >= 3:
    print(f"Congratulations! You guessed {win_number} numbers.!")
else:
    print(f"Sorry, you guessed only {win_number} numbers. Good luck next time!")