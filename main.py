import time as thread
import json
import ast

thread.sleep(2)

all_users = [{"username": 'admin', "password": "0"}]


# <Runtime functions>
def register_login_system():
    if not create_file():
        load_data()
    pass


def close_program():
    # goodbye output
    write_and_truncate_data()


def start_ui():
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Welcome to the login dashboard!!")
    print("To Login, Press 1...")
    print("To Register a New Account, Press 2...")
    print("To Delete Your Account, Press 3...")
    print("To Delete Your Account, Press 4...")
    print("To Exit, Press 99...")
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Written by Takao & Shreyas")

    u_choice = int(input("Please Select an Option: "))

    if u_choice == 1:
        start_authentication()
    elif u_choice == 2:
        print("Thank you for choosing to register!")
        start_registration()
    elif u_choice == 3:
        start_account_deletion()
        pass
    elif u_choice == 4:
        start_password_reset()
        pass
    elif u_choice == 5:
        pass
    elif u_choice == 6:
        pass
    elif u_choice == 99:
        close_program()


def start_authentication():
    username = input("Please enter your username: ")
    if is_username(username):

        for user in all_users:
            if user['username'].lower() == username.lower():
                if ask_for_password(username):
                    print("Welcome to the homepage! Here is a cookie 🍪")

    else:
        print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
        print("That user does not exist! If you would like to create an account press 3")
        thread.sleep(3)
        start_ui()


def start_registration():
    u_username = input("Please enter your desired username: ")

    validated = False

    while not validated:
        if not is_username(u_username):
            u_password = input("Please choose a password: ")
            password_callback = approve_password(u_password)

            if password_callback[0]:
                create_user(u_username, u_password)
                print(f"Your account with the username '{u_password.title()}' has now been created!")
            else:
                for i in range(len(password_callback)):
                    if i != 0:
                        print(password_callback[i])

        else:
            print("That username is already taken! Please try again")
            start_registration()


def start_account_deletion():
    u_username = input("Please enter the username of the account you'd like to delete: ")

    if is_username(u_username):
        if ask_for_password(u_username):
            thread.sleep(0.3)
            print("⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️")
            thread.sleep(0.3)
            print("IF YOUR ACCOUNT IS TERMINATED, THE INFORMATION ASSOCIATED CANNOT BE RECOVERED")
            print(f"PLEASE CONFIRM THE TERMINATION OF THE ACCOUNT {u_username} BY TYPING 'CONFIRM'")
            thread.sleep(0.3)
            print("⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️")
            thread.sleep(0.3)

            if input().__contains__("confirm"):
                remove_user(u_username)
            print("Account removed!")
            thread.sleep(2)
            start_ui()


def start_password_reset():
    u_user = input("Please enter your username: ")
    if is_username(u_user):

        current_password = all_users[u_user['username']]
        previous_password = input("Please enter your previous password: ")
        if previous_password:  # = 80% matching w/ actual password
            print("You may reset your password.")
            new_password = input("Please enter your new password: ")
            all_users["username", "password"] = u_user, new_password
        else:
            print("Sorry, we couldn't deem that you are the owner of the account.")

        u_user = input("Please enter your username: ")
        if is_username(u_user):
            current_pass = input("")

    else:
        print("That is not a valid username! Please try again...")
        start_password_reset()


def ask_for_password(user):
    authentication_tries = 0
    is_correct_pass = False

    while not is_correct_pass and authentication_tries < 3:
        password_to_match = input("Please enter your password: ")

        for looped_user in all_users:
            if looped_user['username'].lower() == user.lower():

                if looped_user['password'].lower() == password_to_match.lower():
                    return True
                else:
                    authentication_tries = authentication_tries + 1

                    if authentication_tries == 3:
                        print(
                            "You have been locked out of the login system for 1 (one) minute with three (3) incorrect tries "
                            "for authentication...")
                        thread.sleep(5)  # 5 seconds only for demonstration purposes
                        start_ui()
                    else:
                        print("Incorrect Password! Please try again:")


# <Back End Functions>
def create_user(username, password):
    new_user = {"username": username, "password": password}
    all_users.append(new_user)


def remove_user(user):
    for looped_user in all_users:
        if looped_user['username'].lower() == user.lower():
            all_users.remove(looped_user)


def is_username(parsed_username):
    for users in all_users:
        if users['username'] == parsed_username:
            return True
        else:
            return False


def approve_password(password_to_approve):
    special_symbols = ["\"", "!", "#", "$" "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">",
                       "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    val = [True]

    if len(password_to_approve) < 6:
        val[0] = False
        val.append("Length should be greater than 6 characters!")

    if len(password_to_approve) > 30:
        val[0] = False
        val.append("Length should be not be greater than 30 characters!")

    if not any(char.isdigit() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one numeral!")

    if not any(char.isupper() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one uppercase letter!")

    if not any(char.islower() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one lowercase letter!")

    if not any(char in special_symbols for char in password_to_approve):
        val[0] = False
        val.append("Password should contain at least one special character!")

    return val


# <File Management Functions>

def write_and_truncate_data():  # Write existing data to a file
    with open("account_data.txt", 'w') as file:
        json.dump(all_users, file)


def load_data():  # Load existing data to the dictionary
    try:
        with open("account_data.txt", "r") as file_in:
            global all_users
            all_users = ast.literal_eval(file_in.read())
    except SyntaxError:
        return


def create_file():
    #  Create file if not exists
    try:
        open("account_data.txt", "x")
        return True
    except FileExistsError:
        return False
        pass


# ---------------------------------------

register_login_system()
start_ui()

# Switch account
# Delete account
# Change password

