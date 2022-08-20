# 載入numpy套件
import numpy as np
'''
#TODO:逐元運算(elementwise):針對陣列中的每個資料，逐一進行基本運算
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
result = data1+data2
print("加法:", result)
result = data1*data2
print("乘法:", result)
result = data1>data2
print("大於:", result)
result=data1==data2
print("是否相等:", result)
'''
'''
#TODO:矩陣運算(matrix):針對兩個陣列進行矩陣運算
data1 = np.array([
    [1, 3]
]) #1*2
data2 = np.array([
    [2, -1, 3],
    [-2, 4, 1]
]) #2*3
result = data1.dot(data2) #1*3
print("內積:",result)
result = data1@data2
print("內積:",result)
result = np.outer(data1, data2) #2*6
print("外積:",result)
'''
#TODO:統計運算(statistics):針對單一陣列進行統計運算
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
]) #2*3
result = data.sum()
print("總和:",result)
result = data.max()
print("最大值:",result)
result = data.mean()
print("平均數:",result)
result = data.std()
print("標準差:",result)

result = data.sum(axis=0) #針對欄column做總和 / 針對第一個維度做總和
print(result)
result = data.sum(axis=1) #針對列row做總和 / 針對第二個維度做總和
print(result)
result = data.max(axis=0)
print(result)
result = data.mean(axis=1)
print(result)

result = data.cumsum(axis=0) #針對欄column做逐值累加 / 針對第一個維度做逐值累加
print(result)