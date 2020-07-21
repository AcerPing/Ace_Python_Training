import cv2
import numpy as np

m1 = cv2.imread("homework2.png",1) #讀取homework2.png原始圖像

#TODO:減去紅色+雜質的圖片
m1[:,:,2]  = cv2.subtract(m1[:,:,2], m1[:,:,0]) #R-B，變為二維圖片
m2 = cv2.subtract(m1[:,:,2],m1[:,:,1]) #R-G (二維圖片)

m2 = cv2.subtract(m2,np.full(m2.shape,254,np.uint8)) #R為254以下的圖片減去254後變為0
m2 = cv2.multiply(m2,np.full(m2.shape,255,np.uint8)) #0乘上255後還是0(黑)，1乘上255後變為255(白)

m2 = cv2.bitwise_not(m2) #黑白顛倒

cv2.imshow("img 1",m2) #最終結果，得出白底黑字
cv2.waitKey() #等待按鍵繼續執行
cv2.destroyAllWindows #關閉所有視窗
