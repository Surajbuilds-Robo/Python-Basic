""" Start with your work from Exercise 8-10. Call the func-tion send_messages() with a copy of the list of messages. 
After calling the func-tion, print both of your lists to show that the original list has retained its messages."""

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

send_messages(texts[:], sent_messages)

print(texts)
print(sent_messages)
