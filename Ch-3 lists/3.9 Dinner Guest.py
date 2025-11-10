""": Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner"""

guest_list=["Ram","Kajol","kantama"]

guest_list.insert(0,"suraj")
guest_list.insert(2,"Snap")
guest_list.append("Roll")
print(guest_list)

print("""Sorry there is an update 
dinner seat is avilable for 2 person only""")

guest_list.pop(0)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop(0)
print(f"Updated {len(guest_list)} invited list :- ")
print(guest_list)

print("Updated list after they were invited")

del guest_list[-1]
del guest_list[0]
print(guest_list)