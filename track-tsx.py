import yfinance as yf

# Replace these tickers with the TSX-listed stocks you want to track
tickers = ['SHOP.TO', 'TD.TO', 'BNS.TO', 'ENB.TO']

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    return stock_info

def main():
    for ticker in tickers:
        stock_info = get_stock_data(ticker)
        print(f"{stock_info['shortName']} ({ticker}):")
        print(f"Current price: {stock_info['regularMarketPrice']}")
        print(f"Market cap: {stock_info['marketCap']}")
        print(f"52-week high: {stock_info['fiftyTwoWeekHigh']}")
        print(f"52-week low: {stock_info['fiftyTwoWeekLow']}\n")

if __name__ == "__main__":
    main()
