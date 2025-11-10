"""Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers."""

million =[]

for i in range(1,1000001):
    million.append(i)

print("max in list",max(million))
print("min in list",min(million))
print("sum of list",sum(million))