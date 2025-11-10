"""Turn your if-else chain from Exercise 5-4 into an if-elif-else chain
.• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien."""

alien_color =["green",'yellow','red']

if "green" in alien_color:
    print("You earned 5 points")
elif "yellow" in alien_color:
    print("You earned 10 points")
elif "red" in alien_color :
    print("You earned 15 points")