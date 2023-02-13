from .utils.csv_reader import csv_reader
from .utils.create_file import create_file
from .restaurant_analyze import RestaurantAnalyze

PATH_TO_SAVE_FILE = "data/mkt_campaign.txt"


def analyze_log(path_to_file):
    csv_data = csv_reader(path_to_file)
    restaurant = RestaurantAnalyze()

    for name, order, week in csv_data:
        restaurant.add_new_order(name, order, week)

    meal = restaurant.get_most_ordered_dish_per_customer("maria")
    most_bought = restaurant.amount_of_meal_bought("arnaldo", "hamburguer")
    meal_not_bought = restaurant.get_never_ordered_per_customer("joao")
    day_never_bought = restaurant.get_days_never_visited_per_customer("joao")

    analyze_data = (
        f"{meal}\n{most_bought}\n{meal_not_bought}\n{day_never_bought}"
    )
    create_file(PATH_TO_SAVE_FILE, analyze_data)
