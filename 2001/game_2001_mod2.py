from flask import Flask
from flask import request
from random import randint
import random

app = Flask("moja appka")

def special_points(pts, player, game_rnd):
    if pts == 7 and game_rnd !=1:
        player = int(player/7)
    elif pts == 11 and game_rnd !=1:
        player = player*11
    else:
        player += pts
    return player

def points(dice1, dice2, player, game_rnd):
    pts = randint(1,dice1) + randint(1,dice2)
    return special_points(pts, player, game_rnd)

@app.route('/', methods=['GET', 'POST'])
def game_2001():
    if request.method == 'POST':
        DICE_LIST = [3, 4, 6, 8, 10, 12, 20, 100]

        p1 = int(request.form.get('p1'))
        p2 = int(request.form.get('p2'))
        game_rnd = int(request.form.get('rnd', 1))

        dice1 = int(request.form.get("dice1"))
        dice2 = int(request.form.get("dice2"))
        p1 = points(dice1, dice2, p1, game_rnd)

        dice3 = random.choice(DICE_LIST)
        dice4 = random.choice(DICE_LIST)
        p2 = points(dice3, dice4, p2, game_rnd)
        game_rnd += 1

        if p1 >= 2001:
            return f"You win! Points: {p1}"
        elif p2 >= 2001:
            return f"Computer wins! Points: {p2}"
        return f"""
                        <form method="POST">
                            <h1>Gra w 2001</h1><br>
                            <label for="description">Wins the player that first gets 2001 points.</label><br>
                            <label for="points">Your points: {p1}. Computer's points {p2}</label><br>
                            <select id="dropdown" name="dice1">
                              <option id="option1" value="3">3</option>
                              <option id="option2" value="4">4</option>
                              <option id="option3" value="6">6</option>
                              <option id="option4" value="8">8</option>
                              <option id="option3" value="12">12</option>
                              <option id="option4" value="20">20</option>
                              <option id="option4" value="100">100</option>
                            </select>
                            <select id="dropdown" name="dice2">
                              <option id="option1" value="3">3</option>
                              <option id="option2" value="4">4</option>
                              <option id="option3" value="6">6</option>
                              <option id="option4" value="8">8</option>
                              <option id="option3" value="12">12</option>
                              <option id="option4" value="20">20</option>
                              <option id="option4" value="100">100</option>
                            </select>
                            <input type="hidden" name="p1" value={p1}>
                            <input type="hidden" name="p2" value={p2}>
                            <input type="hidden" name="rnd" value={game_rnd}>
                            <input type="submit" value="Play">
                        </form>
                    """
    else:
        p1 = 0
        p2 = 0
        game_rnd = 1
        return f"""
                        <form method="POST">
                            <h1>Gra w 2001</h1><br>
                            <label for="number">Wins the player, who first gets to 2001 points.</label><br>
                            <select id="dropdown" name="dice1">
                              <option id="option1" value="3">3</option>
                              <option id="option2" value="4">4</option>
                              <option id="option3" value="6">6</option>
                              <option id="option4" value="8">8</option>
                              <option id="option3" value="12">12</option>
                              <option id="option4" value="20">20</option>
                              <option id="option4" value="100">100</option>
                            </select>
                            <select id="dropdown" name="dice2">
                              <option id="option1" value="3">3</option>
                              <option id="option2" value="4">4</option>
                              <option id="option3" value="6">6</option>
                              <option id="option4" value="8">8</option>
                              <option id="option3" value="12">12</option>
                              <option id="option4" value="20">20</option>
                              <option id="option4" value="100">100</option>
                            </select>
                            <input type="hidden" name="p1" value={p1}>
                            <input type="hidden" name="p2" value={p2}>
                            <input type="hidden" name="rnd" value={game_rnd}>
                            <input type="submit" value="Play">
                        </form>
                    """

if __name__ == "__main__":  # magiczna skrzynka
    app.run(debug=True)