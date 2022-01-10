cities = {
    'Manila': {
        'country': "The Philippines",
        'population': 1780000,
        'fact': "The Name Manila Came From A Flower"
    },

    'Madrid': {
        'country': "Spain",
        'population': 3223000,
        'fact': "Madrid is one of the greenest cities in Europe."
    },

    'Jakarta': {
        'country': "Spain",
        'population': 10560000,
        'fact': "One of the World's Most Populated Cities"
    }
}


for city, cityKeys in cities.items():
    print("---------------")
    print("Host Country: " + cityKeys.get("country"))
    print("City Population: " + cityKeys.get("population").__str__())
    print("Fact: " + cityKeys.get("fact"))

