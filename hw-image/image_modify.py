import cv2
import numpy as np

m1 = cv2.imread("homework2.png",1) #讀取一張圖像

m2 = np. full(m1.shape,(255,255,0),np.uint8) 
m3 = cv2.subtract(m1,m2)

cv2.imshow("img 1",m1) #顯示圖片
cv2.imshow("img 2",m2) #顯示圖片
cv2.imshow("img 2",m3) #顯示圖片
cv2.waitKey() #等待按鍵繼續執行
cv2.destroyAllWindows #關閉所有視窗