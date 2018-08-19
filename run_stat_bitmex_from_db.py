import pandas as pd

import backtrader as bt
import backtrader.feeds as btfeed

from sqlalchemy import *
from datetime import datetime

from database import some_engine

df = pd.read_sql('SELECT * FROM marketprices', con=some_engine)

df = df[['date', 'price_first', 'price_max', 'price_min', 'price_last', 'volume']]

class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()

data = btfeed.PandasData(
    dataname=df,
    datetime='date',
    high= 'price_max',
    low='price_min',
    open= 'price_first',
    close='price_last',
    volume='volume'
)

cerebro.adddata(data)

cerebro.addstrategy(SmaCross)
cerebro.run()
cerebro.plot()