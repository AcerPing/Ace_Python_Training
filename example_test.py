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
# 第十題
def a(V1):
    def b(V2):
        return V1**V2
    return b
a1=a(5)
print(a1(3))
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

# TODO:3-7本章習題
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
'''
#TODO:6.6本章習題   
#第一題
def s(n):
    s = 0
    for i in range(1,n+1):
        s+=i/(i+1)
    # print(s)
    return s
# s = (1/2)+(2/3)+(3/4)+(4/5)
# print(s)
def main():
    # n = int(input("請輸入:"))
    for n in range (1,21):
        print(n,":","\t",s(n))   
main()

#第三題
def distance(x1,y1,x2,y2):
   return ((x2-x1)**2+(y2-y1)**2)**0.5
# print(distance(1,1,10,10))
def main():
    x1=int(input("請輸入坐標軸第一點的x:"))
    y1=int(input("請輸入坐標軸第一點的y:"))
    x2=int(input("請輸入坐標軸第二點的x:"))
    y2=int(input("請輸入坐標軸第二點的y:"))
    print(distance(x1,y1,x2,y2))
    main()
main()

#第四題
def temperature(start,end):
    for F in range(start,end+5,5):
        C = (F-32)*5/9  
        print("華氏:",F,":","\t",C)
def main():
    start = int(input("請輸入華氏起始溫度:"))
    end = int(input("請輸入華氏結束溫度:"))
    temperature(start,end)
main()

#第五題
#小柯的票設為x
#小丁的票設為y
#小姚的票設為z
x = 0
y = 0
z = 0
drop = 0
def menu(candidate):
    global x,y,z,drop
    if candidate == "小柯":
        x+=1
    if candidate == "小丁":
        y+=1
    if candidate == "小姚":
        z+=1
    else:
        drop+=1
    print("小柯的票:",x,"\t",
        "小丁的票:",y,"\t",
        "小姚的票:",z,"\t",
        "廢票:",drop)
def main():
    t = 0
    while t < 10:
        candidate = input("請投下候選人:")
        print("第幾次投票:",t+1)
        menu(candidate)
        t+=1
main()
'''
'''
# TODO:7.7本章習題
# 第一題
def count_the_letter(write_list, write_letter):
    times = 0
    for letter in write_list:
        # print(letter)
        if letter == write_letter:
            times += 1
    return times
def main():
    write_list = input("請輸入字串:")
    write_letter = input("請輸入字母:")
    return count_the_letter(write_list,write_letter)
print(main())

# 第五題
def reverse(string):
    list=[]
    for i in range(len(string)-1,-1,-1):
        list.append(string[i])
    return "".join(list)
def main():
    string = input("請輸入字串:")
    return reverse(string)
print(main())
'''
'''
# TODO:8.9本章習題
# 第一題
import random
#提示使用者簽選六個大樂透號碼
time_yours=0
your_lotto = []
while time_yours < 6:
    your_number = int(input("請簽選大樂透號碼:"))
    if your_number > 49:
        print("此號碼大於49號，不可圈選!")
    elif your_number not in your_lotto:
        your_lotto.append(your_number)
        time_yours += 1
    elif your_number in your_lotto:
        print("此號碼已圈選")
your_lotto.sort()
print("你簽選的大樂透號碼:",your_lotto)
#以隨機亂數產生器產生大樂透號碼(1~49)
time_g = 0
goverment_lotto = []
while time_g < 6:
    goverment_number = random.randint(1,49)
    if goverment_number not in goverment_lotto:
        goverment_lotto.append(goverment_number)
        time_g += 1
    else:
        pass
goverment_lotto.sort()
print("電腦產生的大樂透號碼:",goverment_lotto)
#簽對了幾個號碼
result_list = []
correct = 0
for result_number in your_lotto:
    if result_number in goverment_lotto:
        result_list.append(result_number)
        correct += 1
    else:
        pass
print("你簽對的號碼:",result_list)
print("你簽對了幾個號碼:",correct)

# 第二題
import random
#在biggest函式中找出最大值的元素及其索引
def biggest(numList):
    maximum,idx = max(numList),numList.index(max(numList))
    return "最大值:"+str(maximum),"索引:"+str(idx+1)
#在randomNum函式中以亂數產生器產生100個介於1~100個亂數，並置放於名為numList串列
def randomNum():
    numList = []
    time = 0
    while time < 100:
        number = random.randint(1,100)
        numList.append(number)
        time += 1
    numList.sort()
    print(numList)
    return biggest(numList) #pass list to biggest()
print(randomNum())

# 第三題
#編列學生的分數於串列
score = int(input("請輸入學生的成績:"))
list = []
while score > 0:
    list.append(score)
    score = int(input("請輸入學生的成績:"))
greatest = max(list) #找出最佳的學生分數Best
#以不定數迴圈讀取學生的分數
for i,point in enumerate(list):
    if point >= greatest-5:
        grade = "A"
    elif point >= greatest-15:
        grade = "B"
    elif point >= greatest-25:
        grade = "C" 
    elif point >= greatest-35:
        grade = "D"
    else:
        grade = "F"
    print("第幾位學生:"+str(i+1)," ",
        "該位學生成績:"+str(point)," ",
        "其等級是:"+grade)

# 第四題
#以亂數產生器產生100個介於1到49的亂數
import random
time = 0
list = []
while time < 100:
    number = random.randint(1,49)
    list.append(number)
    time += 1
list.sort()
#並計算每個數出現的個數
for catergory in range(1,50,1):
    print("第幾位數字:"+str(catergory),"出現幾次:"+str(list.count(catergory)))
# print(len(list))

# 第五題
import random
#在createNum函式以隨機亂數產生器產生100個1至50的數字，然後將其置放於numbers串列
def createNum():
    time = 0
    numbers = []
    while time < 100:
        num = random.randint(1,50)
        numbers.append(num)
        time += 1
    numbers.sort()
    return mean(numbers)
#之後再將此串列分別傳給mean函式以計算其平均值
def mean(numbers):
    average = sum(numbers)/len(numbers)
    return average
print(createNum())
'''
'''
# TODO:9.5本章習題
# 第一題
lst44=[
    [11,2,3,14],
    [5,16,7,8],
    [9,10,11,12],
    [3,2,5,1]]
smallest = 9999999 #先令最小值為9999999
for col in range(len(lst44[0])):
    sum = 0
    for row in range(len(lst44)):
        # print(lst44[row][col])
        sum += lst44[row][col]
    print("第幾行",col,"總和",sum)
    if sum < smallest: #如果總和小於smallest，則將此元素指定給smallest
        smallest = sum
        idx_col = col
print("最小值是多少",smallest)
print("哪一行的總和最小",idx_col)

# 第二題
#提示使用者輸入二為串列的列數與行數，然後以亂數產生器產生數字並指定給串列
import random
lst=[]
rows = int(input("How many rows:"))
columns = int(input("How many columns:"))
for i in range(rows):
    lst.append([])
    for col in range(columns):
        number = random.randint(1,100)
        lst[i].append(number)
print("原始的串列:",lst)
#將串列中若是偶數，則將其數字加倍
for row in range(len(lst)):
    # print(lst[row])
    for col in range(len(lst[row])):
        # print(lst[row][col])
        if lst[row][col] % 2 == 0:
            lst[row][col] = lst[row][col]*2
print("新的串列:",lst)

# 第三題
#學生的答案(由亂數產生器產生)
import random
rows = int(input("有幾位學生:"))
questions = int(input("有幾個問題:"))
lst = []
for i in range(rows):
    lst.append([])
    for j in range(questions):
        answer = random.choice(["A","B","C","E","F"])
        lst[i].append(answer)
print(lst)
#標準答案(由亂數產生器產生)
standAns = []
for q in range(questions):
    standAns.append(random.choice(["A","B","C","E","F"]))
print("正確答案",standAns)
#核對答案
for row in range(len(lst)):
    # print(lst[row])
    correct = 0
    for col in range(len(lst[row])):
        # print(lst[row][col])
        if lst[row][col] == standAns[col]:
            correct += 1
    print("第幾位學生",row,"答對幾題",correct)

# 第四題
#產生一個6*6的二維串列，其元素不是0，就是1
import random
lst66 = []
for i in range(0,6,1):
    lst66.append([])
    for j in range(0,6,1):
        lst66[i].append(random.randint(0,1))
print(lst66)
#檢視每一行是否有偶數的1
for rows in range(len(lst66)):
    sum = 0
    # cols = None
    for cols in range(len(lst66[rows])):
        sum += lst66[rows][cols]
    # print(sum)
    if sum % 2 == 0 and sum != 0:
        print("第幾行有偶數的one:",rows,"\t","加總:",sum)
print("-----"*20)
#檢視每一列是否有偶數的1
for col in range(len(lst66[0])):
    sum = 0
    for row in range(len(lst66)):
        # print(lst66[row][col],end="")
        sum += lst66[row][col]
    if sum % 2 == 0 and sum != 0:
        print("第幾列有偶數的one:",col,"\t","總和:",sum)
'''
'''
# TODO:10.8本章習題
# 第一題
import codecs
list = []
for number in range(1,101,1):
    list.append(number)
# print(list)
with codecs.open("example_10-8.txt","w") as file:
    file.write(str(list))
with codecs.open("example_10-8.txt","r") as file:
    print(file.read())

# 第二題
import codecs,os
#提示使用者輸入檔名
fn = input("請輸入檔名及類型:")
#檢查檔案是否存在
if os.path.isfile(fn):
    with codecs.open(fn,"r",encoding="utf-8") as file:
        content = file.read()
        print(content)
    #提示使用者輸入欲被取代的字串及取代的字串
    old_string = input("請輸入欲被取代的字串:")
    new_string = input("請輸入取代的字串:")
    new_content = content.replace(old_string,new_string)
    with codecs.open(fn,"w",encoding="utf-8") as file:
        file.write(new_content)
    #印出最後的檔案內容
    with codecs.open(fn,"r",encoding="utf-8") as file:
        print(file.read())
else:
    print("檔案不存在")

# 第三題
import codecs,os
#提示使用者輸入檔名
fn = input("請輸入檔名及類型:")
#檢查檔案是否存在
if os.path.isfile(fn):
    #讀取檔案內的分數
    with codecs.open(fn,"r",encoding="utf-8") as file:
        content = file.read()
#分析檔案的內容
content = content.split(", ")
print(content)
#計算
total = 0
for number in content:
    # print(number)
    total += int(number)
print("計算其總和:",total)
print("計算其平均數:",total/len(content))

# 第五題
try:
    a = int(input("請輸入三角形的A邊:"))
    b = int(input("請輸入三角形的B邊:"))
    c = int(input("請輸入三角形的C邊:"))
    A = a**2
    B = b**2
    C = c**2
    if A+B>C and A+C>B and B+C>A :
        print("是個三角形")
    else:
        print("RuntimeError")
except ValueError:
    print("ValueError")
'''
'''
# TODO:11.5本章習題
# 第二題
import codecs
#提示使用者輸入含有文字檔的檔名
fn = input("請輸入含有文字檔的檔名:")
#從中讀取字
with codecs.open(fn,"r",encoding="utf-8") as file:
    content = file.read()
#「換行」→" "
content = content.replace("\r\n"," ")
#全部變為小寫
content = content.lower()
#字跟字之間切開成list
content = content.split(" ")
#由小到大排序
content.sort()
print("重複的單字",content)
#顯使沒有重複的單字
lst = []
for letter in content:
    if letter not in lst:
        lst.append(letter)
    else:
        pass
print("沒有重複的單字",lst)

# 第三題
#讀取任意個數的整數
number = input("請輸入任意整數的個數:")
#數字之間以空白隔開
number = number.split( )
# print("〔轉譯〕您所輸入的個數",number)
dic = {}
for n in number:
    if n not in dic:
        dic[n] = number.count(n)
print("〔轉譯〕您所輸入的字典",dic)
dic_tuple = sorted(dic.items(),key=lambda item: item[1],reverse=True)
print("排序後的字典",dic_tuple)
#找出出現最多次數的整數
# max_number = max(dic,key=dic.get) #法一:返回最大值的键值
max_value = max(dic.values())
print("出現最多次數的整數:",end="") 
for m , n in dic_tuple:
    #若出現最多次數的整數不只一個時，則要一併印出
    if n == max_value:
        print(m,end=" ")

# 第五題
import os
dic = {}
#建立一個辭典選單
def menu():
    global x
    print("辭典選單\r\n"
        "(0)結束\r\n"
        "(1)加入\r\n"
        "(2)刪除\r\n"
        "(3)顯示\r\n"
        "(4)修改\r\n")
    #讓使用者輸入選項後加以執行其相對應的動作
    try:
        x = int(input("請輸入辭典選單:"))
        return x
    except:
        print("請輸入整數!!!")
        print("===="*20)
        menu()
menu()
while x != 0:
    #加入的選項
    if x == 1:
        print("目前的字典:",dic)
        keyword = input("請輸入欲加入的keys:")
        if keyword not in dic:
            values = input("請輸入欲加入的values:")
            dic[keyword] = values
            print("====="*20)
            print("已加入該keys")
        elif keyword in dic:
            print("====="*20)
            print("該keys已存在字典中")
        print("====="*20)
        menu()
    #刪除的選項
    elif x == 2:
        print("目前的字典:",dic)
        keyword = input("請輸入欲刪除的keys:")
        if keyword in dic:
            del dic[keyword]
            print("已刪除該keys")
        elif keyword not in dic:
            print("====="*20)
            print("該keys不存在字典中")
        print("====="*20)
        menu()
    #顯示的選項
    elif x == 3:
        print("目前的字典:",dic)
        print("====="*20)
        menu()
    #修改的選項
    elif x == 4:
        print("目前的字典:",dic)
        keyword = input("請輸入欲修改的keys:")
        if keyword in dic:
            values = input("請輸入欲修改的values:")
            dic[keyword] = values
            print("已修改該keys")
        elif keyword not in dic:
            print("====="*20)
            print("該keys不存在字典中")
        print("====="*20)
        menu()
#結束的選項
if x == 0:
    os.system("cls")
'''
'''
# TODO:12.7本章習題
# 第一題
class Stack:
    def __init__(self,items=[]):
        self.items = items
    #push函式用以加入一元素
    def push(self,values):
        self.items.append(values)
        print(values,"已加入")
    #isEmpty函式用以判斷是否為空的
    def isEmpty(self):
        return self.items == 0
    #pop函式刪除元素
    def pop(self):
        if self.isEmpty() == True:
            print("Empty")
        else :
            self.items.pop()
    #getSize函式用以得到大小
    def getSize(self):
        return len(self.items)
stackObj = Stack()
for i in range(1,6):
    stackObj.push(i)
print(stackObj.items)

# 第二、三、四題
class Shape:
    #其中Shape有一資料成員color，用以表示三角形的顏色
    def __init__(self,color="Red"):
        self.color = color
    #取得三角形的顏色
    # def getColor(self):
    #     return self.color
    # #印出三角形的顏色
    # def printColor(self):
    #     print(self.color)
    #設定三角形的顏色
    # def setColor(self,color):
    #     self.color = color
#Triangle的類別繼承Shape類別
class Triangle(Shape):
    #有三個三邊之資料成員
    def __init__(self,a,b,c):
        super().__init__()
        self.length1 = a
        self.length2 = b
        self.length3 = c
    #取得三邊的資料
    def getColor(self):
        return self.length1, self.length2, self.length3
    #計算周長
    def around(self):
        return self.length1 + self.length2 + self.length3
    #印出三角形顏色
    def printColor(self):
        print("三角形顏色:",self.color)
    #設定三角形的顏色
    def setColor(self,color):
        self.color = color

    def length(self):
        print("邊長一:",self.length1,"邊長二:",self.length2,"邊長三:",self.length3)

A = int(input("請輸入三角形的A邊:"))
B = int(input("請輸入三角形的B邊:"))
C = int(input("請輸入三角形的C邊:"))
if A+B>C and A+C>B and B+C>A :
    triangle = Triangle(a=A,b=B,c=C)
    triangle.printColor()
    triangle.setColor(color="blue")
    triangle.printColor()
    triangle.length()
    print(triangle.around())
else:
    print("Invalid")
    raise RuntimeError()
'''
'''
# TODO:13.4本章習題
# 第一題
import numpy as np
#產生一個從1到9的3*3矩陣
np1 = np.array(range(1,10,1))
np1 = np1.reshape([3,3])
print("np1的矩陣:\r\n",np1)
#產生一個從9到1的3*3矩陣
np2 = np.array(range(9,0,-1))
np2 = np2.reshape([3,3])
print("np2的矩陣:\r\n",np2)
#將此兩矩陣相乘並顯示結果
print("相乘後的結果:\r\n",np1.dot(np2))

# 第二題
import numpy as np
#產生一個從1到200之間偶數的10*10矩陣
np2 = np.array(range(2,201,2))
np2 = np2.reshape([10,10])
print("np2偶數矩陣:\r\n",np2)
print()
#產生一個從1到200之間奇數的10*10矩陣
np1 = np.array(range(1,201,2))
np1 = np1.reshape([10,10])
print("np1奇數矩陣:\r\n",np1)
print()
print("====="*20,"\r\n","交換後","\r\n","====="*20)
print()
#將此兩矩陣相互交換
np1, np2 = np2, np1
print("np2矩陣:\r\n",np2)
print()
print("np1矩陣:\r\n",np1)
'''


    



        







    






