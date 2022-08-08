#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv("BTC-USDT_alligator_ADX.csv")
#data = data.sort_index(ascending=False)
#data.to_csv("BTC-USDT_alligator_ADX_reorder.csv")
print("data read")

def stratergy1(data):
    FIAT = 1000.0
    fb = FIAT
    BTC = 0.0
    isbuy = 0
    buy_price = 0
    sell_price = 0
    stop_loss = 0
    stop_loss_ratio = 0.98
    trading_fee=0.2
    diff = 0
    win=0
    loss=0
    profit =[]
    profit_x=[]
    losses = []
    losses_x= []
    stop_losses = []
    stop_losses_x = []
    loss = 0
    count = 0
    i = 0
    initial_BTC =FIAT/10391.77
    hold_value=0
    for ind in data.index:
        if ind>300:
            if data["EMA100"][ind]> data["EMA200"][ind]:
                if (data["ADX"][ind]>40 or 1) and isbuy==0:
                    BTC = FIAT/data["close"][ind]
                    isbuy=1
                    FIAT = 0
                    buy_price = data["close"][ind]
                    stop_loss = stop_loss_ratio*data["close"][ind]
            if data["EMA100"][ind]<= data["EMA200"][ind] :
                if isbuy==1:
                    isbuy=0
                    count+=1
                    sell_price = data["close"][ind]
                    diff = (sell_price-buy_price)*BTC
                    FIAT = BTC*data["close"][ind]
                    fb = FIAT
                    BTC = 0
                    #profit["transaction_"+str(count)] = diff
                    hold_value = data["close"][ind]*initial_BTC
                    #print("current value: "+str(FIAT)+"\t\t hold value: "+str(hold_value))
                    if diff>=0:
                        profit.append(diff)
                        profit_x.append(ind)
                        win+=1
                    else:
                        losses.append(diff)
                        losses_x.append(ind)
                        loss+=1
            #print(data["close"][ind]-buy_price)
            if data["close"][ind]<=0.9*buy_price and isbuy==1 :
                isbuy=0
                count+=1
                sell_price = data["close"][ind]
                diff = (sell_price-buy_price)*BTC
                FIAT = BTC*data["close"][ind]
                fb = FIAT
                BTC = 0
                #profit["transaction_"+str(count)] = diff
                #print("below stoploss")
                hold_value = data["close"][ind]*initial_BTC
                #print("current value: "+str(FIAT)+"\t\t hold value: "+str(hold_value))
                if diff>=0:
                    profit.append(diff)
                    profit_x.append(ind)
                    #print("hii")
                    win+=1
                else:
                    stop_losses.append(diff)
                    stop_losses_x.append(ind)
                    #print(len(stop_losses))
                    loss+=1

    print(fb)
    cb = FIAT + BTC*data["close"][ind]
    print("current calue "+str(fb)+"\t\t hold value: "+str(hold_value))

    return profit,losses,stop_losses,profit_x,losses_x,stop_losses_x

pf,ls,sls,pfx,lsx,slsx = stratergy1(data)
print(len(data.index))
print("profit: "+str(len(pf)))
print("loss: "+str(len(ls)))
print(len(sls))
print(sum(pf))
print(sum(ls)+sum(sls))
#print(sum(sls))

plt.figure(figsize=(12.2,4.5))
plt.scatter(pfx,pf,color="green")
plt.scatter(lsx,ls,color="orange")
plt.scatter(slsx,sls,color="red")
#plt.set_xlabel("index")
#plt.set_ylabel("value")
#plt.set_title('scatter plot')
plt.show()
