from tkinter import *


class MainWindow:
    def __init__(self):

        self.colour = "#7aebff"
        self.frame = Tk()
        self.frame.config(bg="#7aebff")
        self.frame.title("Main Window GUI")
        self.frame.geometry("300x200")
        self.lbl_welcome = Label(text="Welcome", fg="white", bg="purple")
        self.lbl_welcome.pack()

        self.lbl_first_num = Label(text="Enter your first number")
        self.lbl_first_num.pack()

        self.txt_first_num = Entry()
        self.txt_first_num.pack()

        self.lbl_second_num = Label(text="Enter your second number")
        self.lbl_second_num.pack()
        self.txt_second_num = Entry()
        self.txt_second_num.pack()
        Button(text="Click for sum!", command=self.sum).pack()
        Button(text="Click for difference!", command=self.difference).pack()
        Button(text="Click for product!", command=self.product).pack()
        Button(text="Click for quotient!", command=self.quotient).pack()

        self.lbl_result = Label(text="Result = {}", fg="white", bg="red")
        self.lbl_result.pack()

    def sum(self):
        try:
            self.lbl_result.config(text=(int(self.txt_first_num.get()) + int(self.txt_second_num.get())))
        except ValueError:
            self.lbl_result.config(text="Please only input a number!")

    def difference(self):
        try:
            self.lbl_result.config(text=(int(self.txt_first_num.get()) - int(self.txt_second_num.get())))
        except:
            self.lbl_result.config(text="Please only input a number!")

    def product(self):
        try:
            self.lbl_result.config(text=(int(self.txt_first_num.get()) * int(self.txt_second_num.get())))
        except:
            self.lbl_result.config(text="Please only input a number!")

    def quotient(self):
        try:
            self.lbl_result.config(text=(int(self.txt_first_num.get()) / int(self.txt_second_num.get())))
        except:
            self.lbl_result.config(text="Please only input a number!")

    def run(self):
        self.frame.mainloop()


app = MainWindow()
app.run()
