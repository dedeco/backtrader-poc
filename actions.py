
from sqlalchemy import *

from models import Marketdata
from database import session

from datetime import datetime

def datestring_to_datetime(datestr, formatstr="%Y-%m-%d %H:%M:%S"):
    try:
        dt = datetime.strptime(datestr, formatstr)
    except ValueError:
        dt = None
    return dt

def run_some_query():
    q = session.query(Marketdata).\
        order_by(Marketdata.date)

    data  = q.all()

    for d in data[:10]:
        print (d.price_first,\
                d.price_max,\
                d.price_min,\
                d.price_last,\
                d.volume)

def add_data():
    
    m = Marketdata()
    m.quote = 'BITMEX'
    m.date = datestring_to_datetime('2018-08-07 09:50:00')
    m.price_first = 111.11
    m.price_max = 222.22
    m.price_min = 333.33
    m.price_last = 444.44
    m.volume = 1

    session.add(m)
    session.commit()


if __name__ == "__main__":

    print('Imprimindo os 10 primeiros registros...')
    run_some_query()

    print('Adicionando um registro qualquer...')
    add_data()
    print('Adicionado!')