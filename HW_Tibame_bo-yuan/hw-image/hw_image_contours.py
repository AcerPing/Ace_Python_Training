import cv2
import numpy as np


#TODO(1.):開啟影像
camera = cv2.VideoCapture("homework3.mp4")

while camera.isOpened()==True:
    ret,m1=camera.read()
    if ret == True:
        # cv2.imshow("Image 1",m1)
        m2 = cv2.inRange(m1,(78,78,0),(200,200,83)) 
        m2 = cv2.dilate(m2,np.ones((80,100)))
        a,b = cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        for i in range(0,len(a)):
            x,y,w,h = cv2.boundingRect(a[i]) 
            if w > h*2: #當寬度>高度的3倍時
                cv2.rectangle(m1, (x,y), (x+w,y+h), (0,0,255), 2) #繪矩形
        cv2.imshow("Image 1",m1)

                # cv2.imwrite("Video/"+str(i)+".png",m1)
                # pass
        if cv2.waitKey(33) != -1:
            break	
    else:
        break

cv2.destroyAllWindows()

'''
#TODO(2.):辨析圖片
m1 = cv2.imread("homework3_Moment.jpg",1) #讀取原稿圖片
m2 = cv2.inRange(m1,(0,0,0),(255,80,80)) #抓取藍筆的顏色(inrange)，為二階色澤 (在範圍內的像素會被設白色，否為則黑色)
m2 = cv2.dilate(m2,np.ones((20,20))) #將藍色部分擴張
# cv2.imwrite("test_m2.jpg",m2)

a,b = cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
m3 = np.full(m1.shape,255,np.uint8) #製作一張白紙
for i in range(0,len(a)):
    x,y,w,h = cv2.boundingRect(a[i]) #取得包覆指定輪廓點的最小正矩形
    # print(a)
    # print(b)
    # print(x,y,w,h)
    cv2.rectangle(m3, (x,y), (x+w,y+h), (100,100,100), 2)
    cv2.imwrite("Video/"+str(i)+".png",m3[y:y+h,x:x+w])



cv2.imshow("Image",m2)
# cv2.imshow("consequence",m3)

cv2.waitKey()
cv2.destroyAllWindows()

'''
'''
(Question)
# m2 = cv2.inRange(m2,0,50) #抓取黑色的部分，使之變為白色
# m2 = cv2.erode(m2,np.ones((10,10))) #稍微修飾，將黑筆的部分擴張
# m2 = cv2.bitwise_not(m2)
# m2 = cv2.cvtColor(m2,cv2.COLOR_GRAY2BGR)
'''