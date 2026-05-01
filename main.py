import math
import random

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i < 6:
            print("-----------")
    print("\n")

def check_winner(player):
    win_positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_full():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    if random.random() < 0.3:
        available_moves = [i for i, x in enumerate(board) if x == " "]
        if available_moves:
            move = random.choice(available_moves)
            board[move] = "O"
            return


    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move != -1:
        board[move] = "O"


def player_move():
        move = int(input("Enter position (0-8): "))
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "X"
        else:
            print("Invalid move!")
            player_move()


while True:
    print_board()
    player_move()


    if check_winner("X"):
        print_board()
        print("You win!")
        break


    if is_full():
        print_board()
        print("Draw!")
        break


    ai_move()


    if check_winner("O"):
        print_board()
        print("AI wins!")
        break


    if is_full():
        print_board()
        print("Draw!")
        break