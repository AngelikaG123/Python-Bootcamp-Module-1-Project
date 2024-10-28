min = 0
max = 1000
win = False
counter = 0

print("Pick a number between 0 and 1000 and remember it.")

while not win:
    guess = int((max - min) / 2 + min)
    print(f"My guess is: {guess}. Did I win?")
    try:
        decision = int(input("Type: 1 - I won     2 - too small    3 - too big. \nDecision: "))
        if decision == 1:
            print(f"Yay! I won in {counter} tries!")
            win = True
            counter += 1
        elif decision == 2:
            min = guess
            counter += 1
        elif decision == 3:
            max = guess
            counter += 1
        else:
            print("Do not cheat!")
    except ValueError:
        print("Please enter a number in the range 1-3.")

