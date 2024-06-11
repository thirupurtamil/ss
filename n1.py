from jugaad_data.nse import NSELive
import datetime 
import platform 
import time
import requests 
import pandas as pd
import numpy as np
import json

n = NSELive()     

xx = n.live_index('NIFTY 50')




def md():
   
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',}


   with requests.session() as req:
        req.get('https://www.nseindia.com/get-quotes/derivatives?symbol=NIFTY',headers = headers)

        api_req=req.get('https://www.nseindia.com/api/quote-derivative?symbol=NIFTY',headers = headers).json()
  
   return api_req

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
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


acb = md()
ds=[]



z = acb["stocks"][0]
ss = z["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a = z["metadata"]["strikePrice"]
aa = z["metadata"]["optionType"]
d= z["metadata"]["numberOfContractsTraded"]
v = z['metadata']['totalTurnover']
p = z["metadata"]["lastPrice"]
i= z["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c= z["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]




z1= acb["stocks"][1]
ss1= z1["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a1 = z1["metadata"]["strikePrice"]
aa1 = z1["metadata"]["optionType"]
d1 = z1["metadata"]["numberOfContractsTraded"]
v1  = z1['metadata']['totalTurnover']
p1= z1["metadata"]["lastPrice"]
i1= z1["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c1= z1["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]


z2 = acb["stocks"][2]
ss2 = z2["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a2 = z2["metadata"]["strikePrice"]
aa2 = z2["metadata"]["optionType"]
d2= z2["metadata"]["numberOfContractsTraded"]
v2 = z2['metadata']['totalTurnover']
p2 = z2["metadata"]["lastPrice"]
i2= z2["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c2= z2["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]



z3 = acb["stocks"][3]
ss3 = z3["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a3 = z3["metadata"]["strikePrice"]
aa3 = z3["metadata"]["optionType"]
d3= z3["metadata"]["numberOfContractsTraded"]
v3 = z3['metadata']['totalTurnover']
p3 = z3["metadata"]["lastPrice"]
i3= z3["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c3= z3["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]



z4 = acb["stocks"][4]
ss4 = z4["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a4 = z4["metadata"]["strikePrice"]
aa4 = z4["metadata"]["optionType"]
d4= z4["metadata"]["numberOfContractsTraded"]
v4 = z4['metadata']['totalTurnover']
p4 = z4["metadata"]["lastPrice"]
i4= z4["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c4= z4["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]






z5 = acb["stocks"][5]
ss5 = z5["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a5 = z5["metadata"]["strikePrice"]
aa5 = z5["metadata"]["optionType"]
d5= z5["metadata"]["numberOfContractsTraded"]
v5 = z5['metadata']['totalTurnover']
p5 = z5["metadata"]["lastPrice"]
c5= z5["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]
i5= z5["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']





z6 = acb["stocks"][6]
ss6 = z6["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a6 = z6["metadata"]["strikePrice"]
aa6 = z6["metadata"]["optionType"]
d6= z6["metadata"]["numberOfContractsTraded"]
v6 = z6['metadata']['totalTurnover']
p6 = z6["metadata"]["lastPrice"]
i6= z6["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c6= z6["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]



z7 = acb["stocks"][7]
ss7 = z7["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a7 = z7["metadata"]["strikePrice"]
aa7 = z7["metadata"]["optionType"]
d7= z7["metadata"]["numberOfContractsTraded"]
v7 = z7['metadata']['totalTurnover']
p7 = z7["metadata"]["lastPrice"]
i7= z7["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c7= z7["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]


z8 = acb["stocks"][8]
ss8 = z8["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a8 = z8["metadata"]["strikePrice"]
aa8 = z8["metadata"]["optionType"]
d8= z8["metadata"]["numberOfContractsTraded"]
v8 = z8['metadata']['totalTurnover']
p8 = z8["metadata"]["lastPrice"]
i8= z8["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c8= z8["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]

z9 = acb["stocks"][9]
ss9 = z9["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a9 = z9["metadata"]["strikePrice"]
aa9 = z9["metadata"]["optionType"]
d9= z9["metadata"]["numberOfContractsTraded"]
v9 = z9['metadata']['totalTurnover']
p9 = z9["metadata"]["lastPrice"]
c9= z9["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]
i9= z9["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']

z10 = acb["stocks"][10]
ss10 = z10["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a10 = z10["metadata"]["strikePrice"]
aa10 = z10["metadata"]["optionType"]
d10= z10["metadata"]["numberOfContractsTraded"]
v10 = z10['metadata']['totalTurnover']
p10 = z10["metadata"]["lastPrice"]
c10= z10["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]
i10= z10["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']


z11 = acb["stocks"][11]
ss11 = z11["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a11 = z11["metadata"]["strikePrice"]
aa11 = z11["metadata"]["optionType"]
d11= z11["metadata"]["numberOfContractsTraded"]
v11 = z11['metadata']['totalTurnover']
p11 = z11["metadata"]["lastPrice"]
i11= z11["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c11= z11["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]


z12 = acb["stocks"][12]
ss12 = z12["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a12 = z12["metadata"]["strikePrice"]
aa12 = z12["metadata"]["optionType"]
d12= z12["metadata"]["numberOfContractsTraded"]
v12 = z12['metadata']['totalTurnover']
p12 = z12["metadata"]["lastPrice"]
c12= z12["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]
i12= z12["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']




z13 = acb["stocks"][13]
ss13 = z13["marketDeptOrderBook"]["tradeInfo"]["openInterest"]
a13 = z13["metadata"]["strikePrice"]
aa13 = z13["metadata"]["optionType"]
d13= z13["metadata"]["numberOfContractsTraded"]
v13 = z13['metadata']['totalTurnover']
p13 = z13["metadata"]["lastPrice"]
i13= z13["marketDeptOrderBook"]["otherInfo"]['impliedVolatility']
c13= z13["marketDeptOrderBook"]["tradeInfo"]["changeinOpenInterest"]












f=ds.append([a,aa,p,ss,c,i,d,v])

f=ds.append([a1,aa1,p1,ss1,c1,i1,d1,v1])

f=ds.append([a2,aa2,p2,ss2,c2,i2,d2,v2])
f=ds.append([a3,aa3,p3,ss3,c3,i3,d3,v3])
f=ds.append([a4,aa4,p4,ss4,c4,i4,d4,v4])
f=ds.append([a5,aa5,p5,ss5,c5,i5,d5,v5])

f=ds.append([a6,aa6,p6,ss6,c6,i6,d6,v6])
f=ds.append([a7,aa7,p7,ss7,c7,i7,d7,v7])
f=ds.append([a8,aa8,p8,ss8,c8,i8,d8,v8])
f=ds.append([a9,aa9,p8,ss9,c9,i9,d9,v9])
f=ds.append([a10,aa10,p10,ss10,c10,i10,d10,v10])
f=ds.append([a11,aa11,p11,ss11,c11,i11,d11,v11])

f=ds.append([a12,aa12,p12,ss12,c12,i12,d12,v12])
f=ds.append([a13,aa13,p13,ss13,c13,i13,d13,v13])




cols=['STRIKE','OPTION','LAST',"OI","CHIN","IV",'VOLUME','VALUE']
        

dss=pd.DataFrame(ds,columns=cols)  



url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

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
oph = opd.iloc[-67:-9] 




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
print("|----------------------------------[",xx['name'],"]----------------------------|")

print (dss)
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





    
    
    











    
   
   
     
    



















