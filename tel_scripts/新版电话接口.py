# #!/bin/env python
# # -*- coding:utf-8 -*-
# # Created by ZhangTao on 2019/5/26.
# 
# '''获取最新报警并触发报警'''
# 
# import pymysql
# import json
# import requests
# import time
# import datetime
# import json
# import requests
# 
# 
# '''从数据库中取出当前所有的实时报警数据'''
# 
# 
# 
# 
# '''调用电话API接口 拨打电话'''
# def get_code():
#     host = 'http://yuyin1.market.alicloudapi.com'
#     path = '/dx/voice_send'
#     appcode = '96e04dd24c9c4b129ec2a33f7040fa2b'
#     querys = 'code=code%3A123456&phone=15518935198'
#     url = host + path + '?' + querys
#     headers = {
#         'Content-Type': "application/json",
#         'cache-control': "no-cache",
#          'Authorization': "APPCODE 96e04dd24c9c4b129ec2a33f7040fa2b"
#         }
# 
#     response = requests.request("POST", url, headers=headers)
# 
#     respnse_text = response.json()
#     return respnse_text
# 
# 
# '''调用钉钉接口报警发送钉钉群信息'''
# def sendmessage(message):
#     url = 'https://oapi.dingtalk.com/robot/send?access_token=5e7f04c094fea1f3b802950d0ac4a386d2c84341c45875dde755b386adda7112'  # 钉钉机器人的webhook地址
#     HEADERS = {
#         "Content-Type": "application/json ;charset=utf-8 "
#     }
#     message = message
#     String_textMsg = {
#         "msgtype": "text",
#         "text": {"content": message},
#         "at": {
#             "atMobiles": [
#                 "13233543678"  #
#             ],
#             "isAtAll": 2  #
#         }
#     }
#     String_textMsg = json.dumps(String_textMsg)
#     res = requests.post(url, data=String_textMsg, headers=HEADERS)
#     print(res.text)
# 
# 
# '''获取当前报警'''
# def select_tig_db():
#     conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
#     cursor = conn.cursor()
#     sql1 = "select * from 2_now_alert"
#     cursor.execute(sql1)
#     results = cursor.fetchall()
# 
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return results
# 
# 
# '''获取规则列表'''
# def get_db_guize():
#     conn = pymysql.connect(host="192.168.11.166", user ="root", password ="zhangtao", database ="tig_db3", charset ="utf8")
#     cursor = conn.cursor()
#     sql1 = "select * from alert_level"
#     cursor.execute(sql1)
#     results = cursor.fetchall()    #获取查询的所有记录
# 
#     conn.commit()
#     cursor.close()
#     conn.close()
# 
#     return results
# 
# 
# def chufa():
#     now_alert = select_tig_db()  # 当前所有的报警列表
#     guize = get_db_guize()  # 所有的规则列表
#     for i in now_alert:
#         now_ip = (i[1])
#         now_alert = i[2]
# 
#         for j in guize:
# 
#             if str(j[1]) in now_alert:
#                 return "ok",now_alert,now_ip
# 
# queren,chufa_result,now_ip = (chufa())
# 
# if  queren== "ok":
#     conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
#                        charset="utf8")
#     cursor = conn.cursor()
#     sql = "SELECT * FROM university"
#     cursor.execute(sql)
#     conn.commit()
#     cursor.close()
#     results = cursor.fetchall()
# 
#     # DB un表中的数据
#     db_alrt_list = []
#     for i in results:
#         db_alert = str(i[4]) # 数据库中的报警
#         db_alrt_list.append(db_alert)
# 
#         if chufa_result == db_alert:
#             print("存在")
# 
# 
#         if chufa_result != db_alert:
#             nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             media = "电话"
#             tel_log = "成功拨打电话"
#             conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
#                                        charset="utf8")
#             cursor = conn.cursor()
#             sql1 = "INSERT INTO university(hostname,tigger,media,tel_log,queren,createdat,updatedat) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
#                 now_ip, chufa_result, media, tel_log, 0, nowTime, nowTime)
# 
# 
#             cursor.execute(sql1)
#             conn.commit()
#             cursor.close()
#             print("添加成功","报警名称为",chufa_result)
# 
# 
#
import requests
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

print(get_code())