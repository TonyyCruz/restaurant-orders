from restaurant.restaurant import Restaurant


class RestaurantAnalyze(Restaurant):
    def get_most_ordered_dish_per_customer(self, client):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        all_dishes = dict()
        most_ordered_meal,  most_ordered_quantity = tuple(("", 0))

        for week_day in client_active_weeks:
            for meal, num in client_data[week_day]["orders"].items():
                if meal not in all_dishes:
                    all_dishes[meal] = num
                else:
                    all_dishes[meal] += num

                if all_dishes[meal] > most_ordered_quantity:
                    most_ordered_meal = meal
                    most_ordered_quantity = all_dishes[meal]
        return most_ordered_meal

    def amount_of_meal_bought(self, client, meal):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        bought_times = 0

        for week in client_active_weeks:
            if meal in client_data[week]["orders"]:
                bought_times += client_data[week]["orders"][meal]
        return bought_times

    def get_never_ordered_per_customer(self, client):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        menu = set(self.sold_products.keys())
        bought_meals = set()

        for week in client_active_weeks:
            meals = client_data[week]["orders"].keys()
            bought_meals.update(meals)
        return bought_meals.symmetric_difference(menu)

    def get_days_never_visited_per_customer(self, client):
        client_data = self.client_history(client)
        bought_weeks = set(client_data.keys())
        return bought_weeks.symmetric_difference(self.sales_per_week)
