import cv2
import numpy as np
import codecs

m1 = cv2.imread("homework2.png",1) #讀取homework2.png原始圖像

#TODO:因原始檔中的文字為B:G:R=0:0:255，因此先減去B:G:R=255:255:254，再乘上255，讓字體變為純白色
m2 = np. full(m1.shape,(255,255,254),np.uint8) 
m3 = cv2.subtract(m1,m2) #先剪除藍、綠(m1-m2)
cv2.imwrite("D:/Python_Summarize/Python_Training/hw-image/m3.jpg",m3,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m3存檔

#此時只剩字體，B:G:R=0:0:1，乘上255
m4 = np. full(m3.shape,255,np.uint8) 
m5 = cv2.multiply(m3,m4)
cv2.imwrite("D:/Python_Summarize/Python_Training/hw-image/m5.jpg",m5,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m5存檔

m6 = cv2.bitwise_not(m5) #m5各像素值再二進位表示下做not運算
m6 = cv2.cvtColor(m6,cv2.COLOR_BGR2GRAY) #轉換類型，灰階
cv2.imwrite("D:/Python_Summarize/Python_Training/hw-image/m6.jpg",m6,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m6存檔

#TODO:此時檢測文字，文字的顏色為B:G:R=179:179:179，因此改採減去B:G:R=179:179:179，將文字顏色變為純黑色(B:G:R=0:0:0)後，再乘上某一個數值，使做白底黑字
m7 = np. full(m1.shape,179,np.uint8) 
m7 = cv2.cvtColor(m7,cv2.COLOR_BGR2GRAY) 
m8 = cv2.subtract(m6,m7) #減去B:G:R=179:179:179
cv2.imwrite("D:/Python_Summarize/Python_Training/hw-image/m8.jpg",m8,[cv2.IMWRITE_JPEG_QUALITY,100]) #將m8存檔
m9 = np. full(m8.shape,5,np.uint8) #再乘上某一個數值(EX.B:G:R=5:5:5)
m10 = cv2.multiply(m8,m9)
cv2.imwrite("D:/Python_Summarize/Python_Training/hw-image/m10.jpg",m10,[cv2.IMWRITE_JPEG_QUALITY,100]) #得出白底黑字

# cv2.imshow("img 1",m1) #原始圖像
# cv2.imshow("img 2",m2) #剪除藍、綠
# cv2.imshow("img 3",m3) #剪除藍、綠後的結果
# cv2.imshow("img 4",m4) #乘上255
# cv2.imshow("img 5",m5) #乘上255後的結果
# cv2.imshow("img 6",m6) #各像素值再二進位表示下做not運算
# cv2.imshow("img 8",m8) #減去B:G:R=179:179:179的結果
cv2.imshow("img 10",m10) #最終結果，得出白底黑字
cv2.waitKey() #等待按鍵繼續執行
cv2.destroyAllWindows #關閉所有視窗