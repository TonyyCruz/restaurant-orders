from .restaurant_analyze import RestaurantAnalyze


class InventoryControl(RestaurantAnalyze):
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        super().__init__()
        self.inventory = dict()
        self.menu = set()
        self.initialize()

    def initialize(self):
        self.inventory = dict(self.MINIMUM_INVENTORY)
        sold_control = dict()
        for product in self.INGREDIENTS.keys():
            sold_control[product] = 0
            self.menu.add(product)
        self.sold_products = sold_control

    def do_we_have_inventory_to_order(self, order):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] <= 0:
                return False
        return True

    def stock_update(self, order):
        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1

    def order_generate(self, order, day):
        if day not in self.sales_per_week:
            self.sales_per_week[day] = 0
        self.sales_per_week[day] += 1
        self.sold_products[order] += 1
        self.stock_update(order)

    def add_new_order(self, customer, order, day):
        if not self.do_we_have_inventory_to_order(order):
            return False
        if self.is_client(customer):
            self._add_client_order(customer, order, day)
        else:
            self._new_client(customer, order, day)
        self.order_generate(order, day)

    def get_quantities_to_buy(self):
        to_buy = dict()

        for item, quantity in self.inventory.items():
            to_buy[item] = self.MINIMUM_INVENTORY[item] - quantity
        return to_buy

    def get_available_dishes(self):
        available_dishes = set()
        for item in self.menu:
            if self.do_we_have_inventory_to_order(item):
                available_dishes.add(item)
        return available_dishes
