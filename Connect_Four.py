import time

yellow_piece = "🟡"  # player 1
red_piece = "🔴"  # player 2
empty = "⚫"

board = [
    [empty, empty, empty, empty, empty, empty, empty],  # a
    [empty, empty, empty, empty, empty, empty, empty],  # b
    [empty, empty, empty, empty, empty, empty, empty],  # c
    [empty, empty, empty, empty, empty, empty, empty],  # d
    [empty, empty, empty, empty, empty, empty, empty],  # e
    [empty, empty, empty, empty, empty, empty, empty],  # f
]


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

    print("Welcome to Connect Four, coded in Python 3.9 by Joonhee & Shreyas")
    time.sleep(4)
    print(
        "Each player will have a turn to drop a piece into a column of 7. A player must have 4 pieces in a row, either horizontally, diagonally, or vertically to win the game!")
    time.sleep(5)
    print("There are two players required to play this game. Each player will either be given a 🟡 piece, or 🔴 piece")

    time.sleep(2)

    ask_for_ready()


def ask_for_ready():
    ready = input("Are both players ready to begin the game? (YES/NO) (Y/N) ")
    if ready.lower().__contains__("y"):
        begin_game()
    elif ready.lower().__contains__("n"):
        print("Giving 10 seconds for preparation...")
        time.sleep(10)
        ask_for_ready()
    else:
        print("Since you did not answer yes, giving 10 seconds for preparation...")
        time.sleep(10)

        ask_for_ready()


def begin_game():
    player_one = input(f"Please state the name of player 1 '{yellow_piece}': ")
    player_two = input(f"Please state the name of player 2 '{red_piece}': ")

    print_game_board()
    i = 0
    while i < 43:
        if i % 2 == 0:
            input_column = get_correct_integer(player_one)

            if add_piece(yellow_piece, input_column) == 0:
                i = i - 1

        elif i % 2 == 1:
            input_column = get_correct_integer(player_two)

            if add_piece(red_piece, input_column) == 0:
                i = i - 1
        if check_board(player_one, player_two) != "":
            final_winner = check_board(player_one, player_two)
            complete_game(final_winner)
            break
        i = i + 1


def get_correct_integer(player_name):
    try:
        num = int(input(f"{player_name.title()}, please choose a column between 1 and 7. (1, 2, 3, 4, 5, 6, 7): "))

        if num > 7 or num < 1:
            print("That is not a number in the range of 1-7")

            return get_correct_integer(player_name)
        else:
            return num
    except ValueError:
        print("That is not a valid number!")
        return get_correct_integer(player_name)


def print_game_board():
    print("")
    for rows in board:
        print("", *rows, "", sep=" │ ")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("   1    2    3   4    5    6    7")
    print(" ━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━")


def add_piece(piece, number):
    k = 5
    while k >= 0:
        if board[k][number - 1].__contains__(empty):
            board[k][number - 1] = piece
            print_game_board()
            break
        k = k - 1

    if k < 0:
        print("\n\n\nSorry, that row is already full! Please pick another row\n\n\n")
        return 0


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

    print(f"\n\n✨{winner} has won the game!✨")

    ready = input("Would you like to play again! (YES/NO) (Y/N) ")
    if ready.lower().__contains__("y"):

        for i in range(6):
            for j in range(7):
                board[i][j] = empty

        ask_for_ready()

    elif ready.lower().__contains__("n"):
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


begin_game()
