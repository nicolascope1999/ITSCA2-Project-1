import Portfolio as pf
import time

myPortfolio = pf.Portfolio()

#the loading bar gives a delay between so that the program doesnt move too fast for the user.
def display_loading_bar(duration):
    """Display a loading bar for the time of duration"""
    for _ in range(10):
        print("[", "#" * _, " " * (10 - _), "]", end="\r")
        time.sleep(duration / 10) 
    print("[", "#" * 10, "]", end="\n")


def get_input(prompt):
    """Ensures the user does not hit enter witout inputting anything"""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Error: No Input Detected! Please Try Again.")

#this code is repeated for each activity (Add, Create, Buy, Sell)
#refactored to only change what is necessary for the action.
def manage_stocks(role, activity, folioName):
    """Use the role to execute the require method, and pass the values"""
    stockName = get_input(f"What Is The Name Of The Stock You Want To {activity}?: ")
    shares = get_input(f"How Many Shares Would You Like To {activity}?: ")
    try:
        if role == "Add":
            myPortfolio.add_stock(folioName, stockName, shares)
        elif role == "Create":
            myPortfolio.create_portfolio(folioName, stockName, shares)
        elif role == "Buy":
            myPortfolio.buy_shares(folioName, stockName, shares)
        elif role == "Sell":
            myPortfolio.sell_shares(folioName, stockName, shares)
    except ValueError as e:
        print("Error: ", e)

def display_portfolios(portfolios):
    """Neatly display Portfolio(s), Stock(s) and Shares data in the terminal, in table form"""
    print("\n\t{:<20} {:<15} {:<10}".format("Portfolio Name", "Stock Name", "Shares"))
    print("\t" + "-" * 45)
    for portfolio in portfolios:
        portfolio_name = portfolio["portfolioName"]
        for stock in portfolio["stocks"]:
            stock_name, shares = stock["stockName"], stock["shares"]
            print("\t{:<20} {:<15} {:<10}\n".format(portfolio_name, stock_name, shares))

#This is essentailly the front end
#The user will contiunously engage with the program until they explicitly exit it.
#No calculations or direct changes to portfolio are made here, 
#only input handling and passing data using the correct method happens here.
sentinal = True
while sentinal:
    display_loading_bar(1)
    print("\tWelcome To myPortfolio")
    print("\t1 -- Create A New Portfolio")
    print("\t2 -- Add Stocks To An Existing Portfolio")
    print("\t3 -- Buy Shares Of A Stock From An Existing Portfolio")
    print("\t4 -- Sell Shares Of a Stock From An Existing Portfolio")
    print("\t5 -- Deposit Money Into Your Wallet")
    print("\t6 -- Withdraw Money From Your Wallet")
    print("\t7 -- Show Your Wallet Balance")
    print("\t8 -- Show your full Portfolio")
    print("\t9 -- Show one portfolio")
    print("\t0 -- Quit")
    option = get_input("Enter the number for the desired action: ")

    try:
        option = int(option)
        if option not in [0,1,2,3,4,5,6,7,8,9]:
            raise ValueError("Invalid Option Selected! Please Try Again.")
    except ValueError:
        print("Invalid Option Selected! Please Try Again.")
        continue

    if option == 0:
        print("Thank You For Using myPortfolio! Have A Nice Day!")
        sentinal = False

    if  option == 1:
        folioName = get_input("Enter The Name Of The New Portfolio: ")  
        manage_stocks("Create", "Create", folioName)
        sent = True
        while sent:
            conti = input("Create More Stocks? (y): ")
            if conti.lower() == 'n' or conti.lower() == 'no' or not conti:
                sent = False
            else:
                manage_stocks("Add", "Create", folioName)
                print("--- Portfolio Added! ---")  
            
    if option == 2:
        folioName = get_input("For Which Portfolio Do You Want To Add Stocks?: ")
        manage_stocks("Add", "Create", folioName)
        print("--- Stock Added! ---") 
        
    if  option == 3:
        folioName = get_input("For Which Portfolio Do You Want To Buy Shares?: ")
        manage_stocks("Buy", "Buy", folioName)  

    if  option == 4:
        folioName = get_input("For Which Porfolio Do You Want To Sell Shares?: ")
        manage_stocks("Sell", "Sell", folioName)
       

    if option == 5:
        amount = get_input("How Much Would You Like To Deposit?: ")
        try:
            myPortfolio.deposit(amount)
            print(f"\tYour Balance Is: R{myPortfolio.show_balance():,.2f}")
        except ValueError as e:
            print("Error: ", e)
        
    if option == 6:
        amount = get_input("How Much Would You Like To Withdraw?: ")
        try:
            myPortfolio.withdraw(amount)
            print(f"\tYour Balance is: R{myPortfolio.show_balance():,.2f}")
        except ValueError as e:
            print("Error: ", e)
        
    if  option == 7:
        balance = myPortfolio.show_balance()
        print(f"\tYour Balance is: R{balance:,.2f}")
    
    if option == 8:
        display_portfolios(myPortfolio.show_all_portfolios())

    if option == 9:
        folioName = get_input("Which Portfolio Would You Like To View?: ")
        display_portfolios([myPortfolio.get_portfolio(folioName)])