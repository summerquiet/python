#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import ntplib
import os,datetime

hosts = ['0.cn.pool.ntp.org','1.cn.pool.ntp.org','2.cn.pool.ntp.org','3.cn.pool.ntp.org']

def ntp_client():
    #创建实例，NTPClient()是一个类
    t = ntplib.NTPClient()
    for host in hosts:
        try:
            #ntp server可以填写主机和域名，建议用域名
            #缺省端口为ntp， 版本为2， 超时为5s
            #作用：查询 NTP 服务器，并返回对象
            r = t.request(host , port='ntp', version=4, timeout=5)
            if r:
                break
        except Exception as e:
            pass
    #显示的是时间戳
    t = r.tx_time
    print("NPT time:", t)

    #使用datetime模块,格式化：x年x月x日 时:分:秒.毫秒
    _date,_time = str(datetime.datetime.fromtimestamp(t))[:22].split(' ')

    print("NPT time:", _date, _time)
    '''
    print("调整前时间是：", datetime.datetime.now())
    os.system('date {} && time {}'.format(_date, _time))
    print("调整后时间是：", datetime.datetime.now())
    '''

if __name__ == '__main__':
    #适用于Windows
    ntp_client()
