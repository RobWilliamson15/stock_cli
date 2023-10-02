"""
Perform unittests on fetch.py
"""
import unittest
from unittest.mock import patch, mock_open, MagicMock
import fetch

class TestStockCli(unittest.TestCase):
    """
    Unittest Test Cases to cover fetch.py
    """
    @patch("builtins.open", new_callable=mock_open, read_data="AAPL,GOOGL,MSFT")
    def test_read_config(self, _):
        """
        Test case to read config file
        """
        read_data = "AAPL, GOOGL, MSFT"
        self.assertNotEqual(read_data.strip(), "", "Config file is not empty")
        expected_symbols = ["AAPL", "GOOGL", "MSFT"]
        self.assertEqual(fetch.read_config(), expected_symbols)

    @patch.object(fetch, 'yf')
    def test_get_stock_data(self, mock_yf):
        """
        Test case to check if the stock info is outputted correctly
        """
        mock_stock = MagicMock()
        mock_stock.info = {
            'fiftyTwoWeekHigh': 200.0,
            'fiftyTwoWeekLow': 100.0,
            'bid': 150.0,
            'ask': 150.0,
            'regularMarketOpen': 140.0,
            'regularMarketPreviousClose': 130.0,
        }

        mock_yf.Ticker.return_value = mock_stock
        with patch("builtins.print") as mock_print:
            fetch.get_stock_data("AAPL")
        
        # Assert that print was called with the expected strings
        mock_print.assert_any_call("Stock Symbol: AAPL")
        mock_print.assert_any_call("Change Precentage between Open and Mid Price: 7.14%")
        mock_print.assert_any_call("Current Price: $150.0")
        mock_print.assert_any_call("Open Price: $140.0")
        mock_print.assert_any_call("Previous Close Price: $130.0")
        mock_print.assert_any_call("52 Week Average: $150.0")


if __name__ == '__main__':
    unittest.main()
