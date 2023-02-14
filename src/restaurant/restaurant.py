from .i_restaurant import IRestaurant


class Restaurant(IRestaurant):
    def __init__(self):
        self.clients_data = dict()
        self.sold_products = dict()
        self.sales_per_week = dict()

    def is_client(self, client_name):
        return client_name in self.clients_data

    def _add_client_order(self, client, order, week_day):
        if week_day not in self.clients_data[client]:
            self.clients_data[client][week_day] = dict()
            self.clients_data[client][week_day]["visit"] = 0
            self.clients_data[client][week_day]["orders"] = dict()

        if order not in self.clients_data[client][week_day]["orders"]:
            self.clients_data[client][week_day]["orders"][order] = 0

        self.clients_data[client][week_day]["visit"] += 1
        self.clients_data[client][week_day]["orders"][order] += 1

    def _new_client(self, client, order, week_day):
        self.clients_data[client] = dict()
        self.clients_data[client][week_day] = dict()
        self.clients_data[client][week_day]["visit"] = 1

        self.clients_data[client][week_day]["orders"] = dict()
        self.clients_data[client][week_day]["orders"][order] = 1

    def add_new_order(self, client, order, week_day):
        if self.is_client(client):
            self._add_client_order(client, order, week_day)
        else:
            self._new_client(client, order, week_day)

        if order not in self.sold_products:
            self.sold_products[order] = 0
        if week_day not in self.sales_per_week:
            self.sales_per_week[week_day] = 0
        self.sales_per_week[week_day] += 1
        self.sold_products[order] += 1

    def client_history(self, client):
        if client in self.clients_data:
            return self.clients_data[client]

    def __str__(self):
        return f"{self.clients_data}"
