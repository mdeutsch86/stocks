from asset import Asset

class SavingsBook(Asset):
    def __init__(self, name, price):
        super(SavingsBook, self).__init__(name, price)

    def update_savingsBook(self, amount):
        self.price += amount
