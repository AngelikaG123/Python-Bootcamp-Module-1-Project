from random import randint
import re

PATTERN = r"^([0-9]{0,2})D([0-9]{1,3})(?:[\+\-]([0-9]{1,2}))?$"
DICE_LIST = [3, 4, 6, 8, 10, 12, 20, 100]


correct = False
while not correct:
    try:
        code = input("Give a toss code: ")

        match = re.match(PATTERN, code)

        if match:
            toss_count = int(match.group(1)) if match.group(1) else 1
            dice_type = int(match.group(2))

            if dice_type not in DICE_LIST:
                raise Exception(f"Dice type {dice_type} is not supported.")

            modifier = int(match.group(3)) if match.group(3) else 0
            res_sum = 0

            for i in range(toss_count):
                res_sum += randint(1, dice_type)

            res_sum += modifier
            print(res_sum)
            correct = True
        else:
            raise ValueError("Incorrect toss code1.")
    except ValueError:
        print("Incorrect toss code.")