'''
Python處理時間和日期方面的模組，主要就是datetime、time、calendar三個模組的使用
'''

import time
import datetime

'''
#TODO:TIME 獲取到此時的準確時間
# print(type(time.localtime()))
print("獲取到此時的準確時間",time.localtime())
# print(time.localtime().tm_mday)
'''
'''
#TODO:DATETIME 獲取當天的日期
print(datetime.datetime.now())
print("當天的日期",datetime.date.today())
'''
'''
#TODO:獲取昨天的日期
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    # print (type(today))  # 檢視獲取到時間的型別
    # print (type(yesterday))
    return yesterday
yesterday = getYesterday()
print ("昨天的時間：", yesterday)
'''
'''
#TODO:字串轉換為時間和日期
# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(time.strftime("%Y-%m-%d", time.localtime()))
print(type(time.strftime("%Y-%m-%d", time.localtime())))
print(strTodatetime("2014-3-1","%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(type(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
print(strTodatetime("2005-2-16","%Y-%m-%d")-strTodatetime("2004-12-31","%Y-%m-%d"))
'''