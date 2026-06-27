"""Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize."""

import random
import string

class Lottery:

    def ticket(self):
        # Generate ticket: 3 digits + 1 uppercase letter
        return "".join([
            str(random.randint(0, 9)) for _ in range(3)
        ]) + random.choice(string.ascii_uppercase)


# Create object
game = Lottery()

# Generate your ticket
my_ticket = game.ticket()
print("🎟️   My Ticket:", my_ticket)

# Simulation loop
count = 0

while True:
    count += 1
    new_ticket = game.ticket()

    if new_ticket == my_ticket:
        print("🏆 Winning Ticket Found:", new_ticket)
        print("🔁 Total Attempts:", count)
        break