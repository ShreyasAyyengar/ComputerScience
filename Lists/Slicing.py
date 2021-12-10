songs = ["Viva la Vida", "STAY", "Cold Heart", "Gravity", "Interlude", "Epic song", "My Universe", "Blinding Lights", "Hurricane"]

print(f"The FIRST THREE elements in my song list are {songs[:3]}")
print(f"The LAST three elements in my song list are {songs[3:]}")
print(f"The MIDDLE three elements in my song list are {songs[(len(songs)//2)-1 : songs[(len(songs)//2)+1]]}")
