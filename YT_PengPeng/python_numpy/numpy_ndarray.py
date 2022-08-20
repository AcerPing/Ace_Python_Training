#ndarray:多維陣列/陣列
#載入numpy套件
import numpy as np
'''
#TODO:建立一維陣列
data = np.array([1,2,3,4])
print(data)
data = np.empty(4) #創造一個有四個資料的一維陣列，資料未指定
print(data)
data = np.zeros(3)
print(data)
data = np.ones(3)
print(data)
data = np.arange(8)
print(data)
'''
'''
#TODO:建立二維陣列
#創造一個3*3的二維陣列
data = np.array([[2,3,2],
                [1,5,2],
                [4,2,1]])
print(data)
#創造一個3*3的二維陣列，資料未指定
data = np.empty([3,3])
print(data)
#創造一個2*3的二維陣列，資料都是1
data = np.ones([2,3])
print(data)
#創造一個2*3的二維陣列，資料都是0
data = np.zeros([2,3])
print(data)
'''
'''
#TODO:建立三維陣列
#根據列表創造一個2*2*2的三維陣列
data = np.array([
                [[2,3],[1,5]],
                [[2,3],[1,5]]
                ])
print(data)
#創造一個3*1*3的三維陣列，資料都是0
data = np.zeros([3,1,3])
print(data)
'''
#TODO:建立高維陣列
#創造一個1*1*2*3的四維陣列
data = np.array([
    [
        [
            [2,3,3],
            [1,5,5]
        ],
    ]
])
print(data)
#創造一個2*1*1*2的四維陣列，資料都是1
data = np.ones([2,1,1,2])
print(data)