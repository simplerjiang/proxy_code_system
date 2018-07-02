#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from ctypes import *
import time
import datetime

def encipher(v, k): #加密
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        sum.value += delta
        y.value += ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        z.value += ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

def decipher(v, k): #解密
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        z.value -= ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        y.value -= ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        sum.value -= delta
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

if __name__ == "__main__":
    key1 = [30,32,21,14] #加密key，对照setting.py文件中的TEA_KEY
    key2 = [1,2,3,4] #加密key2，如果开启了TEA_ABLE_SECOND，对照setting.py文件中的TEA_KEY2
    v = [1621154517, 3814202980] #网页返回的加密值
    enc = decipher(v,key2) #解密步骤1，先用key2
    print(enc)
    enc = decipher(enc, key1) #解密步骤2，用key1
    print(enc)
    unix_ts = enc[0] #这就是unix时间戳
    times = datetime.datetime.fromtimestamp(unix_ts) #解时间戳
    print(times)