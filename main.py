import ast
import pickle
import ast

from OOP.User import User

# with open("account_data.txt", 'wb') as file:
#     pickle.dump(User("shreyas", "ayyengar", 15, "UK", "verification_question", False), file)
#
# with open('account_data.txt', 'rb') as file:
#     strings_of_bytes = ast.literal_eval(str(file.read()))
#     print(strings_of_bytes)
#
#     data: User = pickle.loads(bytes(ast.literal_eval(strings_of_bytes)))
# # print(data.get_username())

if __name__ == "__main__":
    from tkinter import Tk, Label
    import tkinter.font

    names = []

    window = Tk()
    for name in sorted(tkinter.font.families()):
        names.append(name)

    # loop through names


    # 40, 70 100 = minecraft, 130,

    # chalkduster
    # minecraftia
    # krungthep
    for i in range(105, len(names)):
        print(names[i].replace(" ", "-"))
        Label(window, text="Hello, world!", font=str(names[i]).replace(" ", "-")).pack()

    window.mainloop()
