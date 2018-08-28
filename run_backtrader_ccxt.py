from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import time
from datetime import datetime, timedelta

import backtrader as bt
import ccxt

#pylint: disable=E1101,E1123

class TestStrategy(bt.Strategy):

    def start(self):
        self.counter = 0
        print('START')

    def prenext(self):
        self.counter += 1
        print('prenext len %d - counter %d' % (len(self), self.counter))

    def __init__(self):
        pass

    def next(self):
        print('------ next len %d - counter %d' % (len(self), self.counter))

        self.counter += 1

        print('*' * 5, 'NEXT data0:', bt.num2date(self.data0.datetime[0]),
              self.data0._name, self.data0.open[0], self.data0.high[0],
              self.data0.low[0], self.data0.close[0], self.data0.volume[0],
              bt.TimeFrame.getname(self.data0._timeframe), len(self.data0))

class TestStrategy2(bt.Strategy):
    def next(self):

        for data in self.datas:

            print (data.datetime[0], '$$$$$$$$$$$$$$$$')
            #print (data.datetime[1], '$$$$$$$$$$$$$$$$')
            print (data.datetime[-1], '$$$$$$$$$$$$$$$$')

            print('*' * 5, 'NEXT:', bt.num2date(data.datetime[0]), data._name, data.open[0], data.high[0],
                  data.low[0], data.close[0], data.volume[0],
                  bt.TimeFrame.getname(data._timeframe), len(data))
            #if not self.getposition(data):
            #    order = self.buy(data, exectype=bt.Order.Limit, size=10, price=data.close[0])
            #else:
            #    order = self.sell(data, exectype=bt.Order.Limit, size=10, price=data.close[0])

    def notify_order(self, order):
        print('*' * 5, "NOTIFY ORDER", order)

from config import API_ID, API_SECRET

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    exchange = 'bitmex'
    symbol = 'BTC/USD'

    broker_config = {
        'apiKey': API_ID,
        'secret': API_SECRET,
        'nonce': lambda: str(int(time.time() * 1000))
    }

    broker = bt.brokers.CCXTBroker(exchange=exchange, currency='USDT', config=broker_config)
    cerebro.setbroker(broker)

    hist_start_date = datetime.utcnow() - timedelta(minutes=5)

    data = bt.feeds.CCXT(exchange=exchange,
                         symbol=symbol,
                         timeframe=bt.TimeFrame.Minutes,
                         fromdate=hist_start_date,
                         ohlcv_limit=444)

    cerebro.adddata(data)

    cerebro.addstrategy(TestStrategy2)
    cerebro.run()
    #cerebro.plot()