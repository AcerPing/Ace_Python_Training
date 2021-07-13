# Iterable 資料型態 -> 字串、列表、集合、字典
# for 迴圈 (for 變數名稱 in 可疊代的資料)
'''
# 列表
for x in [5, 3, 2]: print(x)
# 字串
for x in 'abc': print(x)
# 集合
for x in {'a', 'test', 3, 10}: print(x)
# 字典
for key in {'a':'test', 'b':10}: print(key)
dic = {'a':'test', 'b':10}
for key, value in dic.items(): print(value)
for value in dic.values(): print(value)
for key in dic: 
    print(key)
    print(dic[key])

# 內建函式
# max(可疊代資料)
# result_max = max([30, 2, 15, 4])
# result_max = max('xyz')
# result_max = max('何哲平')
# result_max = max({30, 2, 15, 4})
result_max = max({'a':'test', 'b':10})
print(result_max)

# sorted(可疊代資料)
# result_sorted = sorted([30, 2, 15, 4])
# result_sorted = sorted('xyzabc')
# result_sorted = sorted('平哲何')
# result_sorted = sorted({30, 2, 15, 4})
# result_sorted = sorted({'b':10, 'a':'test', 'c':'sorted'})
print(result_sorted)
'''

