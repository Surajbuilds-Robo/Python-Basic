"""Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers"""

favorite_numbers = {
    'suraj': [7, 21, 14],
    'aadi': [5, 10],
    'neha': [3, 9, 12],
    'rahul': [8],
    'sarah': [2, 4, 6]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
