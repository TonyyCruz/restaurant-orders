from restaurant.restaurant import Restaurant


class RestaurantOrders(Restaurant):
    def most_requested_dish(self, client):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        all_dishes = dict()
        most_bought_meal = tuple(("", 0))

        for week_day in client_active_weeks:
            for meal, num in client_data[week_day]["orders"].items():
                if meal not in all_dishes:
                    all_dishes[meal] = num
                else:
                    all_dishes[meal] += num

                if all_dishes[meal] > most_bought_meal[1]:
                    most_bought_meal = (meal, all_dishes[meal])
        return most_bought_meal

    def meal_bought_by_client(self, client, meal):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        bought_times = 0

        for week in client_active_weeks:
            if meal in client_data[week]["orders"]:
                bought_times += client_data[week]["orders"][meal]
        return bought_times

    def meal_never_bought(self, client):
        client_data = self.client_history(client)
        client_active_weeks = client_data.keys()
        bought_meals = set()

        for week in client_active_weeks:
            meals = client_data[week]["orders"].keys()
            bought_meals.update(meals)
        return bought_meals.symmetric_difference(self.menu)
