import os, sys, argparse
import pandas as pd 
import backtrader as bt 
import matplotlib as plt 
from strategies.au_cross import AU_Cross
from strategies.BuyHold import BuyHold

strategies = {
    "au_cross": AU_Cross, 
    "buy_hold": BuyHold

}

parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies: 
    print("invalid strategy, must be one of {}".format(strategies.keys()))
    sys.exit()

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('data/SPY.csv', index_col="Date", parse_dates=True)
msft_prices = pd.read_csv('data/MSFT.csv', index_col="Date", parse_dates=True)
apd_prices = pd.read_csv('data/APD.csv', index_col="Date", parse_dates=True)

feed = bt.feeds.PandasData(dataname=msft_prices)
cerebro.adddata(feed)

cerebro.addstrategy(strategies[args.strategy])
cerebro.run()
cerebro.plot()