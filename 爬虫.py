#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib
import urllib2

data = {'name':'zhangsan','password':'123456'}
param = urllib.urlencode(data)
request = urllib2.Request('http://www.weibo.com', data=param, headers={})
reponse = urllib2.urlopen(request)
print reponse.read()