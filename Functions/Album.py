def make_album(arist_name, album_title, album_length=None):
    album = {
        'title': album_title,
        'artist': arist_name,
    }

    if album_length:
        album["num_of_songs"] = album_length

    return album


print(make_album("The Weeknd", "After Hours", 14))
print(make_album("The Weeknd", "After Hours"))

# Output:

# {'title': 'After Hours', 'artist': 'The Weeknd', 'num_of_songs': 14}
# {'title': 'After Hours', 'artist': 'The Weeknd'}
