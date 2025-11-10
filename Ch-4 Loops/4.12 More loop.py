"""All versions of foods.py in this section have avoided using 
for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
Tuples
Lists work well for storing collections of items that can change throughout the life of a program. The ability to modify lists is particularly important when you’re working with a list of users on a website or a list of characters in a game. However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as 
immutable, and an immutable list is called a tuple.
Defining a Tuple
A tuple looks just like a list, except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
