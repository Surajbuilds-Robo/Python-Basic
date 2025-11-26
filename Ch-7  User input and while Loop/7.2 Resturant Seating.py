"""Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message say-ing they’ll have to wait for a table. Otherwise, report that their table is ready"""

no_people = int(input("Enter no of personfor dinning table :"))

if no_people >8 :
    print("Wait for the table ")
else :
    print("Table is ready")