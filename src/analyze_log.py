from .utils.csv_reader import csv_reader
from .restaurant_order import RestaurantOrders


def analyze_log(path_to_file):
    csv_data = csv_reader(path_to_file)
    print(csv_data)
