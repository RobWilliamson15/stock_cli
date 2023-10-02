# :dollar:stock_cli
## Description
Stock_cli is a lightweigth, command-line based tool designed to fetch and display real-time stock data. It fetches data using the 'yfinance' library and displays the change percentage between open and mid prices with colour coding.

The app allows users to customize the list of stocks they want to track by configuring a simple text file, and it can be run manually or scheduled to run automatically at specified times using cron.

## Features
- Display real-time stock data.
- Customize the list of stocks to track.
- Schedule to run at market open and close or any other time.
- Colour-coded display for positive and negative changes.

## Prerequisites
- Python 3.x
- Docker (Optional but recommended)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/RobWilliamson15/stock-cli.git
cd stock-cli
```

### 2. Setup a Python Environment
#### - Using Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### - Using Docker
```sh
docker build -t stock-cli .
```

## Configuration and Usage

### Initial Setup
Run the application once to set up the initial configuration file.
```sh
python fetch.py  # Or `docker run --rm stock-cli` if using Docker.
```
Follow the prompt and enter the stock symbols separated by a comma, e.g., AAPL,GOOGL,MSFT.

### Running the Application
```sh
python fetch.py  # Or `docker run --rm stock-cli` if using Docker.
```

### Customizing Stock Symbols
To modify the list of stock symbols, edit the `symbols_config.txt` file in the project directory:
```
AAPL,GOOGL,MSFT  # Example of content
```

### Scheduling
To run the app at specific times, like 10 minutes after the market opens and closes every weekday, you can set up a cron job:

```cron
TZ=America/New_York
40 9 * * 1-5 /path-to-your/python /path-to-your/fetch.py  # 9:40 AM Eastern Time. Replace with `docker run --rm stock-cli` if using Docker.
10 16 * * 1-5 /path-to-your/python /path-to-your/fetch.py  # 4:10 PM Eastern Time. Replace with `docker run --rm stock-cli` if using Docker.
```

