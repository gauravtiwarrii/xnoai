from flask import Flask, render_template, request, jsonify
from minimax import best_move, check_winner

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ai_move", methods=["POST"])
def ai_move():
    data = request.get_json()
    board = data.get("board")
    move = best_move(board)
    board[move] = "O"
    winner = check_winner(board, "O")
    return jsonify({"board": board, "move": move, "winner": winner})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
