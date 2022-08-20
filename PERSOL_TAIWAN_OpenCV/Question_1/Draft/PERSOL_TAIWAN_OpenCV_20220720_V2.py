#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt 
import pandas as pd
import os, sys

# 切換檔案主路徑
main_path = r'D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV'
save_path = os.path.join(main_path, 'Comparison_Red')
os.chdir(main_path)

# TODO: 提取比對檔案資料(紅色)
comparision_img_red = cv2.imread(os.path.join(save_path, 'set_red.jpg'))
comparision_img_red  = cv2.cvtColor(comparision_img_red , cv2.COLOR_BGR2RGB) # BGR轉成RGB
plt.xticks([])
plt.yticks([])
plt.imshow(comparision_img_red)
plt.show()
df_red = pd.read_csv(os.path.join(save_path, 'set_red.csv'), header=None)
if (df_red.shape[0] != comparision_img_red.shape[0]) or (df_red.shape[1] != comparision_img_red.shape[1]): raise Exception ('Pandas讀取錯誤，維度不一致！')  #檢查維度是否一致
array_comparision_red = np.array(df_red)

# TODO: 在鏡頭前秀出紅色卡片，就會出現音樂(任何音效皆可)；當紅色卡片從鏡頭前消失，音樂馬上會跟著停止

window_title = os.path.split(main_path)[-1] # 視窗標提
camera_control = cv2.VideoCapture(0) # 攝像頭
image_deviation = 10000

#攝像頭是否開啟
if not camera_control.isOpened(): 
    print("Cannot open camera") #攝像頭沒有開啟
    print("Please open the camera. 攝像頭未開啟")
    raise Exception('Camera No Image')

# 開始讀取影像
play_pause = 1
while camera_control.isOpened():
    success, img = camera_control.read() #cv2讀取攝像頭
    
    if not success: #，是否成功讀取、
        print("cannot receive image from camera.")
        print("Please open the camera. 攝像頭未開啟")
        raise Exception('Camera No Image')
  
    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL) # 命名一個視窗，可不寫 # #cv2.WINDOW_AUTOSIZE
    cv2.imshow(window_title, img) #顯示讀取到的畫面
    
    user_press_key = cv2.waitKey(play_pause) # 等待用戶按鍵觸發，同時給圖像繪製留下時間，若等待時間用戶沒有按下按鍵則繼續循環
    
    if user_press_key == ord('q') or user_press_key == 27: # ord()→返回對應的ASCII數值 # ESC
        print('exit')  
        
        camera_control.release() # 釋放攝像頭裝置
        cv2.destroyWindow(window_title) # 關閉視窗
        
        sys.exit()
    elif user_press_key == 13: 
        play_pause = play_pause ^ 1 # 二進位算 # 按位异或运算符：当两对应的二进位相异时，结果为1
    
    elif user_press_key != -1: 
        print(f'用戶按鍵：{user_press_key}')
        
    # 比對陣列
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 彩色轉灰階
    print(f'Similarity：{abs(np.linalg.norm(img - array_comparision_red))}')
    #檢查維度是否一致
    if img.shape != array_comparision_red.shape: raise Exception ('Pandas讀取錯誤，維度不一致！')  
    if abs(np.linalg.norm(img - array_comparision_red)) < 10000 : 
        print('撥放音樂')
        os.system('D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV\play.mp3')
        os.system("taskkill /f /im Music.UI.exe") 
    
print(type(img)) # <class 'numpy.ndarray'>
pd.DataFrame(np.array(img))

plt.close()
plt.close('all')


'''
< Reference >

OpenCV-Python学习之(一)waitKey()函数详解
https://blog.csdn.net/a1809032425/article/details/81952952

Python OpenCV 等待按鍵事件 cv2.waitKey
https://shengyu7697.github.io/python-opencv-waitkey/
'''