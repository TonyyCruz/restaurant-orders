from .i_restaurant import IRestaurant


class Restaurant(IRestaurant):
    def __init__(self):
        self.clients_history = dict()
        self.menu = set()
        self.week_days_open = set()

    def is_client(self, client_name):
        return client_name in self.clients_history

    def add_client_order(self, client, order, week_day):
        try:
            self.clients_history[client][week_day]["visit"] += 1
        except KeyError:
            self.clients_history[client][week_day]["visit"] = 1
        try:
            self.clients_history[client][week_day]["orders"][order] += 1
        except KeyError:
            self.clients_history[client][week_day]["orders"][order] = 1

    def new_client(self, client, order, week_day):
        self.clients_history[client] = client
        self.clients_history[client][week_day]["visit"] = 1
        self.clients_history[client][week_day]["orders"][order] = 1

    def new_order(self, client, order, week_day):
        if self.is_client(client):
            self.add_client_order(client, order)
        else:
            self.new_client(client, order, week_day)
        # essa logica foi feita esclusivamente para o requisito do projeto
        if order not in self.menu:
            self.menu.add(order)
        if week_day not in self.week_days_open:
            self.menu.add(week_day)

    def client_history(self, client):
        return self.clients_history[client]

    def __str__(self):
        return f"{self.clients_history}"
