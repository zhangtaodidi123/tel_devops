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
#     querys = 'code=code%3A123456&phone=13233543678'
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
#     now_alert = select_tig_db()  #当前所有的报警猎豹
#     guize = get_db_guize()  # 所有的规则列表
#
#
#     for i in now_alert:
#         now_ip = (i[1])
#         now_alert = i[2]
#         now_zabbix_list = [now_ip,now_alert]
#
#         '''查询数据库,关注是否有重复'''
#
#         conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
#                                charset="utf8")
#         cursor = conn.cursor()
#         sql = "SELECT * FROM university"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for j in results:
#             print(j)
#             # web_ip = j[3]
#             # web_alert = j[4]
#             # web_all = [web_ip,web_alert]
#             #
#             # if now_zabbix_list == web_all:
#             #     print("存在")
#             # else:
#             #
#             #     media = "电话"
#             #     tel_log = "没有打"
#             #     conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
#             #                    charset="utf8")
#             #     cursor = conn.cursor()
#             #     sql1 = "INSERT INTO university(hostname,tigger,media,tel_log,queren,createdat,updatedat) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
#             #         i[1], i[2], media, tel_log, 0, 0, 0)
#             #
#             #     cursor.execute(sql1)
#             #     conn.commit()
#             #     cursor.close()
#             #     print("没有发送，添加到数据库中")
#
# chufa()
# #
# #         for j in guize:
# #
# #             guanjianzi = str(j[1])
# #             alert = str(i)
# #             if guanjianzi in alert:
# #
# #                 conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
# #                                        charset="utf8")
# #                 cursor = conn.cursor()
# #                 sql1 = "select * from university WHERE hostname='%s' AND  tigger='%s'" %(i[1],i[2]) # 查询sql语句
# #                 cursor.execute(sql1)
# #                 results = cursor.fetchall()
# #                 conn.commit()
# #                 cursor.close()
# #                 shifouqueren = (results[0][-1])
# #                 print("是否确认已经拆选")
# #                 print(shifouqueren)
# #                 if shifouqueren == "0":
# #                     print("进来啦")
# #                     get_code()
# #                     tel_result = (get_code())
# #                     status_code = (tel_result['return_code'])
# #                     print(tel_result)
# #                     if status_code == '00000':
# #                         print("sucess")
# #                         media = "电话"
# #                         tel_log = "拨打成功"
# #                         conn = pymysql.connect(host="192.168.11.166", user="root", password="zhangtao", database="tig_db3",
# #                                            charset="utf8")
# #                         cursor = conn.cursor()
# #                         sql1 = "INSERT INTO university(hostname,tigger,media,tel_log,queren,createdat,updatedat) VALUES ('%s','%s','%s','%s','%s','%s','%s')" %(i[1],i[2],media,tel_log,0,0,0)
# #
# #                         print(sql1)
# #                         cursor.execute(sql1)
# #                         conn.commit()
# #                         cursor.close()
# #
# #
# #                 else:
# #                     print("failed")
# #         return "done"
# #
# #
# #
# # tel_result = (chufa())
# #
# #
# # def sendmessage(message):
# #     url = 'https://oapi.dingtalk.com/robot/send?access_token=5e7f04c094fea1f3b802950d0ac4a386d2c84341c45875dde755b386adda7112'  # 钉钉机器人的webhook地址
# #     HEADERS = {
# #         "Content-Type": "application/json ;charset=utf-8 "
# #     }
# #     message = message
# #     String_textMsg = {
# #         "msgtype": "text",
# #         "text": {"content": message},
# #         "at": {
# #             "atMobiles": [
# #                 "13233543678"  # 如果需要@某人，这里写他的手机号
# #             ],
# #             "isAtAll": 2  # 如果需要@所有人，这些写1
# #         }
# #     }
# #     String_textMsg = json.dumps(String_textMsg)
# #     res = requests.post(url, data=String_textMsg, headers=HEADERS)
# #     print(res.text)
# #
# # if tel_result == 'done':
# #     # text = "触发电话报警成功,拨打张涛电话"
# #     # print("开始发送钉钉消息")
# #     # sendmessage(text)
# #     print(chufa())
# #
# # #
# #



import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)