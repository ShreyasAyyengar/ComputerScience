# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def print_string_collection(collection_strings):
    print(collection_strings)  # one print
    for s in collection_strings:
        print(s)


print_string_collection(["This", "Is", "A", "Series", "Of", "Strings"])

# Output
# ['This', 'Is', 'A', 'Series', 'Of', 'Strings']
# This
# Is
# A
# Series
# Of
# Strings
