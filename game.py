from flask import Flask, render_template
import random

app = Flask(__name__)

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user choice
@app.route('/play/<choice>')
def play(choice):
    result = determine_winner(choice)
    return f"Computer chose: {result}"

if __name__ == '__main__':
    app.run(debug=True)
