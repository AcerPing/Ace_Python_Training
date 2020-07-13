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
'''
#1-6本章習題
print("半徑為5的圓形周長",5*2*3.1416)
print("寬為3、長為9的矩形面積",3*9)
print("寬為3、長為9的矩形周長",(3+9)*2)
print("10英呎等於幾公分",10*2.54)
print("攝氏26度等於華氏幾度",26*(9/5)+32)
'''

'''
#2-5本章習題
width = int(input("請輸入矩形的長:"))
height = int(input("請輸入矩形的寬:"))
area = width * height
print("面積:",area)
周長 = (width + height) * 2
print("周長:",周長)
'''

#TODO:3-7本章習題
'''
#第一題
a = int(input("請輸入三角形的一個邊:"))
b = int(input("請輸入三角形的一個邊:"))
c = int(input("請輸入三角形的一個邊:"))
if a + b > c or a + c > b or b + c > a:
    print("是三角形")
else:
    print("不是三角形")

#第二題
x = int(input("請輸入x座標點:"))
y = int(input("請輸入y座標點:"))
if ((x-0)**2+(y-0)**2)**0.5 < 10:
    print("在圓內")
else:
    print("不在圓內")
'''
'''
#TODO:4.7本章習題
#第一題
i = 0
sum = 0
while i < 101:
    sum+=i
    i+=2
print(sum)

#第二題-1
sum = 0
for x in range (0,101,5):
    sum+=x
print(sum)

#第二題-2
sum =0
i = 0
while i < 101:
    sum+=i
    i+=5
print(sum)

#第三題
for i in range(1,10,1):
    for j in range(1,i+1):
        print(i*j,end="  ")
    print("\n")

#第四題
for i in range(6,0,-1):
    print("*" * i)

#第五題
for i in range(1,10,1):
    for j in range(1,i+1):
        print(1*j,end="  ")
    print("\n")

import random
list = []
while len(list)<49:
    number = random.randint(1,49)
    list.append(number)
print(list)
'''
'''
#TODO:5.4本章習題   
#第一題-1
total = 0
for i in range(1,6,1):
    a = int(input("Enter a number:"))
    total+=a
print(total)

#第一題-2
total = 0
for i in range(0,10000000):
    a = int(input("Enter a number:"))
    if a!= -999:
        total+=a
    else:
        break
print(total)

#第三題
import random
list=[]
odd = 0
even = 0
ten = 0
for i in range(1,1001):
    number = random.randint(1,200)
    list.append(number)
    if number % 2 ==0:
        even +=1
    elif number % 2 !=0:
        odd +=1

for math in list:
    if math %5 ==0:
        ten +=1

print("list:",list)
print("偶數:",even)
print("奇數:",odd)
print("5的倍數:",ten)
'''




