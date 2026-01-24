""" A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket"""
age = int(input("Enter your age :"))

if age>12:
    print("Cost of Movie is $15")
elif  age<=12 and age >3:
    print("Cost of movie is $10")
elif age<=3 :
    print("Free Movie 😀")