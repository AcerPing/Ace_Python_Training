import random
import pandas as pd

#TODO:下載商工開放平台的公司統編csv ，選擇一類下載
def read_csv():
    df = pd.read_csv('D:\Python_Summarize\Python_Training\HW_HiTRUST/202010.csv') #讀取csv檔
    print(df) #顯示公司設立登記清冊(月份)
    # print(df.shape[0]) #整張資料的長度(資料筆數)與寬度(欄位數量)
    # print(df["統一編號"]) #抓取"統一編號"的column
    row = df.shape[0] #整張資料的長度(資料筆數)
    random_row = random.randint(0,row) #隨機從資料筆數中抽取一筆資料
    print(df["統一編號"][random_row]) #顯示這筆資料的統一編號
    tax_ID_number = df["統一編號"][random_row]
    return tax_ID_number
