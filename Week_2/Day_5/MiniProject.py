# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
player = 'X' # X or O



def display_board():
    print("*****************")
    for row in board :
        print(f"*   {row[0]} | {row[1]} | {row[2]}   *")
        print("*  ---|---|---  *")
    print("*****************")

def player_input(player):
    allowed_input = ["1", "2", "3"]
    while True:
        row = input("Enter row(1-3): ")
        column  = input("Input column(1-3): ")
        if row in allowed_input and column in allowed_input:
            return {row: int(row), column: int(column)}


def check_win():
    pass

def play():
    winner_player = ''
    print("Welcome to TIC TAC TOE!")

    while not winner_player:
        display_board()
        print(f"Player {player}'s turn...")
        player_input(player)
        is_win = check_win()
    print('The game ends...')
    if winner_player == "tie":
        print("in a tie :(")
    else:
        print(f"And {winner_player} wins!!!")
        

