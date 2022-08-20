#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt 
import pandas as pd
import os, sys
import datetime
import time
import random

def what_red() -> np.array:
    '''
    1. 藉由"Set_Comparison"設定紅色資料 
    2. 讀取存在save_path的紅色矩陣資料 (告訴機器什麼是紅色)
    '''
    comparision_img_red = cv2.imread(os.path.join(save_path, 'set_red.jpg')) # 讀取圖片
    comparision_img_red  = cv2.cvtColor(comparision_img_red , cv2.COLOR_BGR2RGB) # BGR轉成RGB
    plt.xticks([]) # 關閉X坐標軸
    plt.yticks([]) # 關閉Y坐標軸
    plt.imshow(comparision_img_red) # 展示圖片
    plt.show()
    df_red = pd.read_csv(os.path.join(save_path, 'set_red.csv'), header=None)
    if (df_red.shape[0] != comparision_img_red.shape[0]) or (df_red.shape[1] != comparision_img_red.shape[1]): raise Exception ('Pandas讀取錯誤，維度不一致！')  #檢查維度是否一致
    array_comparision_red = np.array(df_red)
    return array_comparision_red

if __name__ == '__main__':
    
    print('▼ Start from ' + str(datetime.datetime.now()) + '▼')
    
    camera_control = None
    array_comparision_red = None
    
    try:
        # 切換檔案主路徑
        main_path = r'D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV'
        save_path = os.path.join(main_path, 'Comparison_Red')
        os.chdir(main_path)
        
        # TODO: 提取比對檔案資料(紅色)
        array_comparision_red = what_red()
        
        # TODO: 在鏡頭前秀出紅色卡片，就會出現音樂(任何音效皆可)；當紅色卡片從鏡頭前消失，音樂馬上會跟著停止
        # 音樂清單
        music_list = os.listdir('D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV\PlayMusic\Japanese_N3')
        
        window_title = os.path.split(main_path)[-1] # 視窗標提
        camera_control = cv2.VideoCapture(0) # 攝像頭
        image_deviation = 10000
        
        #攝像頭是否開啟
        if not camera_control.isOpened(): 
            print("Cannot open camera") #攝像頭沒有開啟
            print("Please open the camera. 攝像頭未開啟")
            raise Exception('Camera No Image')
        
        # 開始讀取影像
        play_pause = 1 # 暫停/繼續錄放
        play_music = None # 音樂撥放是否
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
                break
                
            elif user_press_key == 13: 
                play_pause = play_pause ^ 1 # 二進位算 # 按位异或运算符：当两对应的二进位相异时，结果为1 # 邏輯互斥
                if not play_pause: print('Pause Image') # play_pause == 0
                elif play_pause: print('Continue Play Image') # play_pause == 1
            
            elif user_press_key != -1: 
                print(f'用戶按鍵：{user_press_key}')
                
            # 比對陣列
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 彩色轉灰階
            print(f'Similarity：{abs(np.linalg.norm(img - array_comparision_red))}')
            #檢查維度是否一致
            if img.shape != array_comparision_red.shape: raise Exception ('Pandas讀取錯誤，維度不一致！')  
            if abs(np.linalg.norm(img - array_comparision_red)) <= 10000 : 
                if not play_music:
                    print('撥放音樂 Play Music')
                    os.system(os.path.join('D:\Python_Summarize\Python_Training\PERSOL_TAIWAN_OpenCV\PlayMusic\Japanese_N3', music_list[random.randint(0, len(music_list)-1)]))
                    play_music = True
                else: print('繼續撥放音樂 Continue Play Music')
                time.sleep(10)
            else: 
                if play_music:
                    print('關閉音樂 Stop Music')
                    os.system("taskkill /f /im Music.UI.exe") 
                    play_music = False
          
        print('▲ End at' + str(datetime.datetime.now()) + ' ▲')
        
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        program_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f'Error Program Name: {program_name} ,\r\nError Line: {str(exc_tb.tb_lineno)} ,\r\nError Type: {exc_type} ,\r\nError Reason: {exc_obj}')
        raise Exception(exc_obj)
    
    finally:
        if isinstance(camera_control, cv2.VideoCapture):  # cv2關閉所有視窗
            cv2.destroyAllWindows()
        if isinstance(array_comparision_red, np.ndarray):  # plt關閉所有視窗
            plt.close()
            plt.close('all')


'''
< Reference >

OpenCV-Python学习之(一)waitKey()函数详解
https://blog.csdn.net/a1809032425/article/details/81952952

Python OpenCV 等待按鍵事件 cv2.waitKey
https://shengyu7697.github.io/python-opencv-waitkey/

邏輯互斥(exlusive)
邏輯互斥(xor)，在程式語言中，常寫作p ^ q
https://zh.wikipedia.org/zh-tw/%E9%80%BB%E8%BE%91%E5%BC%82%E6%88%96#%E4%BD%BF%E7%94%A8%E5%BC%82%E6%88%96%E8%BF%90%E7%AE%97%E4%BA%A4%E6%8D%A2%E4%B8%A4%E4%B8%AA_int_%E7%B1%BB%E5%9E%8B%E5%8F%98%E9%87%8F%E7%9A%84%E6%95%B0%E5%80%BC
'''