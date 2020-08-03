#載入pandas模組
import pandas as pd
#TODO:資料索引
#pd.DataFrame(字典,index=索引列表)
data = pd.DataFrame({"name":["Amy","Bob","Cherry"],"Salary":[3000,4000,5000]},index=["a","b",'c'])
print(data)
print("="*20)
'''
#TODO:觀察資料
print("資料數列:",data.size)
print("資料型狀(列,欄):",data.shape)
print("資料索引:",data.index)
'''
'''
#TODO:取得列(ROW/橫向)的Series資料(根據順序,根據索引)
print("取得第二列:",data.iloc[1],sep="\n")
print("="*20)
print("取得第c列:",data.loc["c"],sep="\n")
'''
'''
#TODO:取得欄(column/直向)的Series資料(根據欄位名稱)
print("取得name欄位:",data["name"],sep="\n")
print("="*20)
names = data["name"] #取得單維度的Series資料
print("把names全部轉大寫:",names.str.upper(),sep="\n")
#計算薪水的平均值
salaries = data["Salary"]
print("員工薪水的平均值:",salaries.mean())
'''
'''
#建立新的欄位
data["revenue"]=[50000,40000,30000] #data[新欄位的名稱]=列表
data["rand"]=pd.Series([3,6,1],index=["a","b",'c']) #data[新欄位的名稱]=Series的資料
data["cp"] = data["revenue"]/data["Salary"]
print(data)
'''