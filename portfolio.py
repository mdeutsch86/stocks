from asset import Asset
from stock import Stock
from savingsBook import SavingsBook

class Portfolio(object):
    def __init__(self):
        """
        You should first pay_in, otherwise you can not buy anything
        """
        self.cash = 0.
        self.stocks = {}
        self.savingBooks = {}
        self.others = 0.

        self.performance = self.calc_performance()
        self.asset_allocation = {}

    def pay_in(self, amount):
        self.cash += float(amount)

    def calc_performance(self):
        pass

    def calc_asset_allocation(self):
        cash = self.cash
        stocks =0
        savingBooks = 0

    def calc_howMuch(self, price, fees):
        """
        calculates how much stocks are possible to buy depending
        on the cash you have on your account
        """
        return (self.cash - fees)//price

    def buyStock(self, stock_name, stock_price, stock_amount, stock_fee):
        stock_name = stock_name.upper()
        if self.cash > stock_price*stock_amount-stock_fee:
            self.cash -= stock_price*stock_amount-stock_fee
            if stock_name in self.stocks.keys():
                self.stocks[stock_name].update_stock(stock_price, stock_amount, stock_fee)
            else:
                self.stocks.update({stock_name: Stock(stock_name, stock_price, stock_amount, stock_fee)})
        else:
            print("You do not have enough money to buy that much stocks!!!")

    def deposit_on_SavingsBook(self, bookName, amount):
        bookName = bookName.upper()

        if bookName in self.savingBooks.keys():
            self.savingBooks[bookName].update_savingsBook(amount)
        else:
            self.savingBooks.update({bookName: SavingsBook(bookName, amount)})


    def __str__(self):
        if self.cash == 0.:
            data = ''
        else:
            data = 'Cash: {}\n'.format(self.cash)

        for key, value in self.stocks.iteritems():
            data+= str(value)+'\n'
        return data

if __name__ =='__main__':
    import random
    stockprice = [27.69,28.30,27.78,28.38,27.86,27.13,28.26,28.82,28.18,28.31]
    fee = 5.0
    p=Portfolio()
    p.pay_in(100)
    p.buyStock('KO', 27.96, 3, fee)

    for i in range(10):
        price = random.choice(stockprice)
        p.pay_in(100)
        amount = p.calc_howMuch(price,fee)
        if price < p.stocks['KO'].price:
            p.buyStock('KO', price, amount, fee)
            print('bought')
    print(p)
