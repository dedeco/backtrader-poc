from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import HOST, PORT, USER, PASS

some_engine = create_engine('mysql://{}:{}@{}:{:d}/tempus_market_data'.format(USER,PASS,HOST,PORT))

Session = sessionmaker(bind=some_engine)
session = Session()

Base = declarative_base()

