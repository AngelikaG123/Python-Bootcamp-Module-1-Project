from flask import Flask, request

counter = 0

app = Flask("Guess_the_number_3")



@app.route("/", methods=["GET", "POST"])
def guess_the_number_3():
    min_val = 0
    max_val = 1000
    if request.method == "GET":
        guess = int((max_val - min_val) / 2 + min_val)
        html = f"""
                    <form method="POST"> 
                        <input type="hidden" name="min_val" value={min_val}>
                        <input type="hidden" name="max_val" value={max_val}>
                        <input type="hidden" name="guess" value={guess}
                        <p>Let's play the game! I will pick a number in the range 0-1000, 
                        and you will tell me if I guessed.</p>
                        <p>My guess is {guess}</p>
                        <label for="guess">Did I win?</label>
                        <input type="submit" name="choice" value="Yes!">
                        <input type="submit" name="choice" value="Too big!">
                        <input type="submit" name="choice" value="Too small!">

                </form>
                    """
        return html

    elif request.method == "POST":
        answer = request.form.get("choice")
        guess = int(request.form.get("guess"))
        min_val = int(request.form.get("min_val"))
        max_val = int(request.form.get("max_val"))
        if answer == "Yes!":
            return "Congratulations! You guessed the number! :)"
        elif answer == "Too big!":
            max_val = guess
        elif answer == "Too small!":
            min_val = guess
        guess = int((max_val - min_val) / 2 + min_val)
        return f"""
                    <form method="POST"> 
                        <input type="hidden" name="min_val" value={min_val}>
                        <input type="hidden" name="max_val" value={max_val}>
                        <input type="hidden" name="guess" value={guess}
                        <p>Let's play the game! I will pick a number in the range 0-1000, 
                        and you will tell me if I guessed.</p>
                        <p>My guess is {guess}</p>
                        <label for="guess">Did I win?</label>
                        <input type="submit" name="choice" value="Yes!">
                        <input type="submit" name="choice" value="Too big!">
                        <input type="submit" name="choice" value="Too small!">
                </form>
                    """


if __name__ == "__main__":
    app.run(debug=True)