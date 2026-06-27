def city_country(city, country, population=None):
    """Return a formatted city and country string."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"