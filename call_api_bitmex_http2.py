
import logging
from time import sleep

from config import API_ID, API_SECRET

from bitmex_websocket import BitMEXWebsocket

def run():
    logger = setup_logger()

    ws = BitMEXWebsocket(endpoint="wss://www.bitmex.com/"
                        , symbol="XBTUSD"
                        , api_key=API_ID
                        , api_secret=API_SECRET)

    logger.info("Instrument data: %s" % ws.get_instrument())

    while(ws.ws.sock.connected):
        logger.info("Ticker: %s" % ws.get_ticker())
        #if ws.api_key:
            #logger.info("Funds: %s" % ws.funds())
        #logger.info("Market Depth: %s" % ws.market_depth())
        #logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        sleep(5)

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

if __name__ == "__main__":
    run()