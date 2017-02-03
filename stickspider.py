#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
import ssl
import json
import logging
import logging.handlers
import time
import sys

def getLogger(loggerFile) :
    handler = logging.handlers.RotatingFileHandler(loggerFile + '.log', maxBytes=1024 * 1024, backupCount=5)
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    handler.setFormatter(logging.Formatter(fmt))

    logger = logging.getLogger('sticklog')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def getTicketMsg(train_date):
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + train_date + '&leftTicketDTO.from_station=NFF&leftTicketDTO.to_station=NJH&purpose_codes=ADULT'
    req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'})
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    message = urllib2.urlopen(req, context=gcontext).read()
    train = json.loads(message, encoding='UTF-8')
    data = train['data'][0]['queryLeftNewDTO']
    wz_num = u' 无座: ' + data['wz_num']
    yz_num = u' 硬座: ' + data['yz_num']
    yw_num = u' 硬卧: ' + data['yw_num']
    rw_num = u' 软卧: ' + data['rw_num']
    msg = '[' + train_date + ']' + data['start_station_name'] + u'->' + data['to_station_name'] + wz_num + yz_num + yw_num + rw_num
    return data['yw_num'],data['rw_num'],msg

if __name__ == '__main__' :
    train_date = ''
    if len(sys.argv) == 2:
        train_date = sys.argv[1]
    else:
        train_date = '2017-03-03'
    logger = getLogger(train_date)
    while True :
        msg = getTicketMsg(train_date)
        if msg[0] != u'无' :
            logger.info(u'硬卧有啦----------------')
        if msg[1] != u'无' :
            logger.info(u'软卧有啦----------------')
        logger.info(msg[2])
        time.sleep(5)
