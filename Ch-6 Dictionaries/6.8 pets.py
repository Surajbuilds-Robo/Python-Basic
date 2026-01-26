"""Make several dictionaries, where each dictionary represents a differ-ent pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet"""

pet_1 = {'animal': 'dog', 'owner': 'rahul'}
pet_2 = {'animal': 'cat', 'owner': 'aisha'}
pet_3 = {'animal': 'parrot', 'owner': 'suraj'}
pet_4 = {'animal': 'rabbit', 'owner': 'neha'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Animal: {pet['animal'].title()}, Owner: {pet['owner'].title()}")
