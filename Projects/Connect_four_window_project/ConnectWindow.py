import time
from tkinter import *
import time as thread

import pyautogui
from playsound import playsound


def play_game_sound(file_name):
    playsound(file_name, block=False)
    # WE HAVE TO USE "block=False" FOR PLAYING SOUNDS, OTHERWISE IT WILL PAUSE THE GUI
    # FOR THE TIME THAT THE SOUND IS PLAYING

    # This is called **concurrency** and is a way to handle multiple processes at the same time

class ConnectWindow(Frame):

    # pass in gameinstance
    def __init__(self, game_instance):

        super().__init__()

        # We need a running instance of the game in order for our GUI to pull data from
        self.game_instance = game_instance

        self.init_board_grid()
        self.drop_buttons = [
            Button(self, text="Drop Here", command=lambda: self.drop_piece(0), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(1), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(2), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(3), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(4), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(5), padx=10, pady=10),
            Button(self, text="Drop Here", command=lambda: self.drop_piece(6), padx=10, pady=10)
        ]
        self.init_buttons()

        self.title_instruction = Label(self, text=f"Welcome to Connect Four!\n {game_instance.get_playing_name()}'s turn!", font="Copperplate 40")
        self.title_instruction.place(x=100, y=30)

        # Create two images for the red and yellow pieces
        self.red_piece_img = PhotoImage(file="/Users/ShreyasSrinivasAyyengar/JetBrains/PycharmProjects/ComputerScience/Projects/assets/imgs/red_circle.png")
        self.yellow_piece_img = PhotoImage(file="/Users/ShreyasSrinivasAyyengar/JetBrains/PycharmProjects/ComputerScience/Projects/assets/imgs/yellow_circle.png")

        play_game_sound("/Users/ShreyasSrinivasAyyengar/JetBrains/PycharmProjects/ComputerScience/Projects/assets/sounds/kerban_dance.mp3")
        self.master.bind('<Button>', self.motion)

    def init_board_grid(self):
        x = pyautogui.size()[0]
        y = pyautogui.size()[1]
        self.master.title("Python Connect Four")
        self.master.geometry('770x840+' + str(int(x / 2 - 385)) + '+' + str(int(y / 2 - 420)))
        # self.master.resizable(width=False, height=False)
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(110, 180, 110, 840)
        canvas.create_line(220, 180, 220, 840)
        canvas.create_line(330, 180, 330, 840)
        canvas.create_line(440, 180, 440, 840)
        canvas.create_line(550, 180, 550, 840)
        canvas.create_line(660, 180, 660, 840)
        canvas.create_line(0, 180, 770, 180)
        canvas.create_line(0, 290, 770, 290)
        canvas.create_line(0, 400, 770, 400)
        canvas.create_line(0, 510, 770, 510)
        canvas.create_line(0, 620, 770, 620)
        canvas.create_line(0, 730, 770, 730)
        canvas.pack(fill=BOTH, expand=1)

    def init_buttons(self):
        for i in range(len(self.drop_buttons)):
            self.drop_buttons[i].place(x=(110 * i) + 12, y=117)

    def drop_piece(self, column):

        should_play_sound = False
        if self.game_instance.get_playing():
            should_play_sound = self.game_instance.add_piece("red", column)
        else:
            should_play_sound = self.game_instance.add_piece("yellow", column)

        if should_play_sound:
            play_game_sound("/Users/ShreyasSrinivasAyyengar/JetBrains/PycharmProjects/ComputerScience/Projects/assets/sounds/piece_pop.mp3")

    def draw_board(self):
        for column in range(7):
            for row in range(6):

                if self.game_instance.get_board_dictionary()[row * 7 + column].get_color() == "red":
                    lbl_red = Label(self, image=self.red_piece_img, width=80, height=80)
                    lbl_red.place(x=12.5 + 110 * column, y=193 + 110 * row)
                    # self.lbl_red.place(x=7, y=)
                elif self.game_instance.get_board_dictionary()[row * 7 + column].get_color() == "yellow":
                    lbl_yellow = Label(self, image=self.yellow_piece_img, width=80, height=80)
                    lbl_yellow.place(x=12.5 + 110 * column, y=193 + 110 * row)

    def switch_instruction(self):
        self.title_instruction.destroy()
        if self.game_instance.get_playing():
            self.title_instruction = Label(self, text=f"Welcome to Connect Four!\n {self.game_instance.get_playing_name()}'s turn!", font="Copperplate 40", fg="red")
            for button in self.drop_buttons:
                button.config(fg="red")

        else:
            self.title_instruction = Label(self, text=f"Welcome to Connect Four!\n {self.game_instance.get_playing_name()}'s turn!", font="Copperplate 40", fg="#b8a800")
            for button in self.drop_buttons:
                button.config(fg="#b8a800")
        self.title_instruction.place(x=100, y=30)

    def motion(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))


class StartupWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("CONNECT FOUR")

        x = pyautogui.size()[0]  # get the width of the screen (automatically)
        y = pyautogui.size()[1]  # get the height of the screen (automatically)

        # TODO expand to width = 1070 --> adjust params
        self.window.geometry('770x840+' + str(int(x / 2 - 385)) + '+' + str(int(y / 2 - 420)))
        self.window.configure(background='#2d3b4d')

        self.player_one_name = ""
        self.player_two_name = ""

        Label(self.window, text="🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴", font="minecraftia 30", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="Welcome to Connect Four!", font="minecraftia 30", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="Coded by Shreyas A and Joonhee H in Python 3.9!\n", font="chalkduster 25", fg="white", bg="#2d3b4d").pack()

        Label(self.window,
              text="Connect Four is a classic game, wherein two players compete to \nget FOUR pieces in a row, diagonally, horizontally, or vertically!",
              font="krungthep 20",
              fg="white",
              bg="#6d9eab"
              ).pack()

        self.instruction_lbl = Label(self.window, text="\nEnter your names below and click 'Start Game' to begin!", font="minecraftia 20", fg="white", bg="#2d3b4d")
        self.instruction_lbl.pack()

        Button(self.window, text="Start Game!", command=lambda: self.check_empty(), font="chalkduster 30", fg="#2d3b4d", bg="#2d3b4d").place(x=282.5, y=460)
        Button(self.window, text="Directions", command=lambda: DirectionsWindow(), font="chalkduster 20", fg="#2d3b4d", bg="#2d3b4d").place(x=508.5, y=465)
        Button(self.window, text="About the Creators", command=lambda: print("abt"), font="chalkduster 17", fg="#2d3b4d", bg="#2d3b4d").place(x=80, y=467)

        Label(self.window, text="Player 1: ", font="chalkduster 25", fg="white", bg="#2d3b4d").place(x=105, y=365)
        self.name_box_1 = Entry(self.window, font="krungthep 20", fg="#b80202", bg="gray")

        Label(self.window, text="Player 2: ", font="chalkduster 25", fg="white", bg="#2d3b4d").place(x=105, y=405)
        self.name_box_2 = Entry(self.window, font="krungthep 20", fg="#cfc91d", bg="gray")

        self.name_box_1.pack()
        self.name_box_2.pack()

        self.play_game_sound("/Users/ShreyasSrinivasAyyengar/JetBrains/PycharmProjects/ComputerScience/Projects/assets/sounds/heaven_lobby.mp3")

        self.window.bind('<Button>', self.motion)

    def play_game_sound(self, file_name):
        playsound(file_name, block=False)

    def check_empty(self):
        if str(self.name_box_1.get()).strip() == "" or str(self.name_box_2.get()).strip() == "":
            print("Please enter a name!")
        else:
            from Projects.Connect_four_window_project.TestingGameInstance import TestingGameInstance
            # TODO parse in players
            name1 = str(self.name_box_1.get())
            name2 = str(self.name_box_2.get())
            self.window.destroy()
            TestingGameInstance(name1, name2)

            del StartupWindow

    # Debug exact coords of mouse
    def motion(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

    def run(self):
        self.window.mainloop()


class DirectionsWindow:
    # Create smaller directions window (with text and close button)
    def __init__(self):
        self.window = Tk()
        self.window.title("CONNECT FOUR DIRECTIONS")
        self.window.geometry('570x640')
        self.window.configure(background='#2d3b4d')

        Label(self.window, text="🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴", font="minecraftia 30", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="Directions:", font="minecraftia 30", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="1. Click on the 'drop here' button to place your piece.\n", font="chalkduster 20", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="2. The first player to get four pieces in a row wins!\n (either diagonally, vertically, horizontally)\n", font="chalkduster 20", fg="white",
              bg="#2d3b4d").pack()
        Label(self.window, text="3. The game ends when the board is full or a player wins!\n", font="chalkduster 20", fg="white", bg="#2d3b4d").pack()
        Label(self.window, text="4. The game is a drawed if no player wins!\n", font="chalkduster 20", fg="white", bg="#2d3b4d").pack()

    pass


class AboutAuthorsWindow:
    # Create smaller window with info about the authors
    pass


if __name__ == '__main__':
    StartupWindow().run()
