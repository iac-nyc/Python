#!/usr/bin/env python
#hw: 6.1
#Iftekhar Chowdhury

stock_prices_file = "C:\Users\Iftekhar Chowdhury\Desktop\Python\stock_prices.csv"

lines = open(stock_prices_file).readlines()[1:]

def by_closeopen(line):
    val = line.split(',')
    final = float(val[5])- float(val[2])
    return final

for line in sorted(lines, key = by_closeopen, reverse = True)[0:5]:
    line = line.rstrip()
    ticker,date,open,high,low,close,volume = line.split(',')
    print '{} ({}):  {} - {}'.format(ticker,date,open,close)
    
