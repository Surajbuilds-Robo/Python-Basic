"""Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once."""

cities = ["Delhi", "Tokyo", "Paris", "Cape Town", "New York"]

print("Original list:", cities)

print("Second city in the list:", cities[1])

cities[2] = "Berlin"
print("List after changing Paris to Berlin:", cities)

cities.append("Sydney")
print("List after appending Sydney:", cities)

cities.insert(2, "Amsterdam")
print("List after inserting Amsterdam at index 2:", cities)

cities.remove("Delhi")
print("List after removing Delhi:", cities)

del cities[3]
print("List after deleting the city at index 3:", cities)

popped_city = cities.pop()
print("Popped city:", popped_city)
print("List after popping the last city:", cities)

print("Number of cities in the list:", len(cities))

print("Temporarily sorted list:", sorted(cities))
print("List after using sorted():", cities)

cities.sort()
print("List after sort():", cities)


cities.reverse()
print("List after reverse():", cities)
