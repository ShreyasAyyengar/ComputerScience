import time

all_users = []
login_attempts = 0

admin = {'username': "admin", 'password': "0123"}
all_users.append(admin)


def seperator():
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")

def start_app():
    print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
    print("Welcome to the login dashboard!!")
    print("To Login, Press 1...")
    print("To Register, Press 2...")
    print("To Exit, Press 3...")

    choice = (int(input("Where would you like to go: ")))

    if choice == 1:
        ask_for_username()

    elif choice == 2:
        start_registration()

    elif choice == 3:
        print("Goodbye")
        print(" ═ ═ ═ ═   ⋆ ★ ⋆   ═ ═ ═ ═")
        pass


# Login functions <--------------------->
def ask_for_username():
    maximum_tries = 5
    suspension_index = 0

    while suspension_index < maximum_tries:
        username = input("Please enter your username: ")
        if is_username(username):
            seperator()
            ask_for_credentials(username)
            break
        else:
            print(f"That username does not exist! Please try again: ({4 - suspension_index} tries left)")  # Please try again: ({4 - suspension_index} tries left)
            start_app()
            # suspension_index = suspension_index + 1
            # if suspension_index >= maximum_tries:
            #     seperator()
            #     print("You have been locked out of the login system for 1 minute for 5 (five) attempted logins, "
            #           "please try again in 1 (one) minute.")
            #     seperator()
            #     time.sleep(10)  # 10 seconds for demo
            #     ask_for_username()


def is_username(parsed_username):
    for users in all_users:
        if users['username'] == parsed_username:
            return True
        else:
            return False


def ask_for_credentials(user):
    password = input(f"Hello {user.title()}! Please enter your password: ")

    validate_credentials(user, password)

    # if all_users[user['password']] == password:
    #     print(True)
    # else:
    #     print(False)


def validate_credentials(username, password):
    for user in all_users:
        if user.get('username').__eq__(username) and user.get('password').__eq__(password):
            login()


def login():
    print(
        "🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩")
    print(
        "██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗")
    time.sleep(0.3)
    print(
        "██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝")
    time.sleep(0.3)
    print(
        "╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗")
    time.sleep(0.3)
    print(
        " ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝")
    time.sleep(0.3)
    print(
        " ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗")
    time.sleep(0.3)
    print(
        "  ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝")
    print(
        "🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫🟥🟧🟨🟩🟦🟪⬛️⬜️🟫️🟥🟧🟨🟩️")


def ask_password_reset():
    print("Give user directions for a password reset")


# Registration functions <---------------->


start_app()