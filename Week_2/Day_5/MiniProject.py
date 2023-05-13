# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]




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
        if(row in allowed_input and column in allowed_input):
            return [int(row), int(column)]


def check_win():
    pass

def play():
    pass


