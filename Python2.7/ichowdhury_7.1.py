#!/usr/bin/env python
#hw:7.1

stock_prices_file = "C:\Users\Iftekhar Chowdhury\Desktop\Python\stock_prices.csv"

lines = open(stock_prices_file).readlines()[1:]

by_closeopen = lambda x: float(x.split(',')[5-2])

for line in sorted(lines, key = by_closeopen, reverse = True)[0:5]:
    line = line.rstrip()
    ticker,date,open,high,low,close,volume = line.split(',')
    print '{} ({}):  {} - {}'.format(ticker,date,open,close)
