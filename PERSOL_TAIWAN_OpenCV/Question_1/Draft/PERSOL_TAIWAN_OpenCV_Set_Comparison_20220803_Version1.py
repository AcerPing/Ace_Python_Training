#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import pandas as pd
from matplotlib import pyplot as plt
import os
import datetime
import time
# %matplotlib inline

if __name__ == '__main__':
    
    print('▼ Start from ' + str(datetime.datetime.now()) + '▼')
    
    # 切換檔案主路徑
    main_path = r'D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV'
    save_path = os.path.join(main_path, 'Comparison_Red')
    os.chdir(main_path)
    
    if not os.path.isdir(save_path): os.mkdir(save_path) # 建立儲存資料夾
    # 刪除既有檔案(更新)
    if os.path.isfile(os.path.join(save_path, 'set_red.jpg')): 
        os.remove(os.path.join(save_path, 'set_red.jpg'))
        print(f"Deleted {os.path.join(save_path, 'set_red.jpg')}")
    if os.path.isfile(os.path.join(save_path, 'set_red.xlsx')): 
        os.remove(os.path.join(save_path, 'set_red.xlsx'))
        print(f"Deleted {os.path.join(save_path, 'set_red.xlsx')}")
    if os.path.isfile(os.path.join(save_path, 'set_red.csv')): 
        os.remove(os.path.join(save_path, 'set_red.csv'))
        print(f"Deleted {os.path.join(save_path, 'set_red.csv')}")
    
    window_title = os.path.split(main_path)[-1] # 視窗標提
    camera_control = cv2.VideoCapture(0) # 攝像頭
    
    #攝像頭是否開啟
    if not camera_control.isOpened(): 
        print("Cannot open camera") #攝像頭沒有開啟
        print("Please open the camera. 攝像頭未開啟")
        # sys.exit(1)
        raise Exception('Camera No Image')
    
    # 開始讀取影像
    play_pause = 1
    confirm_img = ''
    while camera_control.isOpened() and confirm_img.upper() != 'Y':
        while camera_control.isOpened():
            success, img = camera_control.read() #cv2讀取攝像頭
            
            if not success: #，是否成功讀取、
                print("cannot receive image from camera.")
                print("Please open the camera. 攝像頭未開啟")
                raise Exception('Camera No Image')
          
            cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE) # 命名一個視窗，可不寫
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 彩色轉灰階
            cv2.imshow(window_title, img) #顯示讀取到的畫面
            
            user_press_key = cv2.waitKey(play_pause) # 等待用戶按鍵觸發，同時給圖像繪製留下時間，若等待時間用戶沒有按下按鍵則繼續循環
            
            if user_press_key == ord('q') or user_press_key == 27: # ord()→返回對應的ASCII數值 # ESC
                print('Please wait and Check image.')  
                
                camera_control.release() # 釋放攝像頭裝置
                cv2.destroyWindow(window_title) # 關閉所有視窗
                
                # 輸出圖片
                cv2.imwrite(os.path.join(save_path, 'set_red.jpg'), img, [cv2.IMWRITE_JPEG_OPTIMIZE])
                time.sleep(10)
                
                break
            elif user_press_key == 13: 
                play_pause = play_pause ^ 1 # 二進位算 # 按位异或运算符：当两对应的二进位相异时，结果为1
            
            elif user_press_key != -1: 
                print(f'用戶按鍵：{user_press_key}')
        
        img = cv2.imread(os.path.join(save_path, 'set_red.jpg'))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR轉成RGB
        plt.xticks([]) # 關閉X坐標軸
        plt.yticks([]) # 關閉Y坐標軸
        plt.imshow(img)
        plt.show()
        confirm_img = input('請確認照片是否設定為紅色：')
        if confirm_img.upper() == 'Y': 
            plt.close()
            break
        
    print('Saving Image, Please Wait') 
    time.sleep(5)
    plt.close('all')
    cv2.destroyAllWindows()
    time.sleep(5)
    # 匯出csv、excel
    # type(img) → <class 'numpy.ndarray'>
    img = cv2.imread(os.path.join(save_path, 'set_red.jpg'))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    df_red = pd.DataFrame(img)
    df_red.to_excel(os.path.join(save_path, 'set_red.xlsx'), sheet_name='set_red', index=False, header=False)
    df_red.to_csv(os.path.join(save_path, 'set_red.csv'), index=False, header=None)
    
    print('▲ End at' + str(datetime.datetime.now()) + ' ▲')
    
'''
< Reference >
Python 與 OpenCV 基本讀取、顯示與儲存圖片教學
https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/

'''