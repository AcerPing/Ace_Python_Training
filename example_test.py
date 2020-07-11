'''
#第一題
s=1
def func(a):
    s=2
    a=4

func(s)
print(s)
s=3
func(s)
print(s)
'''
'''
#第二題
count = 12
if count >10:
    count = 11
elif count < 12:
    count = 10
    if count %10 == 0:
        count = 13
    else:
        count = 14

if count == 11:
    count = 10
elif count == 13:
    count = 14

if count %10 == 4:
    count = 13
elif count > 13:
    count = 12
print(count)
'''
'''
#第三題
arr = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    arr[(i+i)%7] = i
    print(i,"  ",arr)
'''
'''
#第四題
def func(a,b):
    s = 0
    if a > b:
        t = a
        a = b
        b = t
        for i in range(0,a):
            for j in range(i,b):
                s+=j
        return s

print(func (7,4))
'''
'''
#第五題
def R(x,y,s):
    t = int((x+y)/2)
    s = s+t
    print(s)
    if x < y:
        if 5 >= t:
            R(t,y,s)
        else:
            R(x,y-5,s)
    else:
        print(s)

R(3,17,0)
'''
'''
#第六題
a = 100
def fn():
    global a
    a = 1
print(a)
fn()
print(a)
'''
'''
#第七題
print(sum(range(0,100)))
'''

#1-6本章習題
print("半徑為5的圓形周長",5*2*3.1416)
print("寬為3、長為9的矩形面積",3*9)
print("寬為3、長為9的矩形周長",(3+9)*2)
print("10英呎等於幾公分",10*2.54)
print("攝氏26度等於華氏幾度",26*(9/5)+32)