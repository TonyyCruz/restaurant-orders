from .i_restaurant import IRestaurant


class Restaurant(IRestaurant):
    def __init__(self):
        self.clients_data = dict()
        self.menu = set()
        self.week_days_open = set()

    def is_client(self, client_name):
        return client_name in self.clients_data

    def add_client_order(self, client, order, week_day):
        try:
            self.clients_data[client][week_day]["visit"] += 1
        except KeyError:
            self.clients_data[client][week_day] = dict()
            self.clients_data[client][week_day]["visit"] = 1
        try:
            self.clients_data[client][week_day]["orders"][order] += 1
        except KeyError:
            self.clients_data[client][week_day] = dict()
            self.clients_data[client][week_day]["orders"] = dict()
            self.clients_data[client][week_day]["orders"][order] = 1

    def new_client(self, client, order, week_day):
        self.clients_data[client] = dict()
        self.clients_data[client][week_day] = dict()
        self.clients_data[client][week_day]["visit"] = 1

        self.clients_data[client][week_day]["orders"] = dict()
        self.clients_data[client][week_day]["orders"][order] = 1

    def new_order(self, client, order, week_day):
        if self.is_client(client):
            self.add_client_order(client, order, week_day)
        else:
            self.new_client(client, order, week_day)
        # essa logica foi feita esclusivamente para o requisito do projeto
        self.menu.add(order)
        self.week_days_open.add(week_day)

    def client_history(self, client):
        if client in self.clients_data:
            return self.clients_data[client]

    def __str__(self):
        return f"{self.clients_data}"
