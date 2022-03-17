# Connect Four, By Joonhee & Shreyas; Coded in Python 3.9

from Projects.Connect_four_window_project.ConnectWindow import ConnectWindow, StartupWindow
from Projects.Connect_four_window_project.GamePiece import GamePiece


# TestingGameInstance
class TestingGameInstance:

    def __init__(self, player_one, player_two):
        self.yellow_piece = "yellow"  # player 1
        self.red_piece = "red"  # player 2
        self.empty_piece = "black"

        self.isPlayerOne = True

        # TODO apply player names
        self.player_one = player_one
        self.player_two = player_two

        self.board_dictionary = {
            # 1 to 42 set as black empty pieces
            0: GamePiece(self.empty_piece, 0),
            2: GamePiece(self.empty_piece, 2),
            3: GamePiece(self.empty_piece, 3),
            4: GamePiece(self.empty_piece, 4),
            1: GamePiece(self.empty_piece, 1),
            5: GamePiece(self.empty_piece, 5),
            6: GamePiece(self.empty_piece, 6),
            7: GamePiece(self.empty_piece, 7),
            8: GamePiece(self.empty_piece, 8),
            9: GamePiece(self.empty_piece, 9),
            10: GamePiece(self.empty_piece, 10),
            11: GamePiece(self.empty_piece, 11),
            12: GamePiece(self.empty_piece, 12),
            13: GamePiece(self.empty_piece, 13),
            14: GamePiece(self.empty_piece, 14),
            15: GamePiece(self.empty_piece, 15),
            16: GamePiece(self.empty_piece, 16),
            17: GamePiece(self.empty_piece, 17),
            18: GamePiece(self.empty_piece, 18),
            19: GamePiece(self.empty_piece, 19),
            20: GamePiece(self.empty_piece, 20),
            21: GamePiece(self.empty_piece, 21),
            22: GamePiece(self.empty_piece, 22),
            23: GamePiece(self.empty_piece, 23),
            24: GamePiece(self.empty_piece, 24),
            25: GamePiece(self.empty_piece, 25),
            26: GamePiece(self.empty_piece, 26),
            27: GamePiece(self.empty_piece, 27),
            28: GamePiece(self.empty_piece, 28),
            29: GamePiece(self.empty_piece, 29),
            30: GamePiece(self.empty_piece, 30),
            31: GamePiece(self.empty_piece, 31),
            32: GamePiece(self.empty_piece, 32),
            33: GamePiece(self.empty_piece, 33),
            34: GamePiece(self.empty_piece, 34),
            35: GamePiece(self.empty_piece, 35),
            36: GamePiece(self.empty_piece, 36),
            37: GamePiece(self.empty_piece, 37),
            38: GamePiece(self.empty_piece, 38),
            39: GamePiece(self.empty_piece, 39),
            40: GamePiece(self.empty_piece, 40),
            41: GamePiece(self.empty_piece, 41)
        }

        # [
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # a
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # b
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # c
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # d
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # e
        #     [empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece, empty_piece],  # f
        # ]  # Initialises board object with multiple lists

        self.board_gui = ConnectWindow(self)

    def pre_start(self):
        self.board_gui.startup_window = StartupWindow(self)
        pass

    def begin_game(self):  # Main game function (brain of the game)

        # Begin game GUI + Name Inputs

        self.board_gui.show_initial_start()

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

    def add_piece(self, piece, column):

        # loop thru 1 --> 6, * 7 get the piece, if its empty, add the piece
        if self.board_dictionary[column].get_color() != self.empty_piece:

            return False

        row_counter = 1

        while row_counter <= 5:
            if self.board_dictionary[row_counter * 7 + column].get_color() != self.empty_piece:
                self.board_dictionary[row_counter * 7 + column - 7].set_color(piece)
                break

            row_counter = row_counter + 1

            if row_counter == 6:
                self.board_dictionary[35 + column].set_color(piece)
                break

        self.isPlayerOne = not self.isPlayerOne

        self.board_gui.switch_instruction()
        self.board_gui.draw_board()
        return True

    def show_game_board(self):
        # Gets the GUI manager and draws the board
        self.board_gui.draw_board()

    def check_board(self, player_one, player_two):

        # checking verticals
        winner = ''
        for row in range(0, 3):
            for column in range(7):
                piece = self.board_dictionary[row * 7 + column].get_color()
                if piece == self.board_dictionary[row * 7 + column + 7].get_color() and piece == self.board_dictionary[
                    row * 7 + column + 14].get_color():
                    if piece == self.board_dictionary[row * 7 + column + 21].get_color():
                        if piece == self.yellow_piece:
                            winner = player_two
                        if piece == self.red_piece:
                            winner = player_one
        # checking horizontals
        for row in range(6):
            for column in range(4):
                piece = self.board_dictionary[row * 7 + column].get_color()
                if piece == self.board_dictionary[row * 7 + column + 1].get_color() and piece == self.board_dictionary[
                    row * 7 + column + 2].get_color():
                    if piece == self.board_dictionary[row * 7 + column + 3].get_color():
                        if piece == self.yellow_piece:
                            winner = player_two
                        if piece == self.red_piece:
                            winner = player_one

        # checking diagonals heading bottom right
        for row in range(3):
            for column in range(4):
                piece = self.board_dictionary[row * 7 + column].get_color()
                if piece == self.board_dictionary[row * 7 + column + 8].get_color() and piece == self.board_dictionary[
                    row * 7 + column + 16].get_color():
                    if piece == self.board_dictionary[row * 7 + column + 24].get_color():
                        if piece == self.yellow_piece:
                            winner = player_two
                        if piece == self.red_piece:
                            winner = player_one
        # checking diagonals heading bottom left
        for column in range(3, 7):
            for row in range(3):
                piece = self.board_dictionary[row * 7 + column].get_color()
                if piece == self.board_dictionary[row * 7 + column + 6].get_color() and piece == self.board_dictionary[row * 7 + column + 12].get_color():
                    if piece == self.board_dictionary[row * 7 + column + 18].get_color():
                        if piece == self.yellow_piece:
                            winner = player_one
                        if piece == self.red_piece:
                            winner = player_two
        return winner + "<- WINNER"

    def complete_game(self, winner):
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

        # check a player has won in any directions

    # Getters -------- (supplies field variables that are assigned with this object)

    def get_board_dictionary(self):
        return self.board_dictionary

    def get_yellow_piece(self):
        return self.yellow_piece

    def get_red_piece(self):
        return self.red_piece

    def get_black_piece(self):
        return self.empty_piece

    def get_playing(self):
        return self.isPlayerOne

    def get_playing_name(self):
        if self.get_playing():
            return str(self.player_one)
        else:
            return str(self.player_two)

# Sources:
# https://stackoverflow.com/questions/4664345/how-do-i-set-a-top-level-variable-in-python
# https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
#
# game_instance = TestingGameInstance()
# game_instance.pre_start()
