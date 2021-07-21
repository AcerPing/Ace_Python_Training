'''
今天要設計一款判斷是否為閏年的程式
是否為閏年，其條件為：
西元年份除以4不可整除，為平年。
西元年份除以4可整除，且除以100不可整除，為閏年。
西元年份除以100可整除，且除以400不可整除，為平年
西元年份除以400可整除，為閏年。

說明:
輸入為一組西元年，請根據以上規則判斷是否為閏年，若為閏年請回傳True，否則False
'''

in_txt = 2002

if int(in_txt) % 4 != 0: print(False)
elif (int(in_txt) % 100 == 0) and (int(in_txt) % 400 != 0): print(False)
elif (int(in_txt) % 4 == 0) and (int(in_txt) % 100 != 0): print(True)
elif (int(in_txt) % 400 == 0): print(True)
else: raise Exception('演算法錯誤')

