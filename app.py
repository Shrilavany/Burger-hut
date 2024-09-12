from flask import Flask, render_template, request
import math
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play-game', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        turn1 = int(request.form['turn1'])
        turn2 = int(request.form['turn2'])

        if turn1 >= turn2:
            return "Error: The number of dishes must be less than the number of branches."

        # Calculate total chances using the logarithmic formula
        total_chances = math.ceil(math.log(turn2 - turn1 + 1, 2))
        x = random.randint(turn1, turn2)
       

        return render_template('play_game.html', x=x, total_chances=total_chances)

    return render_template('play_game_form.html')

if __name__ == '_main_':
    app.run(debug=True)