#載入pandas模組
import pandas as pd
#TODO:資料索引
data = pd.Series([987,456,321,369,258,741],index=["a","b","c","d","e","f"])
# print(data)
'''
#TODO:觀察資料
print("資料型態:",data.dtype)
print("資料數量:",data.size)
print("資料索引:",data.index)
'''
'''
#TODO:取得資料(根據順序、根據索引)
print(data[3],data[0])
print(data["c"],data["f"])
'''
'''
#TODO:數字運算(基本、統計、順序)
print("最大值:",data.max())
print("總和:",data.sum())
print("標準差:",data.std())
print("中位數:",data.median())
print("最大的三個數:","\n",data.nlargest(3)) 
print("最小的兩個數:","\n",data.nsmallest(2))
'''
data = pd.Series(["您好","pYthon","Pandas"])
'''
#TODO:字串運算(基本、串接、搜尋、取代)
print(data.str.lower()) #全部變成小寫
print(data.str.upper()) #全部變成大寫
print(data.str.len()) #算出每個字串的長度
print("－".join(data)) #把字串串起來，可以自訂串接的符號
print(data.str.cat(sep="-")) #把字串串起來，可以自訂串接的符號
print(data.str.find("n")) #文字裡的值如果要搜尋所在位址
print(data.str.contains("n")) #判斷每個字串是否包含特殊的字元
print(data.str.replace("您好","Hi"))
'''