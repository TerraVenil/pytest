#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd
from zipline.api import order, record, symbol
from zipline.algorithm import TradingAlgorithm

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'Close'))

algor_obj = TradingAlgorithm(initialize=initialize, handle_data=handle_data)

data_s = pd.read_csv('./AAPL.csv', parse_dates=['Date'], index_col=0)
data_c = pd.Panel({'AAPL': data_s})

perf_manual = algor_obj.run(data_c)
perf_manual.to_csv('./output.csv')
