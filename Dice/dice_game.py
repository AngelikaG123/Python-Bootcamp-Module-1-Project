from random import randint

dice_type = 0
toss_count = 1
modifier = 0
DICE_LIST = [3, 4, 6, 8, 10, 12, 20, 100]
correct_toss = False

toss_code = "2D20-3"

def roll_dice(toss_code):
    code = toss_code.split()


def find_modifier(lst):
    '''
    This function finds if there is a modifier to be added/subtracted from the result

    :param lst: a list of characters from the input,
                that is the type of toss, without the first, optional toss_count number

    :return: position of the sign that signals the presence of modifier or lack thereof
    '''
    for i in range(len(toss_code)):
        if toss_code[i] == '-' or toss_code[i] == '+':
            return i
    return -1

def find_type_of_dice_modifier(lst, a = 0, b = 0):
    '''
    This function allows to find both type of dice and modifier

    :param lst: a list of the characters with coded dice type and modifier,
                without the first, optional toss_count number
    :param a: beginning of the checked list
    :param b: end of the checked list
    :return: dice type or modifier
    '''
    res = ""
    sign = find_modifier(lst)
    for i in range(a,b):
        i = str(lst[i])
        res += i
    if a > 0 and sign >=0:
        res = -int(res) if lst[sign] == '-' else int(res)
    else:
        res = int(res)
    return res

while not correct_toss:
    try:
        toss = input("Insert the code for your toss, eg. 2D20-10: ")
        toss_code = list(toss)

        # find how many tosses do we have to get and edit the list to remove this number
        if toss_code[0].isdigit():
            toss_count = int(toss_code[0])
            toss_code = toss_code[2:]
        else:
            toss_code = toss_code[1:]

        # if there is no sign like plus or minus in the given code
        if find_modifier(toss_code) == -1:
            dice_type = find_type_of_dice_modifier(toss_code, 0, len(toss_code))
        # if there is a plus or a minus in the given code
        else:
            dice_type = find_type_of_dice_modifier(toss_code,0 , find_modifier(toss_code))
            modifier = find_type_of_dice_modifier(toss_code,find_modifier(toss_code)+1 , len(toss_code))
        if dice_type not in DICE_LIST:
            print("You can pick those types of dice: D3, D4, D6, D8, D10, D12, D20 or D100.")
            raise ValueError
        correct_toss = True
    except ValueError:
        print("Give a correct code for a toss.")

# count the result
toss_res = []
for i in range(1,toss_count+1):
    new_toss = randint(1,dice_type)
    toss_res.append(new_toss)
sum_of_toss = sum(toss_res)
sum_of_toss += modifier
print(f"Your points:{sum_of_toss}")