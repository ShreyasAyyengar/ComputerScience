# CreativeLogins - Written By Shreyas * Takao (Py-3.9)
# Git - https://github.com/ShreyasAyyengar/ComputerScience/blob/master/Projects/Login_System.py


# Import all relevant libraries
import datetime
import time as thread
import json
import ast
import re
from difflib import SequenceMatcher

from datetime import date
import random

# Define main dictionary
from OOP.User import User

all_users = [
    User("shreyas", "ayyengar", 16, "United Kingdom")
]

# <Runtime functions>

# Does not do any heavy: calculations, searching, data reading/writing
# Handles frontend input/output

def register_login_system():
    append_admin()  # Adds an admin user to the all users list

    if not create_file():
        load_data()


def open_main_ui():

    # TODO: replace with GUI
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Welcome to https://creativelogins.com!")
    print()
    print("To Login, Press 1...")
    print("To Register a New Account, Press 2...")
    print("To Delete Your Account, Press 3...")
    print("To Reset Your Account's Password, Press 4...")
    print()
    print("To Exit, Press 99...")
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Written by Takao & Shreyas")

    try:
        u_choice = int(input("Please Select an Option: "))

        if u_choice == 1:
            start_authentication()

        elif u_choice == 2:
            print("Thank you for choosing to register!")
            start_registration()

        elif u_choice == 3:
            start_account_deletion()

        elif u_choice == 4:
            start_password_reset()

        elif u_choice == 99:
            close_program()

    except ValueError:
        print("That was not a valid option!")
        thread.sleep(1.5)
        open_main_ui()


def start_authentication():
    username = input("Please enter your username: ")
    if is_username(username):

        for user in all_users:  # Loop through all registered users
            if user['username'].lower() == username.lower():
                if ask_for_password(username):
                    print("Login successful!")
                    after_login_ui()

    else:
        print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
        print("That user does not exist! If you would like to create an account press 2")
        thread.sleep(3)  # Pause the code for visual effect
        open_main_ui()


def ask_for_password(user):
    authentication_tries = 0  # Counter for how many failed attempts
    is_correct_pass = False  # Simple flag boolean used for while loop control statement

    while not is_correct_pass and authentication_tries < 3:
        password_to_match = input("Please enter your password: ")

        for looped_user in all_users:
            if looped_user['username'].lower() == user.lower():

                if looped_user['password'].lower() == password_to_match.lower():
                    return True  # Return that the password they entered was the correct one!
                else:
                    authentication_tries = authentication_tries + 1  # Add a failed attempt

                    if authentication_tries == 3:  # Reach attempt limit
                        print(
                            "You have been locked out of the login system for 1 (one) minute with three (3) incorrect tries "
                            "for authentication...")
                        thread.sleep(5)  # 5 seconds only for demonstration purposes
                        open_main_ui()  # Opens back the main UI
                    else:
                        print("Incorrect Password! Please try again:")


def start_registration():
    u_username = input("Please enter your desired username: ")

    validated = False

    # Flag booleans for while statements

    email_validated = False
    age_validated = False

    while not validated:
        if not is_username(u_username):

            u_password = input("Please choose a password: ")
            password_callback = approve_password(u_password)

            # A function callback may look like this:
            # [False, 'Length should be greater than 6 characters!',
            # 'Password should have at least one numeral!', 'Password should have at least one uppercase letter!',
            # 'Password should contain at least one special character!']

            if password_callback[0]:  # This will access the first index in the callback either 'True' or 'False'

                while not email_validated:
                    u_email = input("Please enter a valid email address that belongs to you: ")
                    email_callback = approve_email(u_email)

                    if email_callback[0]:

                        while not age_validated:
                            u_age = input("Please enter your age: ")
                            age_callback = is_valid_age(u_age)

                            if age_callback[0]:
                                create_user(u_username, u_password, u_age, u_email)
                                validated = True
                                print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
                                print(f"Your account with the username '{u_username.title()}' has now been created!")
                                print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
                                thread.sleep(2)
                                open_main_ui()
                                break
                            else:
                                print("Failed: " + age_callback[1] + ".")
                                thread.sleep(2)
                                open_main_ui()
                                break
                    else:
                        print("That is not a valid email address, please try again!")

            else:
                for i in range(len(password_callback)):  # Print all reasons for failed password creation
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
            thread.sleep(0.3)  # Animations
            print("IF YOUR ACCOUNT IS TERMINATED, THE INFORMATION ASSOCIATED CANNOT BE RECOVERED")
            print(f"PLEASE CONFIRM THE TERMINATION OF THE ACCOUNT {u_username} BY TYPING 'CONFIRM'")
            thread.sleep(0.3)  # Animations
            print("⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️")
            thread.sleep(0.3)

            if input().lower().__contains__("confirm"):
                remove_user(u_username)
            print("Account removed!")
            thread.sleep(2)
            open_main_ui()


