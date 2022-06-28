# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:55:55 2021

@author: Ace
"""
from bs4 import BeautifulSoup
# import codecs
import os
import sys
from urllib.request import urlopen, Request, urlretrieve 
import warnings
import datetime
import xlwt
import xlrd
from xlutils.copy import copy
import traceback
import time
import shutil
import pandas as pd
import pyautogui

main_path = r'D:\Python_Summarize\Python_Training\purelovers'
os.chdir(main_path)

# 自訂函式庫
from send_email import Send_Mail

############################################################################################################################################
############################################################################################################################################
#Custom Function Defination
def ErrorMessenger(e, fileName='', lineNum=0, funcName='', Custom_Err_Msg=''):
    error_class = e.__class__.__name__ #取得錯誤類型
    detail = e.args[0] #取得詳細內容
    if fileName == '' and funcName == '':
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName =  lastCallStack[2] #取得發生的函數名稱
    if Custom_Err_Msg != "":
        errMsg = Custom_Err_Msg
    else:
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    return errMsg

def ExcelRead(filename, TargetSheetName, key_column):
    ModuleObj = {'Status':'fail',
                 'Custom_Err_Msg': '',
                 'SourceExcelList': [],
                 'key_column': [],
                 'key_column_id': [],
                 'max_row': '',
                 'max_col' : '',
                 'WB':[],
                 'WS':[],
                 'Error': {'e_detail': '', 'e_fileName': '', 'e_lineNum': '', 'e_funcName': ''}}
    try:
        SourceExcelList = []
        #Read Xlrd
        print('Loading Excel:')
        print(filename)
        wb = xlrd.open_workbook(filename)
        print('Worksheets loaded')
        print(wb.sheet_names())        
        
        #表名搜尋
        sheet_names = wb.sheet_names()
        SheetFound = False
        SheetCount = 0
        SheetNo = 0
        for sheet in wb.sheet_names():
            if sheet == TargetSheetName:
                SheetFound = True
                SheetNo = SheetCount
            SheetCount = SheetCount +1
        if SheetFound == False:
            ModuleObj = {'Custom_Err_Msg': 'Cannot find sheet name 「' + TargetSheetName + '」.'}
            del wb, ws
            return ModuleObj 
        print('Sheet 「' + TargetSheetName + '」 Found:', SheetFound, SheetCount, SheetNo)
        ws = wb.sheet_by_name(sheet_names[SheetNo])
        print('Columns: [%s] Rows: [%s]' % (ws.ncols, ws.nrows))
        MaxRow = ws.nrows
        MaxCol = ws.ncols
        
        key_column_id = {}
        for item in key_column:
            key_column_id[item] = ''
        
        #欄位比對
        MaxCheck = len(key_column)
        KeyColCount = 0
        ColCount = 0
        for i in range(0, MaxCheck):
            for item in key_column:
                if ws.cell(0, i).value.strip() == key_column[item]:
                    key_column_id[item] = ColCount
                    KeyColCount = KeyColCount + 1
                    print(key_column_id[item], item)
            ColCount = ColCount + 1
        print(KeyColCount, MaxCheck)
        if KeyColCount < MaxCheck:
            MissedCol = ''
            for item in key_column_id:
                MissedCol = MissedCol + '「 ' + item + '」'
            print('Excel File missing columns as below, please check.\n' + MissedCol)
            ModuleObj = {'Custom_Err_Msg': 'Excel File missing columns as below, please check.\n' + MissedCol}
            del wb, ws
            return ModuleObj
        
        # print(key_column)
        # print(KeyColCount, MaxCheck)
        # print(key_column_id)
        
        # 讀取表資料內容
        for i in range(1, MaxRow):
            CrntRow = ws.row_values(i)
            SourceExcelList.append(CrntRow)
        print('Sheet 「' + TargetSheetName + '」 Loaded. ColumnCount: ', MaxCol, ' RowCount: ', MaxRow, ' DataCapture: ', len(SourceExcelList))
        ModuleObj['Status'] = 'success'
        ModuleObj['SourceExcelList'] = SourceExcelList
        ModuleObj['key_column'] = key_column
        ModuleObj['key_column_id'] = key_column_id
        ModuleObj['max_row'] = MaxRow
        ModuleObj['max_col'] = MaxCol
        ModuleObj['WB'] = wb
        ModuleObj['WS'] = ws
        # ModuleObj = {'Status':'success', 'SourceExcelList': SourceExcelList, 'key_column': key_column, 'key_column_id': key_column_id}
        del wb, ws
        return ModuleObj
    except Exception as e:
        ModuleObj['Error'] = e
        ModuleObj['Error']['e_class'] = e.__class__.__name__ #取得錯誤類型
        ModuleObj['Error']['e_detail'] = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
        ModuleObj['Error']['e_fileName'] = lastCallStack[0] #取得發生的檔案名稱
        ModuleObj['Error']['e_lineNum'] = lastCallStack[1] #取得發生的行號
        ModuleObj['Error']['e_funcName'] = lastCallStack[2] #取得發生的函數名稱
        return ModuleObj
############################################################################################################################################
############################################################################################################################################ 

# For Runmode 1 
page_number =1
def request_url (page_number,web_link="https://purelovers.com/shop/587/girllist/"):
    '''
    至Amour -アムール網站  https://www.purelovers.com/kansai/shop/587/girllist/
    風俗情報ぴゅあらば→関西→大阪府→ミナミ(難波・道頓堀)→店舗型ヘルス→Amour -アムール
    Amour -アムール-／難波｜在籍一覧｜関西風俗情報ぴゅあらば # 難波/店舗型ヘルス
    '''
    page=f'pg{str(page_number).strip()}'
    url = web_link + page
    mainArea, girlListShop, girlList = None, None, list()
    
    #向網站索要資料
    request = Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
    #以urlopen開啟檔案
    with urlopen(request) as file: data = file.read().decode("utf8")
    # with codecs.open("HTML.txt","w",encoding='utf-8') as file: file.write(str(data)) 
    # print(data)
    
    #解析網頁原始碼
    warnings.filterwarnings("ignore")
    html=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼    
    
    #開始逐步搜尋
    try: 
        mainArea = html.find("main",class_='k_purelovers-main') 
        if mainArea == None: raise Exception('Download Error') #檢查是否有抓到關鍵值
        girlListShop = mainArea.find("div",class_='k_row k_mt-2 k_row-grid--small k_row-dense') 
        if girlListShop == None: raise Exception('Download Error') #檢查是否有抓到關鍵值
        girlList = girlListShop.find_all("div", class_='k_col k_col-4') 
        if girlList == list(): raise Exception('Download Error') #檢查是否有抓到關鍵值
    except:
       pass
   
    return mainArea, girlListShop, girlList

    

############################################################################################################################################ 


#TODO: 執行程式（主程式）
if __name__ == '__main__':
    
    try:
    
        #建立資料夾
        save_dir = os.path.join(main_path, r'難波の店舗型ヘルス「Amour -アムール-」の女の子在籍ページです。色々な女の子をご紹介！')
        if not os.path.isdir(save_dir): os.mkdir(save_dir)
        
        # 參數設定
        Runmode = ''
        To = ''
        Cc = ''
        
        Custom_Err_Msg = ''
        
        f = open(os.path.join(main_path,'Config.txt'), 'r', encoding='utf-8')
        for x in f:
            if 'RunMode=' in x:
                RunMode = x.strip().replace('RunMode=', '').strip()
                print('RunMode set to: ' + RunMode)
            elif 'To=' in x:
                To = x.strip().replace('To=', '').strip()
                print('E-mail Receiver set to: ' + To)
            elif 'Cc=' in x:
                Cc = x.strip().replace('Cc=', '').strip()
                print('Carbon Copy Receiver set to: ' + Cc)
            elif 'Load_File=' in x :
                Runmode2_ReadFile = x.strip().replace('Load_File=', '').strip()
                if RunMode == '2' : print('Runmode2 ReadFile Path: ' + Runmode2_ReadFile)
        
        if To == '':
            Custom_Err_Msg = 'Please set necessary information in Config.txt.'
            raise Exception ('Config.txt Error')
        
        # Mode 
        # 先定義主題，是要(封面圖片+名字)，還是要整組圖片(個別針對女優點入下載)
        while RunMode == '' or len(RunMode) != 1 or (RunMode != '1' and RunMode != '3' and RunMode != '2'):  
            RunMode = input('請輸入執行模式，\n1為簡單下載照片，2為深入下載照片，3為完整下載照片，\n輸入模式：')
        print('執行模式: ' + str(RunMode))
        
        #TODO: RunMode 1 or 3
        # 方法一:封面圖片+名字
        if RunMode == '1' or RunMode == '3':
            
            #清空儲存資料夾
            for filename in os.listdir(save_dir):
                file_path = os.path.join(save_dir, filename)
                try:
                    if os.path.isfile(file_path): os.remove(file_path)
                    elif os.path.isdir(file_path): shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    Custom_Err_Msg = Custom_Err_Msg + 'Failed to delete %s. Reason: %s' % (file_path, e)
                    raise Exception ('Unable to delete file.')

            #開始逐步搜尋
            try: 
                mainArea, girlListShop, girlList = request_url(page_number)
                #檢查是否有抓到關鍵值
                if mainArea == None: raise Exception('Download Error') 
                elif girlListShop == None: raise Exception('Download Error')
                elif girlList == list(): raise Exception('Download Error') 
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                # print(exc_type, fname, exc_tb.tb_lineno)
                Custom_Err_Msg = 'Line：' + str(exc_tb.tb_lineno) + '\n' + Custom_Err_Msg + '爬蟲程式沒有抓到關鍵值'
                raise Exception('Download Error')
    
            # 建立Excel結果Log檔
            udt2 = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            OutputPath = main_path
            SourceFilePath_Excel = OutputPath + os.path.sep + 'Result_' + udt2 + '_RunMode_' + RunMode +'.xls'
            SourceFile_ExcelSheet = 'Result List'
            KeyColumn =  {'Girl_Name':'Girl Name',
                          'Name':'Name',
                          'Age':'Age',
                          'URL':'URL',
                          'Resutl1_Status':'Resutl Status',
                          'RPA1_Notes':'RPA1 Notes',
                          'Resutl2_Status':'Resut2 Status',
                          'RPA2_Notes':'RPA2 Notes',}    
            wb1 = xlwt.Workbook()
            ws1 = wb1.add_sheet(SourceFile_ExcelSheet, cell_overwrite_ok=True)
            for index_i, item in enumerate(KeyColumn):
                ws1.write(0, index_i, KeyColumn[item])
            wb1.save(SourceFilePath_Excel)
            
            # 開啟Bug檔案
            f = open("Bug.txt", "w", encoding='utf-8') # 以覆寫模式開啟檔案
            alredy_download = 0 #檢查是否全部都下載，初始值設為0
            Download_Exception = 0 #出錯的照片數量
            len_girlList = 0 #累加女孩全部數量
            CrntRow = 0 # Excel結果Log檔參數
            GirlList_Dic = {} # 字典{人名:URL}
            while mainArea != None and girlListShop != None and girlList != list():
                print(f'目前頁數：{str(page_number).strip()}')
                len_girlList += len(girlList)
                for each_girl in girlList:
                    CrntRow += 1 # Excel結果Log檔參數
                    #清除參數
                    content, girl_name, img = None, None, None
                    girl_name, download_img_path, data_type, save_path = '', '', '', ''
                    Notes = ''
                    
                    try: #錯誤處理
    
                        #文字
                        content = each_girl.find("div",class_='k_imageCard-description')
                        girl_name = content.find('div', class_='k_flex k_align-center k_ellipsis').text
                        girl_name = repr(girl_name).replace(" ","").replace("\\n","").strip() #名字(年齡) EX.アスカ(19)
                        name = girl_name[:girl_name.find('(')].replace("'","").replace("\\u3000","\u3000").strip() #女孩姓名
                        age = girl_name[girl_name.find('(')+1:girl_name.find(')')] #女孩年紀
                        #紀錄到Excel
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('Girl_Name'), girl_name)  
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('Name'), name)
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('Age'), age)  
                        
                         #檢查資料是否有超連結
                        if not r'https://purelovers.com/shop/587/girl/' in each_girl.find("a").get('href'):
                            Notes = Notes + f'girl_name {str(girl_name)} HYPERLINK Error, NO "https://purelovers.com/shop/587/girl/".'
                            raise Exception('Download Error') #不是要找尋的資料 → 換下一筆 #continue
                        
                        # 字典{人名:URL}
                        URL = each_girl.find("a").get('href')
                        GirlList_Dic[girl_name] = URL
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('URL'), str(URL))
                        
                        #圖片 #取得圖片網址 
                        img = each_girl.find("img").get('src')
                        # 畫像準備中，沒有大頭照 
                        if (r'noImage' in img):
                            Notes = Notes + f'girl_name {str(girl_name)} noImage.'
                            raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
                        #檢查圖片資料是否有超連結
                        elif not r'//contents.purelovers.com/upload/girl/' in img:
                            Notes = Notes + f'girl_name {str(girl_name)} img HYPERLINK Error, NO "//contents.purelovers.com/upload/girl/".'
                            raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
                        #alt==名字，確保圖片下載正確
                        img = each_girl.find("img", alt=name).get('src')
                        img = img.split('?')[0] #?後面為參數，代表圖片壓縮尺寸。 #需要取得原始尺寸圖片
    
                        # 取得檔案類型
                        download_img_path = "https:"  + img.strip()
                        data_type = '.' + img.split('.')[-1].strip()
                        save_path = os.path.join(save_dir, (str(girl_name).replace('\'','').replace('\\u3000',' ').strip() + data_type)) #須注意檔案命名格式
                        
                        urlretrieve(download_img_path, save_path) #利用urlretrieve下載檔案
                        alredy_download += 1 #檢查是否全部都下載，每下載一次就+1
                        print(str(alredy_download).strip(), girl_name)
            
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('Resutl1_Status'), 'Completed'.strip())
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('RPA1_Notes'), Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                        
                    except KeyboardInterrupt:
                        sys.exit(1)
            
                    except:
                        if (content != None) and (girl_name != None) and (str(girl_name).strip() != ""):
                            #記錄錯誤
                            #若原因Notes為空白，則記錄系統錯誤（包含行數）
                            if str(Notes).strip() == '':
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                Notes = Notes + '(Line：{})'.format(str(exc_tb.tb_lineno).strip()) + str(exc_obj).strip() 

                            # "Bug.txt"檔案
                            f.write("資料錯誤，無法下載\n")
                            f.write(str(alredy_download).strip()+ '. ' + str(girl_name).strip() + "\n") # 寫入資料
                            f.write('Notes: ' + str(Notes).strip() + "\r\n") # 寫入資料
                            # Excel結果Log檔案
                            ws1.write(CrntRow, list(KeyColumn.keys()).index('Resutl1_Status'), 'Error'.strip())
                            ws1.write(CrntRow, list(KeyColumn.keys()).index('RPA1_Notes'), Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                            wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                            Download_Exception += 1
                        continue
                
                
                # 翻頁
                page_number  = page_number  +1
                #開始逐步搜尋
                mainArea, girlListShop, girlList = request_url(page_number)
                

            f.close()# 關閉檔案
            ws1.col(list(KeyColumn.keys()).index('Girl_Name')).hidden = 1 #隱藏欄
            wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
            if not len_girlList == alredy_download + Download_Exception: 
                Custom_Err_Msg =  Custom_Err_Msg + '尚有美女圖未下載；美女圖未全部下載完畢。'
                raise Exception('Download Error')
        
            print('執行模式: {}  End at {}.'.format(str(RunMode),str(datetime.datetime.now())))
        ########################################################################################################################################################################
        ########################################################################################################################################################################
        
        #TODO: RunMode 3 or 2
        if RunMode == '3' or RunMode == '2':
            
            if RunMode == '2':
                # 檔案位置
                try:
                   try:
                       SourceFilePath_Excel = os.path.join(main_path, Runmode2_ReadFile)
                       SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
                       #檢查檔案路徑是否存在
                       if os.path.isfile(SourceFilePath_Excel) == False: #檔案不存在
                           PrintText = 'File is not existed. Please check the path of the file.'
                           print(PrintText)
                           raise Exception
                   except:
                       SourceFilePath_Excel = pyautogui.prompt(text='請輸入結果檔檔案完整路徑位置: ', title='Runmode2 ReadFile', default='D:\Python_Summarize\Python_Training\purelovers')
                       SourceFilePath_Excel = SourceFilePath_Excel.replace('\u202a','')
                       #檢查檔案路徑是否存在
                       if os.path.isfile(SourceFilePath_Excel) == False: #檔案不存在
                           PrintText = 'File is not existed. Please check the path of the file.'
                           print(PrintText)
                           raise Exception
                except:
                    Custom_Err_Msg = 'Please set necessary information(File Path) in either Config.txt or CMD.'
                    raise Exception
                
                # 複製User原有報表，寫入複製後的那份
                udt2 = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                Copy_SourceFilePath_Excel = os.path.join(main_path, 'Result_' + udt2 + '_RunMode_' + RunMode +'.xls')
                shutil.copy(SourceFilePath_Excel, Copy_SourceFilePath_Excel) # 複製
                SourceFilePath_Excel = Copy_SourceFilePath_Excel
                
                # 表單名稱（SourceFile_ExcelSheet）及 欄位名稱（KeyColumn）與預設相同
                SourceFile_ExcelSheet = 'Result List'
                KeyColumn =  {'Girl_Name':'Girl Name',
                          'Name':'Name',
                          'Age':'Age',
                          'URL':'URL',
                          'Resutl1_Status':'Resutl Status',
                          'RPA1_Notes':'RPA1 Notes',
                          'Resutl2_Status':'Resut2 Status',
                          'RPA2_Notes':'RPA2 Notes',}  
                
                # 設定變數（ws1 & wb1）
                wb1 = copy(xlrd.open_workbook(SourceFilePath_Excel)) # 活頁簿
                sheet_names = xlrd.open_workbook(SourceFilePath_Excel).sheet_names() # 取得全部工作表
                ws1 = wb1.get_sheet(sheet_names.index(SourceFile_ExcelSheet)) # 設定要寫入的工作表（書寫的筆）

            else:         
                print('=======Excel_todo_list Renew=======')
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
            MaxRow = ModuleObj['max_row']
            MaxCol = ModuleObj['max_col']
            print(Excel_todo_list)
            print('====='*10)

        ########################################################################################################################################################################
        ########################################################################################################################################################################
        
        #TODO: RunMode 3 or 2
        if RunMode == '3' or RunMode == '2': 
            
            CrntRow = 0
            for i in range(0, len(Excel_todo_list)):
                CrntRow = i + 1
                Checker_Notes, Save_Path = '',''
                Crnt_Skip = False
                
                # Check Maker Status
                if Excel_todo_list[i][key_column_id['Resutl1_Status']] == 'Error':
                    # 跑RunMode 1時出錯
                    print('Skp Maker "Error" data.')
                    continue

                elif Excel_todo_list[i][key_column_id['Resutl1_Status']] != 'Completed':
                    # 跑RunMode 1時出錯
                    print('Skp Maker not completed data.')
                    continue
                
                elif Excel_todo_list[i][key_column_id['Resutl2_Status']] == 'Completed':
                    # 已經跑完 RunMode 2，不再重跑
                    print('Skp completed data.')
                    continue
                
                CrntRow = i + 1
                class Crnt_Data:
                    Girl_Name = str(Excel_todo_list[i][key_column_id['Girl_Name']]).strip()
                    Name = str(Excel_todo_list[i][key_column_id['Name']]).strip()
                    Age = str(Excel_todo_list[i][key_column_id['Age']]).strip()
                    URL = str(Excel_todo_list[i][key_column_id['URL']]).strip()
                    Resutl1_Status = str(Excel_todo_list[i][key_column_id['Resutl1_Status']]).strip()
                    RPA1_Notes = str((Excel_todo_list[i][key_column_id['RPA1_Notes']])).strip()
                    Resutl2_Status = str(Excel_todo_list[i][key_column_id['Resutl2_Status']]).strip()
                    RPA2_Notes = str(Excel_todo_list[i][key_column_id['RPA2_Notes']]).strip()
                # print(Crnt_Data.__dict__) 
                
                Girl_Name = Crnt_Data.Girl_Name
                Name = Crnt_Data.Name
                
                print('◎ Handle Data' + str(CrntRow) + '/' + str(len(Excel_todo_list)) + '')
                print(Name)
                print('▼ Start from ' + str(datetime.datetime.now()) + '▼')

                # 檢查檔案是否存在
                Save_Path = os.path.join(save_dir, Name + f' ({Crnt_Data.Age})')
                if RunMode == '2' and os.path.isdir(Save_Path) : shutil.rmtree(Save_Path) # RunMode為'2'的情況下，若資料夾已存在則先刪除
                os.mkdir(Save_Path)
                
                try:
                    #向網站索要資料
                    if RunMode == '2': URL = Crnt_Data.URL
                    else:URL = GirlList_Dic[Girl_Name]
                    request = Request(URL,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                    #以urlopen開啟檔案
                    with urlopen(request) as file: data = file.read().decode("utf8")
                    #解析網頁原始碼
                    warnings.filterwarnings("ignore")
                    html=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼   
                    
                    girl_profile = html.find('div', class_='k_flex k_mt-6')
                    
                    # 分析左邊大頭照區域
                    photo_group = girl_profile.find('div', class_='k_imageWrapChange k_flex-shrink-0')
                    # main_photo = photo_group.find('li', class_='k_list-item k_imageWrapChange-main k_col-12') # 封面像面
                    photos = photo_group.find_all('li', class_='k_list-item k_imageWrapChange-list-item k_col-20')
                    photo_number = len(photos) 
                    
                    #下載圖片
                    already_download = 0
                    for number in range(1, int(photo_number)+1):
                        download_link = "https:"  + photos[number-1].find('img',alt=Name).get('src')
                        download_link = download_link.split('?')[0] #?後面為參數 #需要取得原始尺寸圖片
                        Img_Save_Path = os.path.join(Save_Path, f'{Name}_{number}.' + download_link.split('.')[-1]) 
                        urlretrieve(download_link, Img_Save_Path) #利用urlretrieve下載檔案
                        if not r'noImage' in download_link: already_download += 1
                        download_link, Img_Save_Path = '',''   
                    # 檢查全部照片是否皆以下載
                    if not already_download == int(photo_number): 
                        Checker_Notes = 'Download Error'
                        raise Exception('Download Error')
                        
                    # 分析右邊文字描述
                    description = girl_profile.find('div', class_='k_flex-grow-1 k_ml-6')
                    description = description.find('div', class_='k_row k_mt-4 k_row-table k_row--grey-lighten-1')
                    descriptions = description.find_all('div')
                    # Pandas to Excel
                    list_title = list()
                    list_content = list()
                    for index_i , each_content in enumerate(descriptions): 
                        
                        # 取出 class = "k_row*"
                        if each_content.get('class')[0] != 'k_col': continue
                    
                        # ['k_col', 'k_px-2', 'k_py-2', 'k_col-3', 'k_grey', 'k_lighten-4'] 為標題
                        if each_content.get('class')[1] == 'k_px-2' and each_content.get('class')[2] == 'k_py-2' and each_content.get('class')[3] == 'k_col-3': 
                            list_title.append(each_content.text.replace(' ',"").strip())
                        # ['k_col', 'k_py-2', 'k_px-4', 'k_col-9'] 為內容
                        elif each_content.get('class')[1] == 'k_py-2' and each_content.get('class')[2] == 'k_px-4' and each_content.get('class')[3] == 'k_col-9':
                            list_content.append(each_content.text.replace(' ',"").strip())  
                            
                    Series_title = pd.Series(list_title)
                    Series_content = pd.Series(list_content)
                    df = pd.concat([Series_title, Series_content], axis = 1)
                    df.to_excel(os.path.join(Save_Path, f'{Name}.xls') ,sheet_name = Name + f' ({Crnt_Data.Age})', index = False, header=False)

                    ws1.write(CrntRow, key_column_id['Resutl2_Status'], 'Completed'.strip())
                    ws1.write(CrntRow, key_column_id['RPA2_Notes'], Checker_Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                
                except KeyboardInterrupt:
                    wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                    sys.exit(1)
        
                except:
                    #若原因Notes為空白，則記錄系統錯誤（包含行數）
                    if str(Checker_Notes).strip() == '':
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        Checker_Notes = Checker_Notes + '(Line：{})'.format(str(exc_tb.tb_lineno).strip()) + str(exc_obj).strip() 

                    # Excel結果Log檔案
                    ws1.write(CrntRow, key_column_id['Resutl2_Status'], 'Error'.strip())
                    ws1.write(CrntRow, key_column_id['RPA2_Notes'], Checker_Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                    wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                     
                ws1.col(list(KeyColumn.keys()).index('Girl_Name')).hidden = 1 #隱藏欄
                wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                print('▲ End at' + str(datetime.datetime.now()) + ' ▲')

        # 寄發E-mail訊息
        edt2 = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 
        body = 'RPA process completed at' + edt2 + '\nProcess End.\n' 
        Subject='purelovers.py'
        Send_Mail(To=To, Cc=Cc, Subject='purelovers.py', text=body)
        
    except Exception as erel:
        print('Enter Controller Exception Handler.')
        try:print('main Custom_Err_Msg:', '『' + Custom_Err_Msg + '』')
        except:pass
        try: print('main erel:', '『' + erel + '』')
        except:pass
        # Check Expected
        if Custom_Err_Msg == '':
            try:
                Custom_Err_Msg = ErrorMessenger(erel)
                print('erel error in Module.')
            except:pass
        print('ErrorCaptured: ', Custom_Err_Msg)    
        if Custom_Err_Msg != '':
            body='Unexpect Error, Process End. \n\nError Details:\n' + Custom_Err_Msg
            if To != '':
                Send_Mail(To=To, Cc=Cc, Subject='purelovers.py Failed', text=body)
            else:
                print('Process Error, Process End. \n\nError Details:\n' + Custom_Err_Msg)
                input('Error with no mail notification.')
                time.sleep(10)