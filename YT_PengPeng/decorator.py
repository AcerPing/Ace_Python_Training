# 裝飾器 Decorator -> 特殊設計的函式，用來「輔助」其他的函式

'''
# 定義裝飾器
def testDecorator(Callback_Fuction): # def 裝飾器名稱(回呼函式名稱):
    def execute(): # def 內部函式名稱():
        # 裝飾器內部的程式碼
        print("Decorator Function")
        Callback_Fuction("data") #!!! 這個回呼函式，其實就是被裝飾的普通函式 #回呼函式名稱
    return execute # return 內部函式名稱

# 使用裝飾器
@testDecorator # @裝飾器名稱
def main(data):
    print("Normal Function")
    print("data:{}".format(data))

main()
'''

# TODO: 定義一個裝飾器，計算1-50的總和
def calculator(Callback_Function):
    def calculate():
        sum=0
        for i in range(1,51):
            sum+=i
        # print(sum)
        Callback_Function(sum)
    return calculate

#使用裝飾器
@calculator
def show(data):
    print("計算總和: {}".format(data))
show()

@calculator
def show_English(data):
    print("Result: {}".format(data))
show_English()


