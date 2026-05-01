import math
board=["" for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i < 6:
            print("-----------")
    print("\n")
def check_winner(player):
    win_positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos in win_positions:
        if all(board[i]== player for i in pos):
            return True
    return False

def is_full():
    return "" not in board

def minimax(is_maximinzing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0
    if is_maximinzing:
        best_score=-math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                score=minimax(False)
                board[i]==" "
                best_score=max(score, best_score)
        return best_score
    else:
        best_score=math.inf
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                score=minimax(True)
                board[i]==" "
                best_score=max(score, best_score)
        return best_score

