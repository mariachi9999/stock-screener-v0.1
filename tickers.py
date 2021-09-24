#import csv

#file = open('./Tickers.csv')
#type(file)
#csvreader = csv.reader(file)
#print(csvreader)
import pandas as pd

tickers = []
data = pd.read_excel(r"C:\Users\Usuario\Documents\projects\stock-screener-v0.1\EtoroStocksExcel.xlsx")

for ticker in data['TickerAdj']:
    tickers.append(ticker)

print(tickers)