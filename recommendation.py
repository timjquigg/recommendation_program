from restaurantData import *


def welcome():
    print(
        "Welcome to the restauarant recommendation engine. Based on the type "
        "of food you would like to eat and your budget, we'll give you a list"
        "of restaurant options."
    )


def get_restaurant_type():
    print("We have the following restaurant types for you to chose from:")
    while True:
        for i in range(len(types)):
            print("{index}. {type}".format(index=i + 1, type=types[i].capitalize()))
        type = input(
            "Please enter the index number of the type of restaurant you would "
            "like to go to.\n"
        )
        try:
            type = int(type) - 1
            if type in range(len(types)):
                print("You have selected {type}".format(type=types[type].capitalize()))
                check = input("Is this correct? [y/n]\n")
                if check == "y":
                    break
        except:
            print(
                "Please enter a valid index number from the available "
                "restaurant types."
            )
    return types[type]


def get_budget():
    while True:
        budget = input(
            "On a scale of 1 to 5, how much are you will to spend for dinner?\n"
        )
        try:
            if int(budget) <= 5:
                return int(budget)
            else:
                raise Exception
        except:
            print("Please enter a valid number from 1 to 5.\n")


def get_restaurants(type, budget):
    restaurant_options = []
    while True:
        for restaurant in restaurant_data:
            if restaurant[0] == type and int(restaurant[2]) <= budget:
                restaurant_options.append(restaurant)
        if len(restaurant_options) == 0:
            print(f"There are no {type} restaurants within your budget.")
            while True:
                retry = input(
                    "Would you like to change your type [t] or your budget [b]?"
                )
                if retry == "t":
                    type = get_restaurant_type()
                    break
                elif retry == "b":
                    budget = get_budget()
                    break
                else:
                    print("Please enter t for type or b for budget.")
        else:
            break
    return restaurant_options


def display_results(restaurants):
    print(
        f"Here are the {restaurants[0][0].capitalize()} restaurants within your budget:\n"
    )
    max_length = 0
    for restaurant in restaurants:
        if len(restaurant[1]) + 6 > max_length:
            max_length = len(restaurant[1]) + 6
        if len(restaurant[4]) + 9 > max_length:
            max_length = len(restaurant[4]) + 9
    for restaurant in restaurants:
        print("*" * max_length)
        print("\n")
        print(f"Name: {restaurant[1]}")
        print(f"Price: {restaurant[2]}/5")
        print(f"Rating: {restaurant[3]}/5")
        print(f"Address: {restaurant[4]}")
        print("\n")


def recommendation_engine():
    restaurant_type = get_restaurant_type()
    budget = get_budget()
    restaurants = get_restaurants(restaurant_type, budget)
    display_results(restaurants)


welcome()
while True:
    recommendation_engine()
    again = input("Would you like to get another recommendation? Type y for yes.\n")
    if again == "y":
        print("\n")
        pass
    else:
        print("Enjoy your meal!")
        break
