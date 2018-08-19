

from config import API_ID, API_SECRET

import bitmex
import json

#client = bitmex.bitmex(test=True)
#print (API_ID,API_SECRET)
client = bitmex.bitmex(api_key=API_ID, api_secret=API_SECRET)

result = client.Quote.Quote_get(symbol="XBT"
                                , count=1).result()

#result = client.Position.Position_get(filter=json.dumps({'symbol': 'XBTUSD'})).result()

print (result)