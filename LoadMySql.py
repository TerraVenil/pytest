#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import MySQLdb
import pandas as pd
import numpy as np
import datetime
import uuid

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-s %(message)s')

#获取指定个数的0
def getZero(num) :
    str = ""
    for i in range(num) :
        str += "0"
    return str

#补全时间前面的0
def completeZero(time) :
    result = ""
    ilen = len(time)
    if(ilen < 6) :
        result = getZero(6 - ilen) + str(time)
    else :
        result = time
    return result

#合并日期和时间
def combineTime(yyyymmdd,time):
    result = []
    num = 0
    for i in yyyymmdd :
        result.append(str(i) + completeZero(str(time[num])))
        num=num+1
    return result

#转换日期格式
def convertDate(time) :
    result = []
    for i in time :
        result.append(datetime.datetime.strptime(i, '%Y%m%d%H%M%S'))
    return result

#读取历史数据
def readData(file) :
    data = pd.read_csv(file, sep=',', encoding='UTF-8')
    data['date'] = combineTime(data['DTYYYYMMDD'], data['TIME'])
    data['date'] = convertDate(data['date'])
    return data

def loadData2mysql(variety,data) :
    sql = "insert into his_data(id,variety,period,date,open,high,low,close,vol,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    try:
        conn = MySQLdb.connect("120.27.92.201", "root", "Best12167", "forex")
        cur = conn.cursor()

        conn.select_db('forex')

        values = []
        num = 0
        for i in range(len(data)):
            value = []
            value.append(uuid.uuid4())
            value.append(variety)
            value.append('MIN')
            value.append(data['date'][i])
            value.append(data['OPEN'][i])
            value.append(data['HIGH'][i])
            value.append(data['LOW'][i])
            value.append(data['CLOSE'][i])
            value.append(data['VOL'][i])
            values.append(value)
            if(num != 0 and num % 100 == 0) :
                cur.executemany(sql, values)
                conn.commit()
                logging.info("插入条数：" + str(len(values)))
                num = 0
                values = []
            num = num + 1
        if(len(values) > 0) :
            cur.executemany(sql, values)
            conn.commit()
            logging.info("插入条数：" + str(len(values)))

        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def main() :
    file = '/backup/USDCAD.bak.txt'
    logging.info("开始读取数据...")
    data = readData(file)
    logging.info("读取数据完毕")
    loadData2mysql('USDCAD', data)
    logging.info("插入数据完毕")

if __name__ == '__main__' :
    main()