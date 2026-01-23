"""Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the infor-mation you have stored about it."""

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': 'it is the most populous metropolitan area in the world'
    },
    'paris': {
        'country': 'france',
        'population': '11 million',
        'fact': 'it is known as the city of lights'
    },
    'mumbai': {
        'country': 'india',
        'population': '20 million',
        'fact': 'it is the financial capital of india'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact'].capitalize()}")
