"""
Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message 
and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly."""


def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

texts = [
    "Hello there",
    "How are you?",
    "See you soon",
    "Take care"
]

sent_messages = []

send_messages(texts, sent_messages)

print(texts)
print(sent_messages)
