#TODO:多維陣列維度/形狀操作
import numpy as np #載入numpy套件
'''
#TODO:觀察資料形狀
data = np.ones(10)
print(data)

data = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(data.shape)
'''
'''
#TODO:資料轉置
data = np.array([
    [1,3,4],
    [5,6,8]
])
print(data.shape)
print(data.T.shape)
'''
'''
#TODO:扁平化資料
data = np.array([
    [[[1,2,3,4]],
    [[5,6,7,8]],
    [[8,5,2,0]]]
])
newdata = data.ravel()
print(newdata)
print(newdata.shape)
'''
'''
#TODO:重塑資料的形狀
data = np.array([
    [[[1,2,3,4]],
    [[5,6,7,8]],
    [[8,5,2,0]]]
])
print(data.shape) #(1, 3, 1, 4) → 1*3*1*4=12
newdata = data.reshape(4,3)
print(newdata)
'''
#TODO:初始化資料
# data = np.zeros(18).reshape(3,6)
# print(data)
data = np.arange(10).reshape(2,5)
print(data)
print(data.T)