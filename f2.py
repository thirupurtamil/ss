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
xx = n.live_index('NIFTY FINANCIAL SERVICES')




data=[]


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',}
with requests.session() as req:
    req.get('https://www.nseindia.com/get-quotes/derivatives?symbol=FINNIFTY',headers = headers)

    api_req=req.get('https://www.nseindia.com/api/quote-derivative?symbol=FINNIFTY',headers = headers).json()
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
get_rows = df.head(14)


url = 'https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY'
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
    
    dt = rdata['records']['timestamp']
    trend = t_ce-t_pe
    
    t = dt.split(" ")
    
    data = {
      "Time" : t[1],
      "COI" : t_ce,
      "POI" : t_pe,
      "Trend" : trend
   }
    return data



url = 'https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37','accept-encoding': 'gzip, deflate, br','accept-language': 'en-GB,en;q=0.9,en-US;q=0.8'}

session = requests.Session()
request = session.get(url,headers=headers)
cookies = dict(request.cookies)


def dataframe():
    response = session.get(url,headers=headers,cookies=cookies).json()
    rawdata = pd.DataFrame(response)
    rawop = pd.DataFrame(rawdata['filtered']['data']).fillna(0)
    data = []
    for i in range(0,len(rawop)):
        calloi = callcoi = cltp = putoi = putcoi = pltp = 0
        stp = rawop['strikePrice'][i]
        if(rawop['CE'][i]==0):
            calloi = callcoi = 0
        else:
            calloi = rawop['CE'][i]['openInterest']
            callcoi = rawop['CE'][i]['changeinOpenInterest']
            cltp = rawop['CE'][i]['lastPrice']
        if(rawop['PE'][i] == 0):
            putoi = putcoi = 0
        else:
            putoi = rawop['PE'][i]['openInterest']
            putcoi = rawop['PE'][i]['changeinOpenInterest']
            pltp = rawop['PE'][i]['lastPrice']
        opdata = {
            'CALL OI': calloi, 'CALL CHNG OI': callcoi, 'CALL LTP': cltp, 'STRIKE PRICE': stp,
            'PUT OI': putoi, 'PUT CHNG OI': putcoi, 'PUT LTP': pltp
        }
        
        data.append(opdata)
    optionchain = pd.DataFrame(data)
    return optionchain

optionchain = dataframe()
op = optionchain.head(90)

opd = optionchain.set_index("STRIKE PRICE")
oph = opd.iloc[-65:-6] 




ops = oph.filter((["CALL CHNG OI"])).idxmax()
ops=ops.max()

ops1 = oph.filter((["CALL CHNG OI"])).idxmin()
ops1=ops1.min()

opa = oph.filter((["PUT CHNG OI"])).idxmax()
opa=opa.max()

opa1 = oph.filter((["PUT CHNG OI"])).idxmin()
opa1=opa1.min()



opc = oph.filter((["CALL OI"])).idxmax()
opc=opc.max()
opp = oph.filter((["PUT OI"])).idxmax()
opp=opp.max()










print("SERVER TIME:", xx['timestamp'],) 
print("|----------------------------------[",xx['name'],"]-----------------|")

print (get_rows)
print("|--------------------------------------------------------------------------|")

print("|{:<9}| {:<15}|  {:<15}| {:<10}| {:<10}".format(" Time","    CALL","    PUT","Trend","LastPrice",))

print("|--------------------------------------------------------------------------|")

data = importdata()

print("|{:<9}|    {:<12}|     {:<12}| {:<10}|   {:<10}".format(data["Time"],data["COI"],data["POI"],data["Trend"],xx['data'][0]['lastPrice']))
print("|--------------------------------------------------------------------------|")


print("|{:<9}| {:<15}|  {:<15}| {:<10}".format("OPTION","CHANGE +","CHANGE -","OPEINTEREST",))

print("|--------------------------------------------------------------------------|")


print("|{:<9}| {:<15}|  {:<15}| {:<10}".format(" CALL",ops,    ops1,opc))

print("|--------------------------------------------------------------------------|")
print("|{:<9}| {:<15}|  {:<15}| {:<10}".format("  PUT",opa,opa1,opp))

print("|--------------------------------------------------------------------------|")

   
















