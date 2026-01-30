"""Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message"""


def show_messages(messages):
    for message in messages:
        print(message)

texts = [
    "Hello there",
    "How are you?",
    "See you soon",
    "Take care"
]

show_messages(texts)
