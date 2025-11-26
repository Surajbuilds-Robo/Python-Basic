"""Use the code in favorite_languages.py (page 96).• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
Nesting
Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. You can nest dictionar-ies inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary. Nesting is a powerful feature, as the following examples will demonstrate.
A List of Dictionaries
The alien_0 dictionary contains a variety of information about one alien, but it has no room to store information about a second alien, much less a screen full of aliens. How can you manage a fleet of aliens? One way is to make a list of aliens in which each alien is a dictionary of information about that alien. For example, the following code builds a list of three aliens:
aliens.py alien_0 = {'color': 'green', 'points': 5}alien_1 = {'color': 'yellow', 'points': 10}alien_2 = {'color': 'red', 'points': 15}
1 aliens = [alien_0, alien_1, alien_2]for alien in aliens:    print(alien)
"""
# favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'sarah', 'edward', 'phil', 'suraj', 'aadi']

for person in people:
    if person in favorite_languages:
        print(f"Thank you {person.title()} for responding to the poll.")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")

# Nesting Example
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