def start_password_reset():
    u_user = input("Please enter your username: ")

    valid_pass = False  # Flag boolean for while loop, stays false until the new password is valid

    if is_username(u_user):

        for looped_user in all_users:
            if looped_user['username'].lower() == u_user.lower():

                current_password = looped_user['password'].lower()
                previous_password = input("Please enter your previous password as best as you can remember: ")

                #  Uses a SequenceMatcher to determine character accuracy (between 0.0 and 1.0)
                percentage_match = SequenceMatcher(None, current_password, previous_password).ratio()
                print(percentage_match)

                if percentage_match >= 0.8:  # Deemed to have greate accuracy
                    print("The password you entered was very similar to your current password. Proceeding to "
                          "password reset...")
                    thread.sleep(1)

                    while not valid_pass:
                        new_pass = input("Please choose a new password: ")
                        password_callback = approve_password(new_pass)

                        if password_callback[0]:
                            print(f"Success! Your password for the username {u_user} has been updated!")
                            looped_user['password'] = new_pass  # Set new password in dictionary
                            thread.sleep(1)
                            after_login_ui()
                            break

                        else:
                            for i in range(len(password_callback)):
                                if i != 0:
                                    print(password_callback[i])

                else:  # Deemed not to be accurate
                    print("Sorry, we couldn't deem that you are the owner of the account.")
                    thread.sleep(1)
                    open_main_ui()
    else:
        print("That username does not exist! Please try again...")
        start_password_reset()


def after_login_ui():
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Welcome to the Dashboard! Here is some information:")
    print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))
    print("Today's Date:", date.today())
    print()
    print("To Logout, Press 1...")
    print("To Delete Your Account Press 2...")
    print("To Change Your Password Press 3...")
    print("To Play Rock Paper Scissors, Press 4")
    print()
    print("To View All Accounts Registered, Press 5... (Admin)")
    print("To Delete All Accounts Registered, Press 6... (Admin)")
    print()
    print("To Exit, Press 99...")
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")

    u_choice = int(input("Please Select an Option: "))

    if u_choice == 1:
        open_main_ui()
    elif u_choice == 2:
        start_account_deletion()
    elif u_choice == 3:
        start_password_reset()
    elif u_choice == 4:
        play_RPS()

    elif u_choice == 5:
        print("This can only be done by an administrator! Please enter an administrator password: ")
        if ask_for_password('admin'):
            for user in all_users:
                print(user)
        after_login_ui()

    elif u_choice == 6:
        print("This can only be done by an administrator! Please enter an administrator password: ")
        if ask_for_password('admin'):
            print("WARNING ⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️ WARNING")
            print("YOU ARE ABOUT TO DELETE ALL USER DATA FOR 'https://creativelogins.com. THIS CANNOT BE UNDONE.")
            print("WARNING ⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️⛔︎⚠️ WARNING")
            confirm = input("TO PROCEED, PLEASE TYPE 'CONFIRM': ")

            if confirm.__contains__("confirm"):
                all_users.clear()
                append_admin()
            else:
                print("Failed to gain confirmation; Aborting....")

        open_main_ui()
    elif u_choice == 99:
        close_program()


