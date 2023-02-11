from .utils.csv_reader import csv_reader
from .restaurant_order import RestaurantOrders


def analyze_log(path_to_file):
    csv_data = csv_reader(path_to_file)
    restaurantOrders = RestaurantOrders()

    for name, order, week in csv_data:
        restaurantOrders.new_order(name, order, week)

    print("====>>", restaurantOrders.meal_never_bought("joao"))
