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
    aaa = ["test1","test2"]

    for i in aaa:

        tig_host = i[0]  # 当前报警主机名
        tig_name = (i[1]) #当前报警alert名称

        now_alert = [tig_host,tig_name]



        # print("当前报警为",now_alert)
        '''目前数据库中的报警情况'''

        conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
        cursor = conn.cursor()
        sql = "SELECT * FROM university"
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()


        for j in results:
            db_name = j[3]  # 当前报警主机名
            db_alert = (j[4])  # 当前报警alert名称
            db_now = [db_name,db_alert]
            print("当前数据库的报警为",db_now)

            if now_alert == db_now:
                print("存在,不进行insert操作")
            else:
                print("不存在，开始添加数据库")
                conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
                cursor = conn.cursor()
                sql1 = "INSERT INTO university(hostname,tigger) VALUES ('%s','%s')" %(tig_host,tig_name)
                cursor.execute(sql1)
                conn.commit()
                cursor.close()
                conn.close()


if __name__ == '__main__':
    insert_tig_db()