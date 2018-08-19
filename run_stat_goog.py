
from datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeed

class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()

data = btfeed.GenericCSVData(
    dataname='./data/GOOG_STOCK.csv',

    fromdate=datetime(2015, 8, 3),
    todate=datetime(2018, 7, 31),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d'),

    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=6,
    openinterest=-1
)

cerebro.adddata(data)

cerebro.addstrategy(SmaCross)
cerebro.run()
cerebro.plot()