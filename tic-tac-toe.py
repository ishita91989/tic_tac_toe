import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    while True:
        print_board(board)

        if player == "X":
            row, col = map(int, input(f"Player {player}, enter row and column (e.g., 1 2): ").split())
        else:
            print(f"Computer {computer} is making a move...")
            row, col = computer_move(board)

        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = player
        else:
            print("That spot is already taken. Try again.")
            continue

        if check_win(board, player):
            print_board(board)
            if player == "X":
                print(f"Player {player} wins!")
            else:
                print(f"Computer {computer} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()