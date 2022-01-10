# Connect Four, By Joonhee & Shreyas; Coded in Python 3.9

import time  # import time variable (gives us the option to pause the thread)

yellow_piece = "🟡"  # player 1
red_piece = "🔴"  # player 2
empty_piece = "⚫"

board = [
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # a
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # b
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # c
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # d
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # e
    [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # f
]  # Initialises board object with multiple lists


def pre_start():
    print("Loading game...")
    time.sleep(1.5)

    print(
        "🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛")
    print(
        "██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗      ████████╗ █████╗         █████╗ ██╗   ██╗██████╗        ██████╗  █████╗ ███╗   ███╗███████╗")
    time.sleep(0.3)
    print(
        "██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝      ╚══██╔══╝██╔══██╗       ██╔══██╗██║   ██║██╔══██╗      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝")
    time.sleep(0.3)
    print(
        "╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗           ██║   ██║  ██║       ██║  ██║██║   ██║██████╔╝      ██║  ██╗ ███████║██╔████╔██║█████╗")
    time.sleep(0.3)
    print(
        " ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝           ██║   ██║  ██║       ██║  ██║██║   ██║██╔══██╗      ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝ ")
    time.sleep(0.3)
    print(
        " ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗         ██║   ╚█████╔╝       ╚█████╔╝╚██████╔╝██║  ██║      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗")
    time.sleep(0.3)
    print(
        "  ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝         ╚═╝    ╚════╝         ╚════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    print(
        "🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️")
    time.sleep(2)

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    print("Welcome to Connect Four, coded in Python 3.9 by Joonhee & Shreyas")  # Names as the creator
    time.sleep(4)
    print(
        "Each player will have a turn to drop a piece into a column of 7. A player must have 4 pieces in a row, either horizontally, diagonally, or vertically to win the game!")  # Directions
    time.sleep(5)
    print("There are two players required to play this game. Each player will either be given a 🟡 piece, or 🔴 piece")

    time.sleep(2)

    ask_for_ready()


def ask_for_ready():  # checking via input in both players are ready
    is_ready = input("Are both players ready to begin the game? (YES/NO) (Y/N) ")

    # is_ready, holds the string value that the player will enter

    if is_ready.lower().__contains__("y"):
        begin_game()
    elif is_ready.lower().__contains__("n"):
        print("Giving 10 seconds for preparation...")
        time.sleep(10)
        ask_for_ready()
    else:
        print("Since you did not answer yes, giving 10 seconds for preparation...")
        time.sleep(10)

        ask_for_ready()


def begin_game():  # Main game function (brain of the game)

    # Variables used for the two players. These will be accessed through the game,
    # so it is important to define them here
    player_one = input(f"Please state the name of player 1 '{yellow_piece}': ")
    player_two = input(f"Please state the name of player 2 '{red_piece}': ")

    print_game_board()
    player_choosing = 0

    # While loop to decide who is playing
    # even number = player one
    # odd number = player two

    while player_choosing < 42:
        if player_choosing % 2 == 0:
            input_column = get_correct_integer(player_one)

            if add_piece(yellow_piece, input_column) == 0:
                player_choosing = player_choosing - 1

        elif player_choosing % 2 == 1:
            input_column = get_correct_integer(player_two)

            if add_piece(red_piece, input_column) == 0:
                player_choosing = player_choosing - 1
        if check_board(player_one, player_two) != "":
            final_winner = check_board(player_one, player_two)
            complete_game(final_winner)
            break
        player_choosing = player_choosing + 1
    if player_choosing == 42:
        print("It's a tie!")
        complete_game("")


def get_correct_integer(player_name):
    # Essentially a try and catch, to make sure that the integer is a valid number
    # and meets the game's requirements. (1-7, not a string)
    try:
        chosen_column = int(
            input(f"{player_name.title()}, please choose a column between 1 and 7. (1, 2, 3, 4, 5, 6, 7): "))

        if chosen_column > 7 or chosen_column < 1:
            print("That is not a number in the range of 1-7")

            return get_correct_integer(player_name)
        else:
            return chosen_column
    except ValueError:
        print("That is not a valid number!")
        return get_correct_integer(player_name)

    # recursive function until a valid integer is returned


def add_piece(piece, column):
    row_counter = 5
    while row_counter >= 0:
        if board[row_counter][column - 1].__contains__(empty_piece):  # check where there are empty spaces in the column
            board[row_counter][column - 1] = piece
            print_game_board()
            break
        row_counter = row_counter - 1

    if row_counter < 0:  # If the column is already full
        print("\n\n\nSorry, that row is already full! Please pick another row\n\n\n")
        return 0


def print_game_board():
    print("")
    for rows in board:
        print("", *rows, "", sep=" │ ")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("   1    2    3   4    5    6    7")
    print(" ━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━")

    # simply prints the game board


# check a player has won in any directions
def check_board(player_one, player_two):
    # checking verticals
    winner = ''
    for row in range(3, 6):
        for column in range(7):
            piece = board[row][column]
            if piece == board[row - 1][column] and piece == board[row - 2][column] and piece == board[row - 3][column]:
                if piece == yellow_piece:
                    winner = player_one
                if piece == red_piece:
                    winner = player_two
    # checking horizontals
    for column in range(4):
        for row in range(6):
            piece = board[row][column]
            if piece == board[row][column + 1] and piece == board[row][column + 2] and piece == board[row][column + 3]:
                if piece == yellow_piece:
                    winner = player_one
                if piece == red_piece:
                    winner = player_two
    # checking diagonals heading bottom right
    for column in range(4):
        for row in range(3):
            piece = board[row][column]
            if piece == board[row + 1][column + 1] and piece == board[row + 2][column + 2] and piece == board[row + 3][
                column + 3]:
                if piece == yellow_piece:
                    winner = player_one
                if piece == red_piece:
                    winner = player_two
    # checking diagonals heading bottom left
    for column in range(3, 7):
        for row in range(3):
            piece = board[row][column]
            if piece == board[row + 1][column - 1] and piece == board[row + 2][column - 2] and piece == board[row + 3][
                column - 3]:
                if piece == yellow_piece:
                    winner = player_one
                if piece == red_piece:
                    winner = player_two
    return winner


def complete_game(winner):
    # Console print decorations

    print("🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩🟦🟪⬛🟥")
    print(" ██████╗  █████╗ ███╗   ███╗███████╗      █████╗ ██╗   ██╗███████╗██████╗")
    time.sleep(0.3)
    print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝     ██╔══██╗██║   ██║██╔════╝██╔══██╗")
    time.sleep(0.3)
    print("██║  ██╗ ███████║██╔████╔██║█████╗       ██║  ██║╚██╗ ██╔╝█████╗  ██████╔╝")
    time.sleep(0.3)
    print("██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝       ██║  ██║ ╚████╔╝ ██╔══╝  ██╔══██╗")
    time.sleep(0.3)
    print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗     ╚█████╔╝  ╚██╔╝  ███████╗██║  ██║")
    time.sleep(0.3)
    print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ╚════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝")
    time.sleep(0.3)
    print("🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩🟦🟪⬛🟥")

    if winner != "":
        print(f"\n\n✨{winner} has won the game!")

    # Asking the user to play again
    is_ready = input("Would you like to play again! (YES/NO) (Y/N) ")
    if is_ready.lower().__contains__("y"):

        # Clearing the board object for a new game
        for row in range(6):
            for column in range(7):
                board[row][column] = empty_piece

        ask_for_ready()

    elif is_ready.lower().__contains__("n"):
        print(f"If you enjoyed the game, plspls give us a 7!")

        time.sleep(2)
        print(" ██████╗  █████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗███████╗")
        time.sleep(0.3)
        print("██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝")
        time.sleep(0.3)
        print("██║  ██╗ ██║  ██║██║  ██║██║  ██║██████╦╝ ╚████╔╝ █████╗  ")
        time.sleep(0.3)
        print("██║  ╚██╗██║  ██║██║  ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ")
        time.sleep(0.3)
        print("╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝   ██║   ███████╗")
        time.sleep(0.3)
        print(" ╚═════╝  ╚════╝  ╚════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝")


pre_start()

# Sources:
# https://stackoverflow.com/questions/4664345/how-do-i-set-a-top-level-variable-in-python
# https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
