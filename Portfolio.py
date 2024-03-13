#I chose to create only one Portfolio object per user, instead of one porfolio object per portfolio
# therefore a porfolio is initiated with 10000 per user and a default portfolio
# I chose to create a list of dictionaries since it would be easy to turn into a json object should this project
# be further expanded to send data over the interntet.
#You will note that there is data validation in both the Portfolio class and the app. 
# The Porfolio class validates its own data, ensureing it is the correct data type, of an appropriate value etc.
# while the app only checks that the user has not entered blank data. --encapsulation

class Portfolio:
    """Portfolio Management App"""

    def __init__(self):
        self.balance = 10000
        self.portfolios = [{
            "portfolioName": "default",
            "stocks": [{"stockName": "default", "shares": 0}]
        }]

    def get_portfolio(self, name):
        """get a specific portfolio and returns an error if it does not exist"""
        for f in self.portfolios:
            if f['portfolioName'] == name:
                return f
        raise KeyError('No such portfolio exists')

    #most data should be a float and not leass than equal to zero, exceptions are handled in the 
    #respective methods
    def is_valid(self, value):
        """check if a value is a number and not negative or 0 and returns an error if false"""
        try:
            val = float(value)
        except ValueError:
            raise ValueError("Amount should be a valid number")
        if val <= 0:
            raise ValueError("Amount should be positive.")
        else:
            return True
    
    #checks that the user cannot withdraw more than they have, from balance or shares.
    def good_balance(self, value, minimum):
        """Check that the value to deduct is more than the balance to deduct from"""
        if value < minimum:
            raise ValueError("Insufficient balance.")
        else:
            return value
        
    #since portfolios is a list, you can simply append a new dictionary to the list.
    def create_portfolio(self, folioName, stockName, shares):
        """Add a new Portfolio to the users portfolios"""
        if self.is_valid(shares):
            shares = float(shares)
            newPortfolio = {
                "portfolioName": folioName,
                "stocks": [{"stockName": stockName, "shares": shares}]
            }
            self.portfolios.append(newPortfolio)

    #append a dictionary of stocks to the stocks list
    def add_stock(self, folioName, stockName, shares):
        """Add a new stock to a specific portfolio"""
        if self.is_valid(shares):
            shares = float(shares)
            self.get_portfolio(folioName)["stocks"].append({"stockName": stockName, "shares": shares})

    #add shares to a stock in a portfolio
    def buy_shares(self, folioName, stockName, shares):
        """Add shares to specific stock in a specific portfolio"""
        folio = self.get_portfolio(folioName)
        if self.is_valid(shares):
            shares = float(shares)
            for stock in folio["stocks"]:
                if stock["stockName"] == stockName:
                    stock["shares"] += shares

    #remove shares to a stock in a portfolio
    def sell_shares(self, folioName, stockName, shares):
        """Removes shares from given stock in a portfolio"""
        folio = self.get_portfolio(folioName)
        if self.is_valid(shares):
            shares = float(shares)
            for stock in folio["stocks"]:
                if stock["stockName"] == stockName:
                    stock["shares"] -= self.good_balance(stock["shares"], shares)

    def deposit(self, amount):
        """Deposits money into balance"""
        if self.is_valid(amount):
            self.balance += float(amount)

    def withdraw(self, amount):
        """Withdraw money from balance"""
        if self.is_valid(amount):
            self.balance -= self.good_balance(float(amount), self.balance)   

    def show_balance(self):
        return self.balance
    
    def show_all_portfolios(self):
        """returns the list of all portfolios"""
        return self.portfolios