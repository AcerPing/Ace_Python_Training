#TODO:載入pandas模組
import pandas as pd

'''
#TODO:建立series
data = pd.Series([20,10,15])
'''
'''
#TODO:基本series操作
print(data)
print("Max:",data.max())
print("Median:",data.median())
data = data*2
print(data)
data=data==20
print(data)
'''

#TODO:建立DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[3000,5000,4000]
})
#TODO:基本DataFrame操作
print(data)
#取得特定的欄位
# print(data["name"])
#取得特定的列
print("="*20)
print(data.iloc[0]) #印出第一列