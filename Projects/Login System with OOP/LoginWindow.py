from tkinter import *
from OOP.User import *

def pack(pack):
    to_pack: Pack = pack
    to_pack.pack()


class LoginWindow:

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Welcome! Please login...")
        self.frame.geometry = "300x200"

        self.lbl_welcome1 = Label(text=" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
        pack(self.lbl_welcome1)

        self.lbl_welcome2 = Label(text="Welcome to https://creativelogins.com!")
        pack(self.lbl_welcome2)

        self.lbl_username = Label(text="Please enter your username:")
        self.input_username = Entry()


        pack(self.lbl_username)
        pack(self.input_username)

        self.lbl_password = Label(text="Please enter your password:")
        self.input_password = Entry()

        pack(self.lbl_password)
        pack(self.input_password)

        self.btn_proceed = Button(text="Login")
        self.lbl_status = Label(text="Login above.")

        pack(self.btn_proceed)
        pack(self.lbl_status)

    @staticmethod
    def run(self):
        self.frame.mainloop()

    # funion to add image to frame
    def add_image(self, image):
        self.image = PhotoImage(file=image)
        self.image_label = Label(image=self.image)
        self.image_label.pack()



class MainWindow:
    pass


app = LoginWindow()
app.add_image("peepolove.webp")
app.run()