def play_RPS():
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            after_login_ui()
            break


def close_program():
    # Goodbye output and program disabling

    thread.sleep(1.5)
    print(" ██████╗  █████╗  █████╗ ██████╗ ██████╗ ██╗   ██╗███████╗")
    thread.sleep(0.25)
    print("██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝")
    thread.sleep(0.25)
    print("██║  ██╗ ██║  ██║██║  ██║██║  ██║██████╦╝ ╚████╔╝ █████╗  ")
    thread.sleep(0.25)
    print("██║  ╚██╗██║  ██║██║  ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ")
    thread.sleep(0.3)
    print("╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝   ██║   ███████╗")
    thread.sleep(0.25)
    print(" ╚═════╝  ╚════╝  ╚════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝")

    write_and_truncate_data()


# <Back End Functions>
def create_user(username, password, age, email):
    #  Creates a new user object from the {username, password, age, email}
    new_user = {"username": username, "password": password, "age": age, "email": email}
    all_users.append(new_user)  # Appends the new user object into the dictionary


def remove_user(user):
    # Loops through all users until it finds the object with the username the same as the parameter
    for looped_user in all_users:
        if looped_user['username'].lower() == user.lower():
            all_users.remove(looped_user)  # Remove object from dictionary


def is_username(parsed_username):
    # Loops through all users until it finds the object with the username the same as the parameter
    for user in all_users:
        if user['username'].lower() == parsed_username.lower():
            # If a user object with the same username as the parameter, return boolean 'True'
            return True
        else:
            # If no user object found, continue looping to check for it
            continue

    # If absolutely no user was found, return boolean 'False' (no user exists with the name)
    return False


def is_valid_age(age):
    try:
        int_age = int(age)  # Cast String age as an integer

        if int_age <= 0:  # Age cannot be less than 0
            return False, "That is not a valid age!"
        if 0 <= int_age <= 13:  # Must be at least 14 to use
            return False, "You must be at least 14 years old to register"

        return age

    except ValueError:  # Could not parse String as int: {sixteen, forty, banana}
        return False, "Please type a number!"


def approve_password(password_to_approve):
    # A list of approved special symbols
    special_symbols = ["\"", "!", "#", "$" "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">",
                       "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    val = [True]  # initial approval (defaulted to True)

    # Pass must be more than 6 chars
    if len(password_to_approve) < 6:
        val[0] = False
        val.append("Length should be greater than 6 characters!")

    # Pass must be less than 6 chars
    if len(password_to_approve) > 30:
        val[0] = False
        val.append("Length should be not be greater than 30 characters!")

    # Pass must contain a digit
    if not any(char.isdigit() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one numeral!")

    # Pass must contain an UPPERCASE char
    if not any(char.isupper() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one uppercase letter!")

    # PASS MUST CONTAIN lowercase CHAR
    if not any(char.islower() for char in password_to_approve):
        val[0] = False
        val.append("Password should have at least one lowercase letter!")

    # Pass must contain special char from the special_symbols list
    if not any(char in special_symbols for char in password_to_approve):
        val[0] = False
        val.append("Password should contain at least one special character!")

    # Return the callback (list) values of 'val'
    return val


def approve_email(email_to_approve):
    # Special Email Format
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    val = []

    if re.fullmatch(regex, email_to_approve):  # Does the string of email match the regex requirements
        val.append(True)
    else:
        val.append(False)
        val.append("That is not a valid email!")

    # Return callback
    return val


def append_admin():
    # Appends a default user object of type administrator
    all_users.append({'username': "admin", 'password': "0", 'age': -1, 'email': "admin@creativelogins.com"})


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

write_and_truncate_data()

# Add games to after login process
