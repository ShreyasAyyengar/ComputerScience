import random  # imports random library (not really needed, just for ease)

dinner_guests = ["person1", "person2", "person3"]  # initialise the dinner guests into the dinner_guests array list

dinner_guests.sort()

for guest in dinner_guests:
    print(f"Hello {guest}! You have been invited to my dinner lmao, can u come?")  # invited the people

cancelled_guest = random.choice(dinner_guests)  # chooses a random guest to remove
dinner_guests.remove(cancelled_guest) # removes that guest from the array

print("-----------------------------------")
print("Oh no! It looks like " + cancelled_guest + " could not make it!- Added Yoshi instead")  # Sends a removal and invite message
print("-----------------------------------")
dinner_guests.append("Yoshi")  # Appends a new element to the array

print("-----------------------------------")

for attending_guest in dinner_guests:
    print("Just a quick update " + attending_guest + ", we have found a bigger table and will be adding more guests!")  # message all guest about new table

dinner_guests.insert(3, "Ethan")  # insert a new element
dinner_guests.insert(2, "Kyle")  # insert a new element
dinner_guests.append("Jackie")  # note that here i THINK you can also use .insert(-1, "Jackie") since -1 refers to the end. ¯\_(ツ)_/¯

print("-----------------------------------")

for final_guest in dinner_guests:
    print(f"Hello {final_guest}! You have been invited to my dinner AGAIN lmao, can u come?")  # Invites all updated guests.
