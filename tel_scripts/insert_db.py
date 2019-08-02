#!/bin/env python
# -*- coding:utf-8 -*-
# Created by ZhangTao on 2019/5/26.


'''把取出来的报警插入到数据库中'''
from tel_scripts.get_all_tigger import *
import pymysql


def insert_tig_db():
    now = "null"
    aaa = get_one_site()  # 把最新的报警取出来
    tig_list = get_one_site() # 获取报警列表

    for i in tig_list:


        tig_host = i[0]
        tig_name = (i[1])

        conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
                               charset="utf8")
        cursor = conn.cursor()
        sql1 = "INSERT INTO 2_now_alert(ipaddress,alert) VALUES ('%s','%s')" % (tig_host, tig_name)
        cursor.execute(sql1)
        conn.commit()
        cursor.close()
        conn.close()



if __name__ == '__main__':
    insert_tig_db()