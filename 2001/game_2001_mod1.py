from random import randint
import random
DICE_LIST = [3, 4, 6, 8, 10, 12, 20, 100]
player1 = ['You',0] # player name, points
player2 = ['Computer',0]
players = [player1,player2]
game_rnd= 1
def special_points(new_points, player):
    if new_points == 7 and game_rnd != 1:
        player[1] = player[1]/7
    elif new_points == 11 and game_rnd != 1:
        player[1] = player[1]*11
    else:
        player[1] += new_points

def points(dice1, dice2, player):
    lst = [dice1, dice2]
    pts = 0
    for dice in lst:
        pts += randint(1,dice)
    special_points(pts, player)

def game_round():
    try:
        print("Dices to choose: 3, 4, 6, 8, 10, 12, 20, 100")
        dice1 = int(input("Give 1st dice: "))
        dice2 = int(input("Give 2nd dice: "))
        if dice1 not in DICE_LIST or dice2 not in DICE_LIST:
            raise ValueError
        points(dice1, dice2, player1)
        dice3 = random.choice(DICE_LIST)
        dice4 = random.choice(DICE_LIST)
        points(dice3, dice4, player2)
    except ValueError:
        print("Invalid input. Type the numbers associated with the dice types you want to toss.")
    except Exception:
        print("Something went wrong")

    print(f"Your points: {player1[1]}, Computer's points: {player2[1]}")
    input("Press Enter to play next round.")

def main_game():
    playing = True
    while playing:
        game_round()
        if player1[1] >= 2001:
            print(f"{player1[0]} win! Points: {player1[1]}")
            playing = False
        elif player2[1] >= 2001:
            print(f"{player2[0]} wins! Points: {player2[1]}")
            playing = False

main_game()