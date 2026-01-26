"""Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value."""

chck = input("🎟️    Ticket then type yes / no : ").lower()
if chck =="yes"  :
    i=0
    no_tickets =int(input("For how any person u are buying ticket : "))
    while i!=no_tickets:
        age = int(input("Enter your age : "))

        if age>12:
            print("Cost of Movie is💲 15")
        elif  age<=12 and age >3:
            print("Cost of movie is 💲  10")
        elif age<=3 :
            print("Free Movie 😀")
        i+=1
    print("Thank u for buying Tickets  ")

else :
    print("Thank u for buying Ticket 🎫")