import alpaca_trade_api as api
from config import *

BASE_URL = "https://paper-api.alpaca.markets"


class OrderEngine(object):
    '''The Order Engine is the main api connecting to all the main brokers to place orders'''

    def __init__(self):
        self.client = api.REST(API_KEY, SECRET_KEY, BASE_URL)

    def submit_buy_order(self, ticker: str, quantity: int):
        '''Submits a market buy order at the current market price

        Returns:
        * None

        Params:
        * ticker - the ticker symbol of the security (string)
        * quantity - the amount of shares to buy (int)'''

        order = self.client.submit_order(ticker, qty=quantity)
        print(order)

    def list_of_opened_positions(self):
        '''Get all open positions and print each of them

        Returns:
        * None

        Params:
        * None'''
        positions = self.client.list_positions()
        for position in positions:
            print(position)
