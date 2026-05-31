#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))

            # تحقق من الحدود
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move! Out of range.")
                continue

            # تحقق من الخانة
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player

            # تحقق فوز قبل تبديل اللاعب
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # تبديل اللاعب
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    tic_tac_toe()