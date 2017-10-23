class Asset(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Stock(Asset):
    def __init__(self, name, price, amount):
        super(Stock, self).__init__(name, price)
        self.price = round(float(price),3)
        self.prices = [self.price]
        
        self.amount = float(amount)
        self.amounts = [self.amount]

        self.worth = self.price*self.amount

    def update_stock(self, price, amount):
        self.prices.append(float(price))
        self.amounts.append(float(amount))
        self.amount = sum(self.amounts)
        self.price = round(sum([i*j for i,j in zip(self.prices,self.amounts)])/(sum(self.amounts)),3)
        self.worth = self.price*self.amount
        
    def info(self):
        return '{} is the name of the stock'.format(self.name)
    
    def __str__(self):
        return 'Name: {}\tprice: {} amount: {} total: {}'.format(self.name, self.price, self.amount, self.worth)

if __name__=='__main__':
    a = Stock('firstStock', 200, 10)
    print(a)
		a.update_stock(100, 10)
    print(a)
