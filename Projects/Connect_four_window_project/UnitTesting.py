from tkinter import *

import pyautogui


class StartupWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("CONNECT FOUR")

        x = pyautogui.size()[0]  # get the width of the screen (automatically)
        y = pyautogui.size()[1]  # get the height of the screen (automatically)
        self.window.geometry('770x840+' + str(int(x / 2 - 385)) + '+' + str(int(y / 2 - 420)))
        self.window.configure(background='BLACK')

        self.player_one_name = ""
        self.player_two_name = ""

        Label(self.window, text="Welcome to Connect Four!", font="minecraftia 45", fg="white", bg="black").pack()
        Label(self.window, text="Coded by Shreyas A and Joonhee H in Python 3.9!", font="chalkduster 20",
              fg="white", bg="black").pack()
        Label(self.window, text="decxroption bruh", font="arial 20", fg="white", bg="blue").pack()

        Button(self.window, text="Start Game!", command=lambda: self.check_empty(), font="arial", fg="blue",
               bg="white").pack()
        Button(self.window, text="Directions", command=lambda: print("directuions"), font="arial", fg="blue",
               bg="white").pack()
        Button(self.window, text="About the Creators", command=lambda: print("abt"), font="arial", fg="blue",
               bg="white", ).pack()

        self.name_box_1 = Entry(self.window, font="arial", fg="blue", bg="white")
        self.name_box_2 = Entry(self.window, font="arial", fg="blue", bg="white")

        self.name_box_1.pack()
        self.name_box_2.pack()

    def check_empty(self):
        if str(self.name_box_1.get()).strip() == "" or str(self.name_box_2.get()).strip() == "":
            print("Please enter a name!")
        else:
            from Projects.Connect_four_window_project.TestingGameInstance import TestingGameInstance
            self.window.destroy()

            # TODO parse in players
            TestingGameInstance()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    StartupWindow().run()
