def show_messages(collection_strings):
    print(collection_strings)  # one print
    for s in collection_strings:
        print(s)


def send_messages(collection_strings):
    sent_messages = []

    for s in collection_strings:
        sent_messages.append(s)

    print(collection_strings)
    print(sent_messages)


send_messages(["these", "are", "my", "sent", "messages"])

# Output
# ['these', 'are', 'my', 'sent', 'messages']
# ['these', 'are', 'my', 'sent', 'messages']
