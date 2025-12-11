"""Write a program that polls users about their dream vaca-tion. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
Summary
In this chapter, you learned how to use input() to allow users to provide their own information in your programs. You learned to work with both text and numerical input and how to use while loops to make your programs run as long as your users want them to. You saw several ways to control the flow of a while loop by setting an active flag, using the break statement, and using the continue statement. You learned how to use a while loop to move items from one list to another and how to remove all instances of a value from a list. You also learned how while loops can be used with dictionaries.In Chapter 8 you’ll learn about functions. Functions allow you to break your programs into small parts, each of which does one specific job. You can call a function as many times as you want, and you can store your functions in separate files. By using functions, you’ll be able to write more efficient code that’s easier to troubleshoot and maintain and that can be reused in many different programs.
"""

name_p = []
dream_place = []
no_people = int(input("Enter number of entries: "))

for i in range(no_people):
    name = input("Enter your name: ")
    name_p.append(name)
    dream = input("Enter your dream place: ")
    dream_place.append(dream)

# Combine names and dream places into a dictionary
data = {}
for name, dream in zip(name_p, dream_place):
    data[name] = dream

print(data)
