"""
Fetches stock data using yfinance
"""
import os
import yfinance as yf
from termcolor import colored

CONFIG_FILE = 'symbols_config.txt'

def setup_config():
    """
    Setups a config containing all stock tickers
    """
    with open(CONFIG_FILE, 'w') as file:
        print("Config file not found. Please setup your stock symbols.")
        symbols = input("Enter the stock symbols separated by a comma: ")
        file.write(symbols)

def read_config():
    """
    Reads the stock tickers from the config
    """
    with open(CONFIG_FILE, 'r') as file:
        symbols = file.read().strip().split(',')
    return symbols

def get_stock_data(symbol):
    """
    Pulls stock data using yfinance and then outputs to cli
    """
    try:
        # Fetch the stock data
        stock = yf.Ticker(symbol)

        # Get general information
        info = stock.info

        # Calculate 52-week average
        week_52_average = (info['fiftyTwoWeekHigh'] + info['fiftyTwoWeekLow']) / 2

        # Calculate mid price to use as regularMarketPrice
        mid_price = (info['bid'] + info['ask']) / 2

        # Check if the regularMarketOpen is zero before performing division
        if info['regularMarketOpen'] == 0:
            print(f"Cannot calculate the percentage change for {symbol} as the Open Price is 0.")
        else:
        # Calculate the percentage change between open and mid prices
            percentage_change = ((mid_price - info['regularMarketOpen']) / info['regularMarketOpen']) * 100

            # Determine the color based on the percentage change
            color = 'green' if percentage_change >= 0 else 'red'

            print(f"Stock Symbol: {symbol}")
            print(colored(f"Change Precentage between Open and Mid Price: {percentage_change:.2f}%", color))
            print(f"Current Price: ${round(mid_price, 2)}")
            print(f"Open Price: ${info['regularMarketOpen']}")
            print(f"Previous Close Price: ${info['regularMarketPreviousClose']}")
            print(f"52 Week Average: ${round(week_52_average, 2)}")

    except Exception as cannot_retrieve:
        print(f"Could not retrieve data for {symbol}. Error: {cannot_retrieve}")


if __name__ == "__main__":
    if not os.path.exists(CONFIG_FILE):
        setup_config()

    symbols_outer = read_config()
    for symbol_outer in symbols_outer:
        symbol_outer = symbol_outer.strip().upper()
        if symbol_outer:
            get_stock_data(symbol_outer)
