# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:22:25 2021

@author: Ace
"""
# Original Plugin
import sys, os
import xlrd
import xlwt
from xlutils.copy import copy
import datetime
import traceback
import pdfplumber
import pyautogui
import pygetwindow
import pyperclip
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains

import win32com.client

#Custom Functions
OriginalOSPath = os.getcwd()
print(OriginalOSPath)
os.chdir(r'D:\哲平\星展銀行\DBS_DATA_AceChePingHo') #程式執行資料夾
print(os.getcwd())

from Function_Package.Login_Info_Frame import Get_Info
from Function_Package.Function import outlook_is_running, ConvertNum, ExcelRead, ExcelDateHandler, ErrorMessenger, IE_Killer, Launch_Driver, prevent_screen_lock,  SendMail, strTodatetime, timeout, Data_Inputer
from Function_Package.AVC_Module import Check_Network_Connection

time_test = 3

def Inspire_Interactive_Login (uid, upw, EnvURL):
    ModuleObj = {'Status':'fail',
                'Custom_Err_Msg': '',
                'Error': {'e_class': '', 'e_detail': '', 'e_fileName': '', 'e_lineNum': '', 'e_funcName': ''}}
    Custom_Err_Msg = ''
    Process_Version = 'v1.0.20210322'
    
    # if browser == '': browser = Launch_Driver()
    browser = webdriver.Chrome('chromedriver.exe')
    session_id = browser.session_id

    for TryCount in range(1,4):
        try:
            print('Launch Inspire_Interactive')
            print('TryCount: {}'.format(TryCount))
            browser.get(EnvURL)
            browser.switch_to.default_content()
            
            #找到登錄頁面的參數
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']")))
            
            #Auto Login
            #User Name
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
            WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='text']")))
            #Password
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
            WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='password']")))
            
            web_uid = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='text']")))
            web_uid.send_Keys(uid)
            web_pwd = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='password']")))
            web_pwd.send_Keys(upw)
            
            browser.find_element_by_class_name('bb-focus-wrapper').click()
            
            #檢查是否登入成功
            try:
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'login-info-content'))).click()
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'2')))
            except: continue
        
            #print(browser.page_source)
            ModuleObj['browser'] = browser
            ModuleObj['Status'] = 'success'
            ModuleObj['session_id'] = session_id
            break
        
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            sys.exit()
        
        except Exception as erel:
            try:
                sleep(3)
                ModuleObj['Error']['e'] = erel
                cl, exc, tb = sys.exc_info() #取得Call Stack
                lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
                ModuleObj['Error']['e_fileName'] = lastCallStack[0] #取得發生的檔案名稱
                ModuleObj['Error']['e_lineNum'] = lastCallStack[1] #取得發生的行號
                ModuleObj['Error']['e_funcName'] = lastCallStack[2] #取得發生的函數名稱
                print(e.__class__.__name__ , erel.args[0], lastCallStack[0], lastCallStack[1], lastCallStack[2])
            except:pass
            raise Exception
    return ModuleObj
            
#移動到指定的資料夾
Attachments_Folder = 'CBG WMS SIP'
def move_to_CBG_Attachment (browser, Attachments_Folder=Attachments_Folder):
    #點選CONTENT MANAGER
    print('Click "CONTENT MANAGER"')
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//li[@title='Content Manager' and @class='bookmark inactive']"))).click() #參數參考
    #點選Attachments
    print('Click "Attachments"')
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Attachments' and @class='bookmark-link inactive']"))).click()  #參數參考
    #找到要上傳的資料夾
    print('Move to {}'.format(Attachments_Folder))    
    #點擊Structure每一個Item，將Structure每一個Item打開
    Structure_Items = browser.find_elements_by_xpath("//div[@class='subfolders closed']")
    try:
        for every_structure_item in Structure_Items:
            every_structure_item.click()
    except:pass
    #找出Attachments底下的文字，若等於CBG WMS SN/CBG WMS SIP，點擊進去
    Sub_Structure_Items = browser.find_elements_by_xpath("//a[@title='Attachments' and @class='bookmark-link']")
    try:
        for every_sub_structure_items in Sub_Structure_Items:
            print(every_sub_structure_items.text)
            if every_sub_structure_items.text == Attachments_Folder:
                every_sub_structure_items.click()
    except:pass

###########################################################################################################################

#主流程
if __name__ == "__main__":
    try:
        #Variables Initiated
        #Process Info
        Process_Name = 'RPA Tool for SN Term Sheet Upload/Release'
        Process_Version = 'v1.0.20210322'
        
        to = ''
        EnvURL = ''
        RunMode = ''
        uid1 = ''
        upw1 = ''
        uid2 = ''
        upw2 = ''
        
        Upload_Path = ''
        Result_Folder = ''
        Result_FileName = ''
        Result_FileSheet = ''
        
        Custom_Err_Msg = ''
        subject = Process_Name
        
        f = open('Config.txt', 'r', encoding='utf-8')
        for x in f:
            # print(x)
            if 'mailto=' in x:
                to = x.strip().replace('mailto=', '').strip()
                print('Mail Notification to: ' + to)
            elif 'CC_Mail=' in x:
                CC_Mail = x.strip().replace('CC_Mail=', '').strip()
                if CC_Mail != '':
                    print('CC Mail Notification to: ' + CC_Mail)
            elif 'bcc_mail=' in x:
                bcc_mail = x.strip().replace('bcc_mail=', '').strip()
                if bcc_mail != '':
                    print('BCC Mail Notification to: ' + bcc_mail)
            
            elif 'url=' in x:
                EnvURL = x.strip().replace('url=', '').strip()
                print('Environment to: ' + EnvURL)
            elif 'runmode=' in x:
                RunMode = x.strip().replace('runmode=', '').strip()
                print('RunMode Set to: ' + RunMode)
            
            elif 'm_id=' in x:
                uid1 = x.strip().replace('m_id=', '').strip()
                print('Maker ID Set to: ' + uid1)
            elif 'm_pw=' in x:
                upw1 = x.strip().replace('m_pw=', '').strip()
                print('Maker PW Set to: ' + (len(upw1) * '*'))
            elif 'c_id=' in x:
                uid2 = x.strip().replace('c_id=', '').strip()
                print('Checker ID Set to: ' + uid2)
            elif 'c_pw=' in x:
                upw2 = x.strip().replace('c_pw=', '').strip()
                print('Checker PW Set to: ' + (len(upw2) * '*'))
            
            #檔案上傳路徑
            elif 'Upload_Path=' in x: 
                Upload_Path = x.strip().replace('Upload_Path=', '').strip()
                print('Upload_Path Set to: ' + Upload_Path)

            #Result_Folder路徑設定
            #讀取Result_Folder資料夾
            elif 'Result_Folder=' in x: 
                Result_Folder = x.strip().replace('Result_Folder=', '').strip()
                print('Result_Folder Set to: ' + Result_Folder)
            #讀取Result_FileName檔名
            elif 'Result_FileName=' in x: 
                Result_FileName = x.strip().replace('Result_FileName=', '').strip()
                print('Result_FileName Set to: ' + Result_FileName)
            #讀取Result_FileSheet表單名稱
            elif 'Result_FileSheet=' in x: 
                Result_FileSheet = x.strip().replace('Result_FileSheet=', '').strip()
                print('Result_FileSheet Set to: ' + Result_FileSheet)
        
        if to == '' or EnvURL == '':
            Custom_Err_Msg = 'Please set necessary information in Config.txt.'
            raise Exception
        
        #檢查路徑是否設對 → "\\"的問題
        #當Upload_Path結尾多出'\'時
        if Upload_Path.endswith('\\'):
            path_split = list(Upload_Path)
            del path_split[-1]
            Upload_Path = ''.join(path_split)
        #當Upload_Path開頭多出'\'時
        if Upload_Path.startswith('\\'): Upload_Path = Upload_Path.replace('\\','',1)
        
        #User Information
        #Mode
        while RunMode == '' or len(RunMode) != 1 or (RunMode != '1' and RunMode != '2' and RunMode != '3'):
            RunMode = input('請輸入執行模式，\n1為Maker，2為Checker，3為全部執行，\n輸入模式：')
        print('執行模式: ' + str(RunMode))
        #User Information
        #Maker
        if RunMode == '1' or RunMode == '3':
            if uid1 == '' or upw1 == '':
                ModuleObj =  Get_Info('Please Enter Maker Info.', 'User Information')
                if ModuleObj['Status'] == 'success':
                    print('Get_Info ModuleObj = ' + ModuleObj['Status'])
                    uid1 = ModuleObj['uid']
                    upw1 = ModuleObj['upw']
                else:
                    print('Get_Info ModuleObj = ' + ModuleObj['Status'])
                    if ModuleObj['Custom_Err_Msg'] == '':
                        e = ModuleObj['Error']
                        Custom_Err_Msg = ErrorMessenger(e)
                    else:
                        Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    raise Exception
        #Checker
        if RunMode == '2' or RunMode == '3':
           if uid2 == '' or upw2 == '':
               ModuleObj =  Get_Info('Please Enter Checker Info.', 'User Information')
               if ModuleObj['Status'] == 'success':
                   print('Get_Info ModuleObj = ' + ModuleObj['Status'])
                   uid2 = ModuleObj['uid']
                   upw2 = ModuleObj['upw']
               else:
                   print('Get_Info ModuleObj = ' + ModuleObj['Status'])
                   if ModuleObj['Custom_Err_Msg'] == '':
                       e = ModuleObj['Error']
                       Custom_Err_Msg = ErrorMessenger(e)
                   else:
                       Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                   raise Exception
       
        print('Check Network...')
        Custom_Err_Msg = ''
        if not Check_Network_Connection():
            Custom_Err_Msg = 'No Network Connection. Process Abort.'
            print(Custom_Err_Msg)
            raise Exception
            
        #-------------------------------------------------------------------------------------------------------------
        
        SourcePath = os.getcwd()
        OutputPath = SourcePath + os.path.sep + 'OutputResult'
        
        if not os.path.isdir(OutputPath):
            os.mkdir(OutputPath)
        
        if outlook_is_running():
            PrintText = 'Outlook Running: Yes'
            print(PrintText)
        else:
            PrintText = 'Outlook Running: No, Please open Outlook to enable mail function.'
            print(PrintText)
            Custom_Err_Msg = PrintText
            raise Exception
        
        #-------------------------------------------------------------------------------------------------------------
        
        # Maker
        if RunMode == '1' or RunMode == '3':
            #檢查上傳檔案路徑是否存在
            try:
                try:
                    Upload_Path = Upload_Path.replace('\u202a','')
                    #檢查檔案路徑是否存在
                    if os.path.exists(Upload_Path) == False:
                        PrintText = 'File is not existed. Please check the path of the file.'
                        print(PrintText)
                        Custom_Err_Msg = PrintText
                        raise Exception
                except:
                    Upload_Path = pyautogui.prompt(text='請輸入上傳檔案完整路徑位置: ', title='Upload_Path', default='')
                    # Upload_Path = input('請輸入上傳檔案完整路徑位置:')
                    Upload_Path = Upload_Path.replace('\u202a','')
                    #檢查檔案路徑是否存在
                    if os.path.exists(Upload_Path) == False:
                        PrintText = 'File is not existed. Please check the path of the file.'
                        print(PrintText)
                        Custom_Err_Msg = PrintText
                        raise Exception
            except:
                Custom_Err_Msg = 'Please set necessary information(path) of Upload_Path in either Config.txt or CMD.'
                raise Exception
            
            #Excel
            udt2 = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            SourceFilePath_Excel = OutputPath + os.path.sep + 'Result_' + udt2 + '_RunMode_' + RunMode +'.xls'
            SourceFile_ExcelSheet = 'List'
            
            KeyColumn =  {'Upload_Item':'Upload_Item',
                          'Maker_Status':'Maker_Status',
                          'Maker_Notes':'Maker_Notes',
                          'Checker_Status':'Checker_Status',
                          'Checker_Notes':'Checker_Notes'}
                        
            wb1 = xlwt.Workbook()
            ws1 = wb1.add_sheet(SourceFile_ExcelSheet, cell_overwrite_ok=True)
            
            new_line = 0
            
            ws1.write(new_line, 0, KeyColumn['Upload_Item'])
            ws1.write(new_line, 1, KeyColumn['Maker_Status'])
            ws1.write(new_line, 2, KeyColumn['Maker_Notes'])
            ws1.write(new_line, 3, KeyColumn['Checker_Status'])
            ws1.write(new_line, 4, KeyColumn['Checker_Notes'])
            
            What_Files_Inside = os.listdir(Upload_Path)
            print('資料夾內的所有檔案: ', What_Files_Inside)
            CrntRow = new_line + 1
            for Upload_PDF_File in What_Files_Inside:
                file_name = Upload_Path + os.path.sep + Upload_PDF_File
                #檢查是否為檔案 以及 是否為PDF檔
                if os.path.isfile(file_name) and Upload_PDF_File.endswith('.pdf'):
                    ws1.write(CrntRow, 0, Upload_PDF_File)
                    CrntRow += 1
                else:continue
            wb1.save(SourceFilePath_Excel)
            otuputName = SourceFilePath_Excel
            
            # ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
            
            #Read Excel
            Excel_todo_list = []
            ModuleObj = ExcelRead(SourceFilePath_Excel, SourceFile_ExcelSheet, KeyColumn)
            print(ModuleObj)
            if ModuleObj['Status'] == 'success':
                print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
            else:
                print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
                if ModuleObj['Custom_Err_Msg'] == '':
                    e = ModuleObj['Error']
                    Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    ErrorMessenger(e['e'], e['e_fileName'], e['e_lineNum'], e['e_funcName'])
                else: Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                raise Exception
            Excel_todo_list = ModuleObj['SourceExcelList']
            key_column = ModuleObj['key_column']
            key_column_id = ModuleObj['key_column_id']
            WB = ModuleObj['WB']
            WS = ModuleObj['WS']
            MaxRow = ModuleObj['max_row']
            MaxCol = ModuleObj['max_col']
            if len(Excel_todo_list) == 0:
                Custom_Err_Msg = 'No Data found in Excel, Please check your file format.'
                raise Exception
                
            print(Excel_todo_list)
            print('====='*10)
            
            # 運行網頁 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            # 登入Inspire Interactive
            uid = uid1
            upw = upw1
            print(uid)
            ModuleObj = Inspire_Interactive_Login (uid, upw, EnvURL)
            if ModuleObj['Status'] == 'success':
                browser = ModuleObj['browser']
                print('ModuleObj = ' + ModuleObj['Status'])
            else:
                if ModuleObj['Custom_Err_Msg'] == '':
                    e = ModuleObj['Error']
                    Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    ErrorMessenger(e['e'], e['e_fileName'], e['e_lineNum'], e['e_funcName'])
                else: Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                print('ModuleObj = ' + ModuleObj['Status'], Custom_Err_Msg)
                raise Exception
            
            #Main Maker
            move_to_CBG_Attachment (browser, Attachments_Folder=Attachments_Folder)
            
            #獲得開啟視窗控制代碼
            main_windows = browser.current_window_handle
            print(main_windows)
            
            CrntRow = 0
            for i in range(0, len(Excel_todo_list)):
                CrntRow = i + 1
                Maker_Notes = ''
                Label_Result = ''
                
                print('◎ Handle Data' + str(CrntRow) + '/' + str(len(Excel_todo_list)) + '')
                print('▼ Start from ' + str(datetime.datetime.now()) + '▼')
                
                Crnt_Skip = False
                
                # 一筆資料試n次
                # mainTryCount = 0
                # while mainTryCount <= 3:
                #     mainTryCount = mainTryCount + 1
                
                try:
                    class Crnt_Data:
                        Upload_Item = str(Excel_todo_list[i][key_column_id['Upload_Item']]).strip()
                        Maker_Status = str(Excel_todo_list[i][key_column_id['Maker_Status']]).strip()
                        Maker_Notes = str(Excel_todo_list[i][key_column_id['Maker_Notes']]).strip()
                        Checker_Status = str(Excel_todo_list[i][key_column_id['Checker_Status']]).strip()
                        Checker_Notes = str(Excel_todo_list[i][key_column_id['Checker_Notes']]).strip()
                    print(Crnt_Data.__dict__)
                    
                    Upload_PDF_File = Crnt_Data.Upload_Item
                    
                    #prevent screen lock
                    prevent_screen_lock()
                    
                    file_name = Upload_Path + os.path.sep + Upload_PDF_File
                    print('Now Uploading: {}'.format(file_name))
                    
                    #檢查是否為檔案 以及 是否為PDF檔
                    if os.path.isfile(file_name) and file_name.strip() != '' and Upload_PDF_File.endswith('.pdf'):
                        
                        #test
                        for test_time in range(0, time_test):
                            
                            #點擊，會跳出上傳視窗
                            WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='calss']"))).click()  #參數參考
                            
                            #按SELECT FILE，選擇存放檔案的資料夾
                            SELECT_FILE = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='button']")))
                            webdriver.ActionChains(browser).move_to_element(SELECT_FILE ).click(SELECT_FILE ).perform()
                            sleep(6)
                            
                            #選取指定PDF檔案，逐筆上傳
                            pyperclip.copy(file_name)
                            sleep(2)
                            pyautogui.hotkey('ctrl', 'v')
                            sleep(2)
                            pyautogui.press('enter')
                            sleep(2)
                            
                            Ele_Xpath = "//input[@type='text' and @name='itemName']"
                            Select_Name = browser.find_element_by_xpath(Ele_Xpath).get_property('value').strip()
                            print('Select File: {}'.format(Select_Name))
                            
                            if Select_Name != '': break
                            elif Select_Name == '':
                                Btn_Cancel = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='button']")))
                                Btn_Cancel.click()
                                browser.refresh() #重新整理頁面
                                browser.implicitly_wait(10) #隱性等待，最長等10秒
                            else:
                                Btn_Cancel = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='button']")))
                                Btn_Cancel.click()
                                Maker_Notes = Maker_Notes + '[ Error! Something wrong with this file. Please Check! ]\n'
                                ws1.write(CrntRow, key_column_id['Maker_Status'], 'Error')
                                ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                                wb1.save(otuputName)
                                browser.refresh() #重新整理頁面
                                browser.implicitly_wait(10) #隱性等待，最長等10秒
                                break
                        
                        else:
                            Maker_Notes = Maker_Notes + '[ Error! Something wrong with this file. Please Check! ]\n'
                            print(Maker_Notes)
                            ws1.write(CrntRow, key_column_id['Maker_Status'], 'Error')
                            ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                            wb1.save(otuputName)
                            continue
                        
                        try:
                            Ele_Xpath = "//span[@name='errorItem errorItemVertical']"
                            Alert = browser.find_element_by_xpath(Ele_Xpath).get_property('style').strip()
                        except: Alert = 'display: none;'
                        print('File Status: {}'.format(Alert))
                        
                        #檔案路徑顯示在上傳視窗，點選Upload。 (若檔案尚未上傳)
                        if Alert == 'display: none;':
                            try:
                                Btn_Upload = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='button']")))
                                webdriver.ActionChains(browser).move_to_element(Btn_Upload ).click(Btn_Upload ).perform()
                                sleep(2)
                            except: 
                                Maker_Notes = Maker_Notes + '[ Something Worng, Error Occurred, Please Check! ]\n'
                                raise Exception
                        #若檔案以上傳，點擊Cancel，跳過此筆，並註明此檔案已存在雲端上
                        elif Alert == 'display: inline;':
                            Btn_Cancel = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='button']")))
                            Btn_Cancel.click()
                            Maker_Notes = Maker_Notes + '[ There is the same file name on the  Inspire Interactive. Probably this file has been uploaded. Please Check! ]\n'
                            print(Maker_Notes)
                            ws1.write(CrntRow, key_column_id['Maker_Status'], 'Skip')
                            ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                            wb1.save(otuputName)
                            continue
                        else:
                            if 'Something wrong with this file' not in Maker_Notes: Maker_Notes = Maker_Notes + '[ Error! Something wrong with this file. Please Check! ]\n'
                            else: pass
                            print(Maker_Notes)
                            ws1.write(CrntRow, key_column_id['Maker_Status'], 'Error')
                            ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                            wb1.save(otuputName)
                            continue
                        
                        #Upload後會新增視窗顯示上傳檔案
                        print('Change the window')
                        for test_time in range(0, time_test):
                            # 檢查是否為兩個視窗
                            all_windows = browser.window_handles
                            if len(all_windows) == 2:
                                # 切換到最新的視窗
                                browser.switch_to_window(all_windows[-1])
                                # 獲得開啟視窗控制代碼
                                window_after_upload = browser.current_window_handle
                                # 檢測是否有成功切換視窗
                                if window_after_upload != main_windows: break
                                else: continue
                            elif len(all_windows) == 1:
                                sleep(2)
                                continue
                            else:
                                Maker_Notes = Maker_Notes + '[ Something Worng, Error Occurred, Please Check! ]\n'
                                print(Maker_Notes)
                                raise Exception
                        else:
                            Maker_Notes = Maker_Notes + '[ Something Worng, Error Occurred, Please Check! ]\n'
                            print(Maker_Notes)
                            raise Exception
                        
                        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']"))) #參數參考
                        
                        # TODO: 點擊，再點選SendToCheckerGroup的OK按鈕
                        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]"))).click()
                        sleep(2)
                        print(WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//h3[@id='approval-action-name' and @title='SendToCheckerGroup']"))).text.strip())
                        sleep(5)
                        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'approveButton'))).click()
                        
                        # TODO: 顯示，表示資料傳至Checker待放行
                        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']"))) #參數參考
                        Label_Result = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']"))).text.strip() #參數參考
                        print(Label_Result)
                        Maker_Notes = Maker_Notes + '[' + Label_Result + ']\n'
                        print(Maker_Notes)
                        ws1.write(CrntRow, key_column_id['Maker_Status'], 'Completed')
                        ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                        wb1.save(otuputName)
                        print('▲ End at' + str(datetime.datetime.now()) + ' ▲')
                        
                        # TODO: 再次點選Attachments視窗頁籤
                        print('Change to the main window.')
                        browser.close()
                        # 獲取開啟的多個視窗控制代碼
                        windows = browser.window_handles
                        # 切換到當前最新開啟的視窗
                        browser.switch_to_window(all_windows[-1])
                                    
                    else: continue
                    
                    prevent_screen_lock()
                                
                except:
                    print('Something Worng, Error Occurred!')
                    # 紀錄Maker
                    ws1.write(CrntRow, key_column_id['Maker_Status'], 'Error')
                    ws1.write(CrntRow, key_column_id['Maker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                    wb1.save(otuputName)
                    # TODO: 切換視窗
                    print('Change to the main window.')
                    all_windows = browser.window_handles
                    # 切換到主視窗
                    for s_window in all_windows:
                        if s_window != main_windows:
                            browser.switch_to_window(s_window)
                            browser.clear()
                        else: continue
                    # 再次檢視視窗，獲得開啟的所有的視窗控制代碼
                    all_windows = browser.window_handles   
                    if len(all_windows) == 1 and all_windows[0] == main_windows:
                        continue # 進入下一筆
                    else : raise Exception
                
            # Maker結束，登出LogOut
            try:
                print('Logout the "Maker" account.')
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'login-info-content'))).click()
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'2'))).click()
                #User Name
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
                WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='text']")))
                #Password
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
                WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='password']")))
            except: print(sys.exc_info())
            finally:
                browser.quit()
                prevent_screen_lock()
        
        if RunMode == '3':
            print('=======Excel_todo_list Renew=======')
            ModuleObj = ExcelRead(otuputName, SourceFile_ExcelSheet, KeyColumn)
            print(ModuleObj)
            if ModuleObj['Status'] == 'success':
                print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
            else:
                print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
                if ModuleObj['Custom_Err_Msg'] == '':
                    e = ModuleObj['Error']
                    Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    ErrorMessenger(e['e'], e['e_fileName'], e['e_lineNum'], e['e_funcName'])
                else: Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                raise Exception
            Excel_todo_list = ModuleObj['SourceExcelList']
            MaxRow = ModuleObj['max_row']
            MaxCol = ModuleObj['max_col']
            if ModuleObj['Status'] == 'success':
                print('Convert_data_format ModuleObj = ' + ModuleObj['Status'])
                Excel_todo_list = ModuleObj['SourceExcelList']
            else:
                print('Convert_data_format ModuleObj = ' + ModuleObj['Status'])
                if ModuleObj['Custom_Err_Msg'] != '': Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                raise Exception
            print(Excel_todo_list)
            print('====='*10)
            
# ====================================================================================================================================================================
# ====================================================================================================================================================================

        if RunMode == '2' or RunMode == '3':
            
            # Read Excel 讀檔
            if RunMode == '2':
                #檢查路徑是否設對 → "\\"的問題
                #當Upload_Path結尾多出'\'時
                if Result_Folder.endswith('\\'):
                    path_split = list(Result_Folder)
                    del path_split[-1]
                    Result_Folder = ''.join(path_split)
                #當Upload_Path開頭多出'\'時
                if Result_Folder.startswith('\\'): Result_Folder = Result_Folder.replace('\\','',1)
                
                # Excel
                # TODO: 讀取Result位置
                try:
                   try:
                       
                       SourceFilePath_Excel = os.path.join(Result_Folder, Result_FileName)
                       SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
                       #檢查檔案路徑是否存在
                       if os.path.exists(SourceFilePath_Excel) == False: #檔案不存在
                           PrintText = 'File is not existed. Please check the path of the file.'
                           print(PrintText)
                           Custom_Err_Msg = PrintText
                           raise Exception
                   except:
                       SourceFilePath_Excel = pyautogui.prompt(text='請輸入結果檔檔案完整路徑位置: ', title='SourceFilePath_Excel', default='')
                       # SourceFilePath_Excel = input('請輸入上傳檔案完整路徑位置:')
                       SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
                       #檢查檔案路徑是否存在
                       if os.path.exists(Upload_Path) == False: #檔案不存在
                           PrintText = 'File is not existed. Please check the path of the file.'
                           print(PrintText)
                           Custom_Err_Msg = PrintText
                           raise Exception
                except:
                    Custom_Err_Msg = 'Please set necessary information(path) of Final Report in either Config.txt or CMD. (Including Result_Folder & Result_FileName)'
                    raise Exception
                
                SourceFile_ExcelSheet = Result_FileSheet 
                
                KeyColumn =  {'Upload_Item':'Upload_Item',
                          'Maker_Status':'Maker_Status',
                          'Maker_Notes':'Maker_Notes',
                          'Checker_Status':'Checker_Status',
                          'Checker_Notes':'Checker_Notes'}
                
                #Read Excel
                Excel_todo_list = []
                ModuleObj = ExcelRead(SourceFilePath_Excel, SourceFile_ExcelSheet, KeyColumn)
                print(ModuleObj)
                if ModuleObj['Status'] == 'success':
                    print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
                else:
                    print('ExcelRead ModuleObj = ' + ModuleObj['Status'])
                    if ModuleObj['Custom_Err_Msg'] == '':
                        e = ModuleObj['Error']
                        Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                        ErrorMessenger(e['e'], e['e_fileName'], e['e_lineNum'], e['e_funcName'])
                    else: Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    raise Exception
                Excel_todo_list = ModuleObj['SourceExcelList']
                key_column = ModuleObj['key_column']
                key_column_id = ModuleObj['key_column_id']
                WB = ModuleObj['WB']
                WS = ModuleObj['WS']
                MaxRow = ModuleObj['max_row']
                MaxCol = ModuleObj['max_col']
                if len(Excel_todo_list) == 0:
                    Custom_Err_Msg = 'No Data found in Excel, Please check your file format.'
                    raise Exception

                # Create Result Excel
                wb1 = xlwt.Workbook()
                ws1 = wb1.add_sheet(SourceFile_ExcelSheet, cell_overwrite_ok=True)
                
                # 拷貝來源檔內容至新檔案
                Copy_List = [[str(c.value) for c in WS.row(i)] for i in range(WS.nrows)]
                # print(Copy_List)
                for i in range(0, MaxRow):
                    for k in range(0, MaxCol):
                        ws1.write(i, k, Copy_List[i][k])
                        #  ws1.write(i, k, ConvertNum(Copy_List[i][k]))
                
                udt2 = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                SourceFilePath_Excel = OutputPath + os.path.sep + 'Result_' + udt2 + '_RunMode_' + RunMode +'.xls'
                wb1.save(otuputName)
                
                print(Excel_todo_list)
                print('====='*10)
            
            elif RunMode == '3': pass # 代表Maker及Checker都做
            
            # 登入Inspire Interactive
            uid = uid2
            upw = upw2
            print(uid)
            # 運行網頁 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            ModuleObj = Inspire_Interactive_Login (uid, upw, EnvURL)
            if ModuleObj['Status'] == 'success':
                browser = ModuleObj['browser']
                print('ModuleObj = ' + ModuleObj['Status'])
            else:
                if ModuleObj['Custom_Err_Msg'] == '':
                    e = ModuleObj['Error']
                    Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                    ErrorMessenger(e['e'], e['e_fileName'], e['e_lineNum'], e['e_funcName'])
                else: Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                print('ModuleObj = ' + ModuleObj['Status'], Custom_Err_Msg)
                raise Exception
            
            #Main Maker
            move_to_CBG_Attachment (browser, Attachments_Folder=Attachments_Folder)
            
            #獲得開啟視窗控制代碼
            main_windows = browser.current_window_handle
            print(main_windows)
            
            CrntRow = 0
            for i in range(0, len(Excel_todo_list)):
                CrntRow = i + 1
                Checker_Notes = ''
                Publish_Template = ''
                Crnt_Skip = False
                
                # Check Maker Status
                if Excel_todo_list[i][key_column_id['Maker_Status']] != 'Skip':
                    if Excel_todo_list[i][key_column_id['Maker_Status']] != 'Completed':
                        print('Skp Maker not completed data.')
                        continue
                
                if Excel_todo_list[i][key_column_id['Maker_Status']] != 'Completed':
                    if Excel_todo_list[i][key_column_id['Maker_Status']] != 'Skip':
                        print('Skp Maker not completed data.')
                        continue
                
                if Excel_todo_list[i][key_column_id['Maker_Status']] != 'Error':
                    print('Skp Maker "Error" data.')
                    continue
            
                if Excel_todo_list[i][key_column_id['Checker_Status']] == 'Verified':
                    print('Skp completed data.')
                    continue

                print('◎ Handle Data' + str(CrntRow) + '/' + str(len(Excel_todo_list)) + '')
                print('▼ Start from ' + str(datetime.datetime.now()) + '▼')
                
                
                try:
                    class Crnt_Data:
                        Upload_Item = str(Excel_todo_list[i][key_column_id['Upload_Item']]).strip()
                        Maker_Status = str(Excel_todo_list[i][key_column_id['Maker_Status']]).strip()
                        Maker_Notes = str(Excel_todo_list[i][key_column_id['Maker_Notes']]).strip()
                        Checker_Status = str(Excel_todo_list[i][key_column_id['Checker_Status']]).strip()
                        Checker_Notes = str(Excel_todo_list[i][key_column_id['Checker_Notes']]).strip()
                    print(Crnt_Data.__dict__)
                    
                    Upload_PDF_File = Crnt_Data.Upload_Item
                    
                    #prevent screen lock
                    prevent_screen_lock()
                    
                    file_name = Upload_Path + os.path.sep + Upload_PDF_File
                    
                    # 一筆資料試n次
                    mainTryCount = 0
                    while mainTryCount <= 3:
                        mainTryCount = mainTryCount + 1
                        
                        try:
                            browser.refresh() # 重新整理頁面
                            browser.implicitly_wait(10)
                            
                            # 在資料夾內(CBG WMS SN/CBG WMS SIP)搜尋檔名
                            search_box = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='filter_input' and @type='text' and @title='Filter']")))
                            
                            Crnt_Handle = Crnt_Data.Upload_Item
                            if Crnt_Handle != '':
                                Xpath = "//input[@class='filter_input' and @type='text' and @title='Filter']"
                                Data_Inputer(str(Crnt_Handle).strip(), Xpath, 1)
                                search_box.send_Keys(Keys.RETURN)
                            
                            #嘗試搜尋'NO, no results found. Try different folders, attributes or keywords." → 代表無此檔案，跳過此筆
                            try:
                                browser.implicitly_wait(5)
                                error_type = browser.find_element_by_xpath("//div[@class='dashboard-nothing-found visible']").text.replace('\n','')
                                print(error_type)
                                Checker_Notes = Checker_Notes + '[' + error_type + ']\n'
                                print(Checker_Notes)
                                # 紀錄Maker
                                ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                                ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                                wb1.save(otuputName)
                                mainTryCount = 10
                                raise Exception
                            except:pass
                            
                            # 點擊該搜尋到的檔案
                            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']"))) #參數參考
                            try:
                                Search_File = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='text' and @title={}]".format("'" + Upload_PDF_File[:Upload_PDF_File.rfind('.') + "'"]))))
                                webdriver.ActionChains(browser).move_to_element(Search_File ).click(Search_File ).perform()
                            except TimeoutException:
                                # Python rfind() 方法 → 返回字符串最後一次出現的位置
                                Search_File = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='text' and @title={}]".format("'" + Upload_PDF_File[:Upload_PDF_File.rfind('.') + "'"]))))
                                webdriver.ActionChains(browser).move_to_element(Search_File ).click(Search_File ).perform()
                            break
                        
                        except: continue
                        
                    else:
                        Checker_Notes = Checker_Notes + '[ Error! Cannot find the file on the Inspire Interactive. Please Check! ]\n'
                        print(Checker_Notes)
                        ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                        ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                        wb1.save(otuputName)
                        continue
                        
                    #Upload後會新增視窗顯示上傳檔案
                    # TODO: 切換視窗
                    print('Change the window')
                    for test_time in range(0, time_test):
                        # 檢查是否為兩個視窗
                        # 獲得開啟視窗的所有控制代碼
                        all_windows = browser.window_handles
                        if len(all_windows) == 2:
                            # 切換到最新的視窗
                            browser.switch_to_window(all_windows[-1])
                            # 獲得開啟視窗控制代碼
                            window_after_upload = browser.current_window_handle
                            # 檢測是否有成功切換視窗
                            if window_after_upload != main_windows: break
                            else: continue
                        elif len(all_windows) == 1:
                            sleep(2)
                            continue
                        else:
                            Checker_Notes = Checker_Notes + '[ Something Worng, Error Occurred, Please Check! ]\n'
                            print(Maker_Notes)
                            raise Exception
                    else:
                        Checker_Notes = Checker_Notes + '[ Something Worng, Error Occurred, Please Check! ]\n'
                        print(Maker_Notes)
                        raise Exception    
                    
                    browser.refresh() # 重新整理頁面
                    browser.implicitly_wait(10)
                    
                    # 點擊後顯示"Open Resource Draft"
                    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-app-header-btn']"))) #參數參考
                    sleep(5)
                    try:
                        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='icon iconEditDraft']"))).click()
                        sleep(2)
                        print(WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//h3[@id='approval-action-name' and @title='Open Resource Draft']"))).text.strip())
                        sleep(5)
                    except TimeoutException:
                        print(WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='class']"))).text.strip())
                        if (len(browser.find_elements_by_xpath("//div[@title='class']")) == 4) and (len(browser.find_elements_by_xpath("//div[@title='class']")) == 4) \
                            and browser.find_elements_by_xpath("//div[@title='class']")[-2].text.strip() == 'History' and browser.find_elements_by_xpath("//div[@title='class']")[-2].text.strip() == 'History' :
                            Checker_Notes = Checker_Notes + '[ Error! Probably this file has already been verified. ]\n'
                            print(Checker_Notes)
                            ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                            ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                            wb1.save(otuputName)
                        else:
                            Checker_Notes = Checker_Notes + '[ Error! Something wrong with this file. ]\n'
                            print(Checker_Notes)
                            ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                            ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                            wb1.save(otuputName)
                        browser.close()
                        # 獲得開啟視窗的所有控制代碼
                        windows = browser.window_handles
                        # 切換到最新的視窗
                        browser.switch_to_window(windows[-1])
                        continue
                    
                    #Click "OK" #可能會有MoveTargetOutOfBoundsException錯誤!
                    for test_time in range(0,time_test):
                        print('test_time: {}'.format(test_time))
                        try:
                            try:
                                try:
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    webdriver.ActionChains(browser).move_to_element(Btn_OK ).click(Btn_OK ).perform()
                                    break
                                except:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    webdriver.ActionChains(browser).move_to_element(Btn_OK ).click(Btn_OK ).perform()
                                    break
                            except:
                                try:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    Btn_OK.click()
                                    break
                                except:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    Btn_OK.click()
                                    break
                        except:
                            sleep(5)
                            continue
                        
                    else:
                        Checker_Notes = Checker_Notes + '[ Error! Unable to click the "Open Resource Draft" button. ]\n'
                        print(Checker_Notes)
                        ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                        ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                        wb1.save(otuputName)
                        browser.close()
                        # 獲得開啟視窗的所有控制代碼
                        windows = browser.window_handles
                        # 切換到最新的視窗
                        browser.switch_to_window(windows[-1])
                        continue
                    
                    browser.implicitly_wait(10)
                    
                    #可能會有MoveTargetOutOfBoundsException錯誤! #TimeoutException無法抓到的可能性
                    for test_time in range(0,time_test):
                        print('test_time: {}'.format(test_time))
                        try:
                            print(WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//h3[@id='approval-action-name' and @title='Assign To Me']"))).text.strip())
                            try:
                                try:
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    webdriver.ActionChains(browser).move_to_element(Btn_OK ).click(Btn_OK ).perform()
                                    # 檢測是否點擊到
                                    Btn_Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]")))
                                    break
                                except:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    webdriver.ActionChains(browser).move_to_element(Btn_OK ).click(Btn_OK ).perform()
                                    # 檢測是否點擊到
                                    Btn_Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]")))
                                    break
                            except:
                                try:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    Btn_OK.click()
                                    # 檢測是否點擊到
                                    Btn_Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]")))
                                    break
                                except:
                                    print('change another way.')
                                    Btn_OK = WebDriverWait(browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='approveButton' and @type='button' and @title='Confirm Action']"))) #.click()
                                    Btn_OK.click()
                                    # 檢測是否點擊到
                                    Btn_Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]")))
                                    break
                        except:
                            browser.refresh() # 重新整理頁面
                            browser.implicitly_wait(10)
                            continue
                        
                    else:
                        Checker_Notes = Checker_Notes + '[ "Assign To Me" Button Error! CrntData End with Tryed:3, Data Skipped. ]\n'
                        print(Checker_Notes)
                        ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                        ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                        wb1.save(otuputName)
                        browser.close()
                        # 獲得開啟視窗的所有控制代碼
                        windows = browser.window_handles
                        # 切換到最新的視窗
                        browser.switch_to_window(windows[-1])
                        continue
                    
                    browser.refresh() # 重新整理頁面
                    browser.implicitly_wait(10)
                    
                    # Click "Publish Template"
                    Btn_Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[(contains(@class, 'api__action_'))]"))).click()
                    sleep(2)
                    Publish_Template = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//h3[@id='approval-action-name' and @title='Publish Template']"))).text.strip()
                    print(Publish_Template)
                    
                    #Click "OK"
                    Btn_OK = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='approveButton' and @type='button']"))) #.click()
                    try: webdriver.ActionChains(browser).move_to_element(Btn_OK ).click(Btn_OK ).perform()
                    except: Btn_OK.click()
                    
                    # TODO: 跳回主頁面 (需等待頁面只剩一個視窗，也就是主視窗時)
                    while True:
                         windows = browser.window_handles  
                         if len(windows) == 1:
                             # 切換到當前最新開啟的視窗
                             browser.switch_to_window(windows[-1])
                             break
                         else:continue
                     
                    Checker_Notes = Checker_Notes + '[' + Publish_Template + ']\n'
                    print(Checker_Notes)
                    # 紀錄Maker
                    ws1.write(CrntRow, key_column_id['Checker_Status'], 'Verified')
                    ws1.write(CrntRow, key_column_id['Checker_Notes'], Checker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                    wb1.save(otuputName)
                    
                    # 此筆資料結束
                    print('Press OK')
                    print('▲ End at' + str(datetime.datetime.now()) + ' ▲')
                    prevent_screen_lock()
                    
                        
                except:
                    print('Something Worng, Error Occurred!')
                    # 紀錄Maker
                    ws1.write(CrntRow, key_column_id['Checker_Status'], 'Error')
                    ws1.write(CrntRow, key_column_id['Checker_Notes'], Maker_Notes +' [@ ' + str(datetime.datetime.now()) + ' by' + uid + ']')
                    wb1.save(otuputName)
                    # TODO: 切換視窗
                    print('Change to the main window.')
                    all_windows = browser.window_handles
                    # 切換到主視窗
                    for s_window in all_windows:
                        if s_window != main_windows:
                            browser.switch_to_window(s_window)
                            browser.clear()
                        else: continue
                    # 再次檢視視窗，獲得開啟的所有的視窗控制代碼
                    all_windows = browser.window_handles   
                    if len(all_windows) == 1 and all_windows[0] == main_windows:
                        continue # 進入下一筆
                    else : raise Exception
    
            # Checker結束，登出LogOut
            try:
                print('Logout the "Checker" account.')
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'login-info-content'))).click()
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'2'))).click()
                #User Name
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
                WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='text']")))
                #Password
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bb-textbox']")))
                WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='bb-input' and @type='password']")))
            except: print(sys.exc_info())
            finally:
                browser.quit()
                prevent_screen_lock()
    
        edt2 = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 
        if outlook_is_running():
            body = 'BOT process completed at' + edt2 + '\nProcess End.\n' + 'Please refer to the attachment for Report Result and more detail. \n' + 'Hope you have a nice day.\n'
            SendMail(to=to, cc=CC_Mail, bcc=bcc_mail, subject=subject + ' Successed', body=body, attach_path=otuputName)
        else:
            print('Finished successed with no mail notification.')
            sleep(10)
    
    except Exception as erel:
        print('Enter Controller Exception Handler.')
        try:print('main Custom_Err_Msg:', '『' + Custom_Err_Msg + '』')
        except:pass
        try: print('main erel:', '『' + erel + '』')
        except:pass
        # Check Expected
        if Custom_Err_Msg == '':
            if ModuleObj['Custom_Err_Msg'] != '':
                Custom_Err_Msg = ModuleObj['Custom_Err_Msg']
                print('custom error in Module.')
            else:
                try:
                    Custom_Err_Msg = ErrorMessenger(erel)
                    print('erel error in Module.')
                except:
                    erel = ModuleObj['Error']['e']
                    Custom_Err_Msg = ErrorMessenger(erel)
                    print('erel error in Module.')
        print('ErrorCaptured: ', Custom_Err_Msg)    
        if outlook_is_running():
            if Custom_Err_Msg == 'Invalid User ID or Password.':
                SendMail(to=to, cc=CC_Mail, bcc=bcc_mail, subject=subject + ' Failed', body='Finacle10 Login Sense End with password incorrect. \n\n Error Details:\n' + Custom_Err_Msg)
            elif Custom_Err_Msg != '':
                SendMail(to=to, cc=CC_Mail, bcc=bcc_mail, subject=subject + ' Failed', body='Unexpect Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
        else:
            if Custom_Err_Msg != '':
                print('Process Error, Process End. \n\n Error Details:\n' + Custom_Err_Msg)
                input('Error with no mail notification.')
                sleep(10)