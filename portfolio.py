from asset import Asset
from stock import Stock
from savingsBook import SavingsBook
class Portfolio(object):
    def __init__(self):
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


    def buyStock(self, stock_name, stock_price, stock_amount):
        stock_name = stock_name.upper()

        if stock_name in self.stocks.keys():
            self.stocks[stock_name].update_stock(stock_price, stock_amount)
        else:
            self.stocks.update({stock_name: Stock(stock_name, stock_price, stock_amount)})

    def deposit_on_SavingsBook(self, bookName, amount):
        bookName = bookName.upper()

        if bookName in self.savingBooks.keys():
            self.savingBooks[bookName].update_savingsBook(amount)
        else:
            self.savingBooks.update({bookName: SavingsBook(bookName, amount)})


    def __str__(self):
        if self.cash==0.:
            data = ''
        else:
            data = 'Cash: {}\n'.format(self.cash)

        for key, value in self.stocks.iteritems():
            data+= str(value)+'\n'
        return data

if __name__ =='__main__':

    p=Portfolio()
    p.deposit_on_SavingsBook('S1',1898.50)
    p.buyStock('Ko', 40.0, 10)
    p.buyStock('IBAB', 26.28,40)
