#!/bin/env python
# -*- coding:utf-8 -*-
# Created by ZhangTao on 2019/5/26.

'''获取最新报警并触发报警'''

import pymysql
import json
import requests
import time
import datetime
import json
import requests


'''从数据库中取出当前所有的实时报警数据'''




'''调用电话API接口 拨打电话'''
def get_code():
    host = 'http://yuyin1.market.alicloudapi.com'
    path = '/dx/voice_send'
    appcode = '96e04dd24c9c4b129ec2a33f7040fa2b'
    querys = 'code=code%3A123456&phone=13233543678'
    url = host + path + '?' + querys
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
         'Authorization': "APPCODE 96e04dd24c9c4b129ec2a33f7040fa2b"
        }

    response = requests.request("POST", url, headers=headers)

    respnse_text = response.json()
    print("开始拨打电话")
    return respnse_text


'''调用钉钉接口报警发送钉钉群信息'''
def sendmessage(message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5e7f04c094fea1f3b802950d0ac4a386d2c84341c45875dde755b386adda7112'  # 钉钉机器人的webhook地址
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = message
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "13233543678"  #
            ],
            "isAtAll": 2  #
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)


'''获取当前报警'''
def select_tig_db():
    conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
    cursor = conn.cursor()
    sql1 = "select * from 2_now_alert"
    cursor.execute(sql1)
    results = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    return results


'''获取规则列表'''
def get_db_guize():
    conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
    cursor = conn.cursor()
    sql1 = "select * from alert_level"
    cursor.execute(sql1)
    results = cursor.fetchall()    #获取查询的所有记录

    conn.commit()
    cursor.close()
    conn.close()

    return results



'''插入数据'''
'''找出 2_now 这张表和 un 这张表的差距, 
如果 2_now中的数据 在 un 中不存在就添加到un中
'''
def duibi():
    # 获取 实时报警页面列表
    now_alert1 = []
    now_alert = select_tig_db()
    for i in now_alert:
        ip = i[1]
        name = i[2]
        now_data = [ip,name]
        now_alert1.append(now_data)

    ## 获取 现在 un 数据库中的数据

    un_alert1 = []
    conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
                           charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT * FROM university"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    results = cursor.fetchall()


    for x in results:
        un_ip = x[3]
        un_name = x[4]
        un_data = [un_ip,un_name]
        un_alert1.append(un_data)

    # 开始对比 now_alert1   un_alert1 的差集,将 un_alert1 比较 now_alert1 没有的增加进去

    chazhi_list = []
    for i in now_alert1:
        if i not in un_alert1:
            chazhi_list.append(i)




    for j in chazhi_list:
        ipaddress = j[0]
        alertname = j[1]
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        media = "电话"
        tel_log = "成功拨打电话"
        conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
                                    charset="utf8")
        cursor = conn.cursor()
        sql1 = "INSERT INTO university(hostname,tigger,media,tel_log,queren,createdat,updatedat) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
         ipaddress, alertname, media, media, tel_log, nowTime, nowTime)


        cursor.execute(sql1)
        conn.commit()
        cursor.close()


'''拨打完成后的逻辑处理'''
def chufa():
    now_all_alert = select_tig_db()
    guize = get_db_guize()

    for i in guize:
        guanjianzi = (i[1])
        for j in now_all_alert:
            # print(j)
            if guanjianzi in j[2]:
                print("111")
                conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
                                       charset="utf8")
                cursor = conn.cursor()

                sql2 = "SELECT * FROM university"
                cursor.execute(sql2)
                conn.commit()
                cursor.close()
                results1 = cursor.fetchall()
                for j in results1:
                    queren = j[7]
                    print(queren)
                    if queren == "2":
                        print(get_code())

                        print("拨打电话接口成功")
                        duibi()

                        # 开始修改queren字段

                        print("添加数据库成功")

print(chufa())


