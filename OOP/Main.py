from OOP.Restaurant import Restaurant
from OOP.User import User

if __name__ == '__main__':
    # Users -----

    people = [
        User("Shreyas", "Ayyengar", "15", "United Kingdom"),
        User("John", "Hannah", "56", "United Kingdom"),
        User("Laurence", "Leboeuf", "36", "Canada")
    ]

    for person in people:
        person.describe_user()
        person.greet_user()

    restaurants = [
        Restaurant("Paul's", "French"),
        Restaurant("L'Opera", "Italy"),
        Restaurant("Kashmir", "India")
    ]

    for restaurant in restaurants:
        restaurant.describe_restaurant()
        restaurant.open()

