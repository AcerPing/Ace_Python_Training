
def decorator_factory(data): # def 裝飾器工廠名稱 (參數名稱):
    def my_decorator(callback): # def 裝飾器名稱 (回呼函式名稱):
        def inner_function(): # def 內部函式名稱():
            print(data) # 裝飾器內部程式碼
            result = data *10 
            callback(result) # 回呼函式名稱
        return inner_function # return 內部函式名稱
    return my_decorator # return 裝飾器名稱

@decorator_factory(6666) # @ 裝飾器工廠名稱 (參數名稱)
def main(result): # def 函式名稱():
    print(result) # 函式內部的程式碼

main() # 呼叫帶有裝飾器的函式



# TODO: 定義一個裝飾器，計算1-max的總和
def calculate_factory(max):
    def calculator(Callback_Function):
        def calculate():
            sum=0
            for i in range(1,max+1):
                sum+=i
            # print(sum)
            Callback_Function(sum)
        return calculate
    return calculator

#使用裝飾器
@calculate_factory(200)
def show(data):
    print("計算總和: {}".format(data))
show()

@calculate_factory(500)
def show_English(data):
    print("Result: {}".format(data))
show_English()
