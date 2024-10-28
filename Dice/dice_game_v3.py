from random import randint
DICE_LIST = [3, 4, 6, 8, 10, 12, 20, 100]

def points(toss_code):
    points = 0
    modifier = 0
    count = 1
    global dice
    for i in range(0,len(toss_code)):
        if toss_code[i] == '-' or toss_code[i] =='+':
            modifier = int(toss_code[i+1:]) if toss_code[i] == "+" else -int(toss_code[i+1:])
            toss_code = toss_code[:i]
            break
    count, dice = toss_code.split('D')
    if not count:
        count = 1
    count = int(count)
    dice = int(dice)

    for _ in range(1,count+1):
        number = randint(1, dice)
        points += number
    points += modifier
    return points

def roll():
    correct = False
    while not correct:
        try:
            my_code = input("Give your toss code: ")
            my_points = points(my_code)
            if dice not in DICE_LIST:
                raise ValueError("Invalid dice code")
            print(f"Your points: {my_points}")
            correct = True
            return my_points
        except ValueError:
            print(f"Your toss code is invalid.")
        except Exception:
            print("Your toss code is invalid.")


# print(roll("2D20-10"))
# print(roll("D6"))
# print(roll("3D12"))
# print(roll("D6+100"))

print(roll())



