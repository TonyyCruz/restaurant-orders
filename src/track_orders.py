from .restaurant_analyze import RestaurantAnalyze


class TrackOrders(RestaurantAnalyze):
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        sales = 0
        if not self.week_sales:
            return sales
        else:
            for _, orders in self.week_sales.items():
                sales += orders
            return sales

    # def add_new_order(self, customer, order, day):
    #     pass

    # def get_most_ordered_dish_per_customer(self, customer):
    #     pass

    # def get_never_ordered_per_customer(self, customer):
    #     pass

    # def get_days_never_visited_per_customer(self, customer):
    #     pass

    def get_busiest_day(self):
        week_day, best_order = ("segunda-feira", 0)

        for week, orders in self.week_sales.items():
            if orders > best_order:
                week_day = week
                best_order = orders
        return week_day

    def get_least_busy_day(self):
        week_day, less_order = ("segunda-feira", None)

        for week, orders in self.week_sales.items():
            if less_order is None:
                week_day = week
                less_order = orders
            if orders < less_order:
                week_day = week
                less_order = orders
        return week_day
