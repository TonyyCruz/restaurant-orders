from .utils.csv_reader import csv_reader
from .utils.create_file import create_file
from .restaurant_analyze import RestaurantAnalyze

PATH_TO_SAVE_FILE = "data/mkt_campaign.txt"


def analyze_log(path_to_file):
    csv_data = csv_reader(path_to_file)
    restaurant = RestaurantAnalyze()

    for name, order, week in csv_data:
        restaurant.new_order(name, order, week)

    meal, _quantity = restaurant.most_requested_dish_by_client("maria")
    most_bought = restaurant.amount_of_meal_bought("arnaldo", "hamburguer")
    meal_not_bought = restaurant.meal_customer_never_bought("joao")
    day_never_bought = restaurant.week_that_customer_not_bought("joao")

    analyze_data = (
        f"{meal}\n{most_bought}\n{meal_not_bought}\n{day_never_bought}"
    )
    create_file(PATH_TO_SAVE_FILE, analyze_data)
