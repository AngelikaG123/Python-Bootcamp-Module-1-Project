from random import randint

player1 = ['You',0]
player2 = ['Computer',0]
players = [player1,player2]
playing = True

def first_round():
    input("Press Enter to play.")
    for player in players:
        a = randint(1,6)
        b = randint(1,6)
        player[1] += a
        player[1] += b
    print(f"Your points: {player1[1]}, computer points {player2[1]}. Press Enter to play next round.")
    input("Press Enter to play next round.")


def round():

    for player in players:
        a = randint(1, 6)
        b = randint(1, 6)
        if a + b == 7:
            player[1] += int(player[1]/7)
        elif a + b == 11:
            player[1] += int(player[1]*11)
        else:
            player[1] += (a + b)
    input(f"Your points: {player1[1]}, computer points {player2[1]}. Press Enter to play next round.")

first_round()
while playing:
    round()
    if player1[1] >= 2001:
        print(f"{player1[0]} win!")
        playing = False
    elif player2[1] >= 2001:
        print(f"{player2[0]} wins!")
        playing = False



