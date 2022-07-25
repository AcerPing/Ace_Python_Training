# 生成器Generator -> 動態產生可疊代的資料。

# TODO: 定義建立生成器
def test():
    print('階段一')
    yield 5
    print('階段二')
    yield 10
# TODO: 呼叫並回傳生成器
gen = test() # 得到生成器

# TODO:〔方法一〕利用next
# print(next(gen))
# print('----------------')
# print(next(gen))
# TODO:〔方法二〕搭配 for 迴圈中使用
# for 變數名稱 in 生成器: 將生成器產生的資料逐一取出
# for d in gen: print(d)

# TODO: 產生無限多個偶數
def generatorEven(maxnumber):
    number = 0
    while number <= maxnumber:
        yield 2 * number
        number += 1
Even_Generator = generatorEven(20)
for show_number in Even_Generator: print(show_number) 
# for i in range(10): print(next(Even_Generator))
    