"""You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list."""

dinner_list =["Gambit","Ravi","rahul"]
new_dinner_list =[dinner_list[0],"Ram",dinner_list[2]]

print(f"{dinner_list[0]} is invited.")
print(f"{dinner_list[1]} is invited.")
print(f"{dinner_list[2]} is invited.")

print(dinner_list[1],"can't make to the dinner.")

print("\tNew list")
print(f"{new_dinner_list[0]} is comming.")
print(f"{new_dinner_list[1]} is comming.")
print(f"{new_dinner_list[2]} is comming.")

