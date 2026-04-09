"""Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random num-
ber between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times."""


import random 
class Dice :
    
    def __init__(self,slides,roll_times):
        self.slides = slides
        self.roll_times = roll_times

    def roll_dice(self):
        dice_history =[]
        for i in range (0,self.roll_times):
            dice_history.append(random.randint(1,self.slides))
        print(f"Dice History of {self.slides} that has been rolled {self.roll_times} : {dice_history}")

slides = int(input("Enter no of side does your dice have : "))
roll_times=int(input("How many times i have to roll : "))


dice = Dice(slides,roll_times)

dice.roll_dice()


