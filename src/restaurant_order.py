class RestaurantOrders:
    def __init__(self):
        # self.client_list = set()
        self.clients_history = dict()

    def is_client(self, client_name):
        return client_name in self.clients_history

    def add_client_order(self, client, order, week_day):
        try:
            self.clients_history[client][week_day]["visit"] += 1
        except KeyError:
            self.clients_history[client][week_day]["visit"] = 1
        try:
            self.clients_history[client][week_day][order] += 1
        except KeyError:
            self.clients_history[client][week_day][order] = 1

    def new_client(self, client, order, week_day):
        self.clients_history[client] = client
        self.clients_history[client][week_day]["visit"] = 1
        self.clients_history[client][week_day][order] = 1

    def new_order(self, client, order, week_day):
        if self.is_client(client):
            self.add_client_order(client, order)
        else:
            self.new_client(client, order, week_day)

        def __str__(self):
            return self.clients_history
