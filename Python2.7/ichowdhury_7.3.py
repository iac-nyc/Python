#!/usr/bin/env python

##hw:7.3
##Iftekhar Chowdhury

stock_prices_file = "C:\Users\Iftekhar Chowdhury\Desktop\Python\stock_prices.csv"

lines = open(stock_prices_file).readlines()[1:]

ticker_dict = {}
for line in lines:
    els = line.split(',')
    ticker = els[0]
   
    high = float(els[3])
    low = float(els[4])
    close = float(els[5])
    if ticker not in ticker_dict:
        ticker_dict[ticker]=[]
    ticker_dict[ticker].append(close)
    
#sorted_keys = sorted(ticker_dict, key = lambda x:float(max(ticker_dict[x])-min(ticker_dict[x]))

for key in ticker_dict:
    print "{}: Highest Value:{}".format(key, max(ticker_dict[key]))
    print "{}: Lowest Value:{}".format(key,min(ticker_dict[key]))
    print 
    
 
