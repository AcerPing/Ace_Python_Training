#載入pandas模組
import pandas as pd
'''
#TODO:篩選練習(Series)
data = pd.Series([30,15,20])
# condition = [True,False,True]
condition = data>18
print(condition)
filterData = data[condition]
print(filterData) 

data = pd.Series(["How","are","You"])
# condition = [False,True,True]
condition = data.str.contains("o")
print(condition)
filterData = data[condition]
print(filterData)
'''
'''
#TODO:篩選練習(DataFrame)
data = pd.DataFrame({"name":["Ace","Angela","Rober"],"Salary":[900000,500000,300]})
print(data)
# condition = [True,True,False]
# condition = data["Salary"] > 50000
condition = data["name"]=="Ace"
print(condition)
filterData = data[condition]
print(filterData)
'''
