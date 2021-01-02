'''
Python處理時間和日期方面的模組，主要就是datetime、time、calendar三個模組的使用
'''

import time
import datetime
import calendar

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

print("!!!!")
print(time.strftime("%Y-%m-%d_%H-%M", time.localtime()))
print("!!!!")
'''
#TODO:獲取日曆相關資訊
# 獲取某個月的日曆，返回字串型別
calendar.setfirstweekday(calendar.SUNDAY) # 設定日曆的第一天
cal = calendar.month(2020, 12)
# print (cal)

# 獲取一年的日曆
cal = calendar.calendar(2020)
print(cal)
'''
'''
# TODO:calendar模組還可以處理閏年的問題
# 判斷是否閏年
print (calendar.isleap(2012)) #答：2012年是閏年。
# 兩個年份之間閏年的個數
print (calendar.leapdays(2010, 2020))
'''
'''
#TODO:兩日期相減 
d1 = datetime.datetime(2020, 12, 31) 
d2 = datetime.datetime(2020, 12, 1) 
print ((d1 - d2).days)
'''
'''
#TODO:執行時間： 
starttime = datetime.datetime.now() 
# print(starttime)
endtime = datetime.datetime.now() 
# print(repr(endtime))
# print(endtime)
print ((endtime - starttime).seconds)
#Note
while True:
    starttime = datetime.datetime.now()
    endtime = datetime.datetime(2020, 12, 29, 20, 28, 00, 936802) 
    print ((endtime - starttime).seconds)
    time_left = (endtime - starttime).seconds
    if time_left == 0:
        print("Happy New Year")
        break
'''
'''
# TODO:計算當前時間向後10天的時間。 (如果是小時 days 換成 hours )
d1 = datetime.datetime.now() 
d3 = d1+datetime.timedelta(days =10) 
print(d1)
print (str(d3)) 
print (d3.ctime())
'''
print(time.ctime()) #顯示當前的時間。
print(time.strftime("%Y-%m-%d %X",time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.mktime(datetime.datetime(2020,12,29).timetuple())) # 將日期轉化為秒

cc=[2020,12,29,21,00,00] #Attributes: year, month, day, hour, minute, second
print(time.mktime(datetime.datetime(cc[0],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple()))

print(time.time()) #取得當前時間；
print(time.localtime()) #取得本地時間；
print(time.strftime(str(time.localtime()))) #格式化日期；

timeString = time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
print(time.strptime(timeString)) # 把字串轉化為日期；

print(datetime.datetime(2020,12,31).weekday()) # 判斷輸入的日期是星期幾

print(datetime.datetime.utcnow()) # datetime模組獲取當前時間
print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) # 格式化