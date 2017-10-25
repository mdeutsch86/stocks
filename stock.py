from asset import Asset

class Stock(Asset):
    def __init__(self, name, price, amount, fee=0.):
        super(Stock, self).__init__(name, price)
        self.price = round(float(price),3)
        self.prices = [self.price]

        self.amount = float(amount)
        self.amounts = [self.amount]

        self.worth = self.price*self.amount

        self.fee = float(fee)
        self.fees = [fee]

        self.breakEven = self.calc_breakEven()

        
        
    def update_stock(self, price, amount, fee):
        self.prices.append(float(price))
        self.amounts.append(float(amount))
        self.amount = sum(self.amounts)
        self.price = round(sum([i*j for i,j in zip(self.prices,self.amounts)])/(sum(self.amounts)),3)
        self.worth = self.price*self.amount
        self.fees.append(self.fee)
        self.breakEven = self.calc_breakEven()

    def calc_breakEven(self):
        return (sum([p*a for p,a in zip(self.prices, self.amounts)])+sum(self.fees))/sum(self.amounts)
       
    def info(self):
        return '{} is the name of the stock'.format(self.name)

    def __str__(self):
        return 'Name: {}\nprice: {}\namount: {}\ntotal: {}\nbreak even: {}'.format(self.name, self.price, self.amount, self.worth, self.breakEven)

if __name__=='__main__':
    a = Stock('firstStock', 200, 10, 9.9)
    print(a)
    a.update_stock(100, 10, 9.9)
    print(a)
