from order import Order

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1-15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return {order.coffee for order in self.orders()}

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None

        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price

        return max(customer_spending, key=customer_spending.get)