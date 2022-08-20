import pandas as pd
#TODO:讀取資料
data = pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
#TODO:觀察資料
# print(data)
print("資料數量:",data.shape)
print("資料欄位:",data.columns)
print("===="*20)
'''
#TODO:分析資料(評分的各種數據)
condition=data["Rating"]<=5
data = data[condition]
print(data)
# print(data["Rating"])
print("平均數:",data["Rating"].mean())
print("取得前一千個應用程式的平均數:",data["Rating"].nlargest(1000).mean())
print("中位數:",data["Rating"].median())
'''
'''
#TODO:分析資料(安裝數量的各種統計數據)
# print(data['Installs'][10472])
data['Installs'] = pd.to_numeric(data['Installs'].str.replace("[,+]","").replace("Free",""))
print(data['Installs'])
print("平均數:",data['Installs'].mean())
condition = data['Installs'] > 100000
print("安裝數量大於100,000的應用程式有幾個:",data[condition].shape[0])
'''
#TODO:基於資料的應用(關鍵字搜尋應用程式的名稱)
keyword = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyword,case=False)
print(data[condition]["App"])
print("包含關鍵字的應用程式數量:",data[condition].shape[0])
