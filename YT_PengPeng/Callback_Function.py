
def test(arg):
    # print(arg)
    arg("Hello Ping") # 呼叫回呼函式，帶入參數

# 定義一個回呼函式
def handle(data):
    print(data)

test(handle)

'''
def add(n1, n2, cb):
    cb(n1+n2)

def handle1(result):
    print("結果是:", result)

def handle2(result):
    print("結果は:", result)

add(20, 20, handle1)
add(10, 100, handle2)
'''