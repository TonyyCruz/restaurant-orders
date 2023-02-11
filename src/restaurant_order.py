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