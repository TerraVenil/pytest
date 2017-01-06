#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import sys
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
def combineTime(yyyymmdd,time,count):
    result = []
    num = count
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

#插入数据库
def loadData2mysql(data, count) :
    sql = "insert into his_data(id,ticker,period,date,open,high,low,close,vol,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    try:
        conn = MySQLdb.connect("120.27.92.201", "root", "Best12167", "forex")
        cur = conn.cursor()

        conn.select_db('forex')

        values = []
        for i in range(len(data)):
            value = []
            value.append(uuid.uuid4())
            value.append(data['TICKER'][i + count])
            value.append('SECOND')
            value.append(data['date'][i + count])
            value.append(data['OPEN'][i + count])
            value.append(data['HIGH'][i + count])
            value.append(data['LOW'][i + count])
            value.append(data['CLOSE'][i + count])
            value.append(data['VOL'][i + count])
            values.append(value)

        cur.executemany(sql, values)
        conn.commit()
        logging.info("插入条数：" + str(len(values)))

        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def main(file) :
    logging.info("开始读取数据")
    reader = pd.read_csv(file, sep=',', encoding='UTF-8', iterator=True)
    loop = True
    count = 0
    while loop :
        subdata = reader.get_chunk(200)
        subdata['date'] = combineTime(subdata['DTYYYYMMDD'], subdata['TIME'], count)
        subdata['date'] = convertDate(subdata['date'])

        logging.info("读取数据完毕:" + str(len(subdata)))
        loadData2mysql(subdata, count)
        logging.info("插入数据完毕:" + str(len(subdata)))

        count += len(subdata)

        if len(subdata) < 200: loop = False

    logging.info("插入数据完毕!共插入:" + str(count))


if __name__ == '__main__' :
    file = ''
    if len(sys.argv) == 2 :
        file = sys.argv[1]
    else :
        file = '/backup/USDCAD.txt'
    main(file)