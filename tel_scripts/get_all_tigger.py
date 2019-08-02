#!/bin/env python
# -*- coding:utf-8 -*-
# Created by ZhangTao on 2019/5/26.

'''脚本结果： 从zabbix中获取当前所有的报警出来,
通过zabbix的API接口来实现功能的调用
'''

from pyzabbix import ZabbixAPI

def get_one_site():


    USERNAME = "zhangtao"
    PASSWORD = "123456"
    ZABBXI_URL = "http://192.168.10.30/zabbix"

    zapi = ZabbixAPI(ZABBXI_URL)
    zapi.login(USERNAME, PASSWORD)


    zjson = zapi.trigger.get(output=["triggerid",
                                     "description",
                                     "priority"
                                     ],
                             filter={"value": 1

                                     },
                             sortfield="priority", sortorder="DESC", only_true="extend", active=1, monitored=1,
                             selectHosts=["host"],
                             selectLastEvent=["clock"],
                             selectGroups=["groupid", "name"],
                             selectItems=["prevvalue", "units", "value_type", "lastvalue"], expandData=1, limit=300)
    tg_list = []
    for i in zjson:

        tg_host = i['hosts'][0]['host']
        tg_name = i['description']
        tg_dict =[tg_host,tg_name]

        tg_list.append(tg_dict)

    return tg_list




if __name__ == '__main__':
    print(get_one_site())