import math

PLAYER = "X"
AI = "O"

def check_winner(board, player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win)

def minimax(board, depth, is_max):
    if check_winner(board, AI): return 10 - depth
    if check_winner(board, PLAYER): return depth - 10
    if " " not in board: return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                best = max(best, minimax(board, depth+1, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = PLAYER
                best = min(best, minimax(board, depth+1, True))
                board[i] = " "
        return best

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
