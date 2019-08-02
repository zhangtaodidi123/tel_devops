#!/bin/env python
# -*- coding:utf-8 -*-
# Created by ZhangTao on 2019/5/26.

'''第二次更新数据库, 更新'''
import pymysql
from pyzabbix import ZabbixAPI


now = "null"
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



def insert_tig_db():
    tig_list = get_one_site() # 获取报警列表



    conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
    cursor = conn.cursor()
    sql = "delete from 2_now_alert"
    cursor.execute(sql)
    conn.commit()
    cursor.close()


    tig_list = get_one_site() # 获取报警列表

    for i in tig_list:

        tig_host = i[0]
        tig_name = (i[1])

        cursor = conn.cursor()
        sql1 = "INSERT INTO 2_now_alert(ipaddress,alert) VALUES ('%s','%s')" % (tig_host, tig_name)
        cursor.execute(sql1)
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    insert_tig_db()