#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

import LoadMySql as lms

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-s %(message)s')

def getNextFiveMinutes(date) :
    pass

def merge(data) :
    data['date'] = lms.combineTime(data['DTYYYYMMDD'], data['TIME'], 0)
    data['date'] = lms.convertDate(data['date'])
    return data

def main() :

    file='/backup/USDCAD.bak.txt'
    reader = pd.read_csv(file, sep=',', encoding='UTF-8', iterator=True)

    data = reader.get_chunk(30000)
    data = merge(data)
    close = data['CLOSE'].values

    output1 = talib.SMA(close, 500)
    output2 = talib.SMA(output1, 500)
    output3 = talib.SMA(output2, 500)

    plt.plot(close, label="CLOSE")
    plt.plot(output1, label='MA1')
    plt.plot(output2, label='MA2')
    plt.plot(output3, label='MA3')

    plt.show()

if __name__ == '__main__' :
    main()