import random

class OutOfRangeError(Exception):
    pass

class PlaceHaveInput(Exception):
    pass

def initialise_board():
    board = {}
    for i in range(1, 10):
        board[i] = " "
    return board

def print_board(board):
    print("+---+---+---+")
    print(f"| {board[1]} | {board[2]} | {board[3]} |")
    print("+---+---+---+")
    print(f"| {board[4]} | {board[5]} | {board[6]} |")
    print("+---+---+---+")
    print(f"| {board[7]} | {board[8]} | {board[9]} |")
    print("+---+---+---+")

def play(board, player, inp):
    board[inp] = player

def getinp(board):
    while True:
        try:
            inp = int(input("Enter your input (1-9): "))
            if inp > 9 or inp < 1:
                raise OutOfRangeError("Input must be between 1 and 9")
            if board[inp] != " ":
                raise PlaceHaveInput("Location already has an item")
            return inp
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        except OutOfRangeError as e:
            print(e)
        except PlaceHaveInput as e:
            print(e)

def get_ai_input(board):
    available_moves = [key for key, value in board.items() if value == " "]
    return random.choice(available_moves)

def check_win(board, player):
    win_conditions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def main():
    board = initialise_board()
    current_player = "X"
    moves = 0
    print_board(board)
    
    while moves < 9:
        if current_player == "X":
            inp = getinp(board)
        else:
            inp = get_ai_input(board)
            print(f"AI chooses position {inp}")
        
        play(board, current_player, inp)
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
        moves += 1
    
    print("It's a tie!")

if __name__ == "__main__":
    main()
