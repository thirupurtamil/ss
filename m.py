from jugaad_data.nse import *
from pprint import pprint
from time import sleep
from datetime import datetime
import requests
import pandas as pd
import time
from datetime import *
from time import *


n = NSELive()
xx = n.live_index('NIFTY MIDCAP SELECT')




data=[]


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',}
with requests.session() as req:
    req.get('https://www.nseindia.com/get-quotes/derivatives?symbol=MIDCPNIFTY',headers = headers)

    api_req=req.get('https://www.nseindia.com/api/quote-derivative?symbol=MIDCPNIFTY',headers = headers).json()
    for item in api_req['stocks']:
        data.append([
            
            item['metadata']['strikePrice'],
            item['metadata']['optionType'],
            item['metadata']['openPrice'],
            item['metadata']["highPrice"],
            item['metadata']['lowPrice'],
            item['metadata']['lastPrice'],
            item['metadata']['numberOfContractsTraded'],
            item['metadata']['totalTurnover'],]),

cols=['STRIKEPRICE','OPTION','OPEN',"HIGH",'LOW','LAST','VOL','VALUE']
df = pd.DataFrame(data, columns=cols)
get_rows = df.head(6)


url = 'https://www.nseindia.com/api/option-chain-indices?symbol=MIDCPNIFTY'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8',
           'accept-encoding': 'gzip, deflate, br'}

session = requests.Session()

def importdata():
    request = session.get(url,headers=headers)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, cookies=cookies).json()   
    rdata = pd.DataFrame(response)
    t_ce = rdata['filtered']['CE']['totOI']
    t_pe = rdata['filtered']['PE']['totOI']
    tc = rdata['filtered']['CE']['totVol']
    tp   = rdata['filtered']['PE']['totVol']
    dt = rdata['records']['timestamp']
    trend = t_ce-t_pe
    tr = tc - tp
    t = dt.split(" ")
    data = {
      "Time" : t[1],
      "COI" : t_ce,
      "POI" : t_pe,
      "tc" : tc,
      "tp" : tp,
      "Tr" : tr,
      "Trend" : trend
   }
    return data



print("SERVER TIME:", xx['timestamp'],) 
print("|----------------------------------[",xx['name'],"]-----------------|")

print (get_rows)
print("|--------------------------------------------------------------------------|")

print("|{:<9}| {:<15}|  {:<15}| {:<10}| {:<10}".format(" Time","    CALL","    PUT","Trend","LastPrice",))

print("|--------------------------------------------------------------------------|")

data = importdata()

print("|{:<9}|    {:<12}|     {:<12}| {:<10}|   {:<10}".format(data["Time"],data["COI"],data["POI"],data["Trend"],xx['data'][0]['lastPrice']))
print("|--------------------------------------------------------------------------|")

   
















