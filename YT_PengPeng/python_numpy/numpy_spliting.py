#載入Numpy套件
import numpy as np

'''
#準備測試資料
array = np.array([
    [1,3,5,7,9,11,13],
    [2,4,6,8,10,12,14]
]) #2*7

#TODO:根據第一個維度切割
result1 = np.vsplit(array, 2)
print(result1)
# 1*7
    # [[1,3,5,7,9,11,13]],
# 1*7
    # [[2,4,6,8,10,12,14]]
'''
#準備測試資料
array = np.array([
    [1,3,5,7,9,11],
    [2,4,6,8,10,12]
]) #2*6
#TODO:根據第二個維度切割
result2 = np.hsplit(array, 2)
print(result2)
# 2*3
    #[[1,3,5,],[2,4,6,]]
# 2*3
    #[[7,9,11],[8,10,12]]
#TODO:根據第二個維度切割成三個陣列
result3 = np.hsplit(array, 3)
print(result3)
# 2*2
    #[[1,3,],[2,4,]]
# 2*2
    #[[5,7,],[6,8,]]
# 2*2
    #[[9,11],[10,12]]
