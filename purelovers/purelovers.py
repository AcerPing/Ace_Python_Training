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
import traceback
import time
import shutil

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

main_path = r'D:\Python_Summarize\Python_Training\purelovers'
os.chdir(main_path)

#執行程式 #主程式
if __name__ == '__main__':
    
    try:
    
        #TODO: 建立資料夾
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
        
        if To == '':
            Custom_Err_Msg = 'Please set necessary information in Config.txt.'
            raise Exception ('Config.txt Error')
        
        # Mode 
        # 先定義主題，是要(封面圖片+名字)，還是要整組圖片(個別針對女優點入下載)
        while RunMode == '' or len(RunMode) != 1 or (RunMode != '1' and RunMode != '3'): #RunMode != '2' 
            RunMode = input('請輸入執行模式，\n1為簡單下載照片，3為深入下載照片，\n輸入模式：')
        print('執行模式: ' + str(RunMode))

        # 方法一:封面圖片+名字
        if RunMode == '1' or RunMode == '3':
            # 至Amour -アムール網站 
            # 風俗情報ぴゅあらば→関西→大阪府→ミナミ(難波・道頓堀)→店舗型ヘルス→Amour -アムール
            # Amour -アムール-／難波｜在籍一覧｜関西風俗情報ぴゅあらば # 難波/店舗型ヘルス
            url="https://www.purelovers.com/kansai/shop/587/girllist/" 
        
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
            mainArea = html.find("div",id='mainArea') 
            girlListShop = mainArea.find("ul",class_='girlListShop') 
            girlList = girlListShop.find_all("li", class_='girlShopListBox') 
    
            # 建立Excel結果Log檔
            udt2 = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            OutputPath = r'D:\Python_Summarize\Python_Training\purelovers'
            SourceFilePath_Excel = OutputPath + os.path.sep + 'Result_' + udt2 + '_RunMode_' + RunMode +'.xls'
            SourceFile_ExcelSheet = 'Result List'
            KeyColumn =  {'Name':'Name',
                          'Age':'Age',
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
            CrntRow = 0 # Excel結果Log檔參數
            GirlList_Dic = {} # 字典{人名:URL}
            for each_girl in girlList:
                CrntRow += 1 # Excel結果Log檔參數
                #清除參數
                content, girl_name, img = None, None, None
                girl_name, download_img_path, data_type, save_path = '', '', '', ''
                Notes = ''
                
                try: #錯誤處理
                    
                    #文字
                    content = each_girl.find("div",class_='girlListShop-girlDate')
                    girl_name = content.find('a', class_='bold')
                    ws1.write(CrntRow, list(KeyColumn.keys()).index('Name'), girl_name.text.split(u'\xa0')[0].strip())
                    if r'/kansai/shop/587/girl/' in girl_name.get('href'):pass #檢查是否為要找尋的資料 #檢查名字是否為超連結且有/kansai/shop/587/girl/
                    else: 
                        Notes = Notes + 'girl_name HYPERLINK Error, NO "/kansai/shop/587/girl/".'
                        raise Exception('Download Error') #不是要找尋的資料 → 換下一筆 #continue
                    
                    # 字典{人名:URL}
                    GirlList_Dic[girl_name.text.split(u'\xa0')[0].strip()] = girl_name.get('href') 
                    
                    name = girl_name.text.split(u'\xa0')[0].strip()
                    age = girl_name.text.split(u'\xa0')[1].strip().replace('(','').replace(')','').strip()
                    girl_name = girl_name.text.strip().replace(u'\xa0', u' ').strip() #名字 / 年齡
                    ws1.write(CrntRow, list(KeyColumn.keys()).index('Age'), age)       
    
                    #圖片 #取得所有圖片連結
                    img = each_girl.find("table",class_='girlList-img girlList-').find('a')
                    if r'/kansai/shop/587/girl/' in img.get('href'):pass #檢查是否為要找尋的資料 #檢查名字是否為超連結且有/kansai/shop/587/girl/
                    else:
                        Notes = Notes + 'img HYPERLINK Error, NO "/kansai/shop/587/girl/".'
                        raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
                    img = img.find('img', style='width:90px;height:135px;object-fit:cover;',alt=name).get('src') #取得圖片網址 #alt==名字，確保圖片下載正確
                    img = img.split('?')[0] #?後面為參數，代表圖片壓縮尺寸。 #需要取得原始尺寸圖片
                    if (r'//contents.purelovers.com/upload/girl/' in img) or (r'//contents.purelovers.com/common/img/' in img): pass #檢查是否為要找尋的資料
                    else: 
                        Notes = Notes + 'img HYPERLINK Error, NO "//contents.purelovers.com/upload/girl/" or "//contents.purelovers.com/common/img/".'
                        raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
                    
                    # 取得檔案類型
                    download_img_path = "https:"  + img.strip()
                    data_type = '.' + img.split('.')[-1].strip()
                    save_path = os.path.join(save_dir, (girl_name + data_type))
                    
                    # 檢查檔案是否存在
                    if os.path.exists(save_path): os.remove(save_path) # 檢查檔案是否存在
                    urlretrieve(download_img_path, save_path) #利用urlretrieve下載檔案
                    print(girl_name)
                    alredy_download += 1 #檢查是否全部都下載，每下載一次就+1
                    print(alredy_download)
        
                    if r'//contents.purelovers.com/common/img/' in img:
                        Notes = Notes + 'No IMG. "//contents.purelovers.com/common/img/". No "//contents.purelovers.com/upload/girl/".'
                        raise Exception('Download Error') #不是要找尋的資料 → 換下一筆
        
                    ws1.write(CrntRow, list(KeyColumn.keys()).index('Resutl1_Status'), 'Completed'.strip())
                    ws1.write(CrntRow, list(KeyColumn.keys()).index('RPA1_Notes'), Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                except KeyboardInterrupt:
                    sys.exit(1)
        
                except:
                    if (content != None) and (girl_name != None) and (str(girl_name).strip() != ""):
                        #記錄錯誤
                        # "Bug.txt"檔案
                        f.write("資料錯誤，無法下載\n")
                        f.write(str(alredy_download).strip()+ '. ' + str(girl_name).strip() + "\n") # 寫入資料
                        f.write('Notes: ' + str(Notes).strip() + "\r\n") # 寫入資料
                        # Excel結果Log檔案
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('Resutl1_Status'), 'Error'.strip())
                        ws1.write(CrntRow, list(KeyColumn.keys()).index('RPA1_Notes'), Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                    continue
            
            f.close()# 關閉檔案
            wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
            if not len(girlList) == alredy_download: raise Exception('Download Error')
        
        ########################################################################################################################################################################
        ########################################################################################################################################################################
        
        if RunMode == '3':
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
        
        if RunMode == '3':
            
            CrntRow = 0
            for i in range(0, len(Excel_todo_list)):
                CrntRow = i + 1
                Checker_Notes, Save_Path = '',''
                Crnt_Skip = False
                
                # Check Maker Status
                if Excel_todo_list[i][key_column_id['Resutl1_Status']] == 'Error':
                    print('Skp Maker "Error" data.')
                    continue

                elif Excel_todo_list[i][key_column_id['Resutl1_Status']] != 'Completed':
                    print('Skp Maker not completed data.')
                    continue
                
                CrntRow = i + 1
                class Crnt_Data:
                    Name = str(Excel_todo_list[i][key_column_id['Name']]).strip()
                    Age = str(Excel_todo_list[i][key_column_id['Age']]).strip()
                    Resutl1_Status = str(Excel_todo_list[i][key_column_id['Resutl1_Status']]).strip()
                    RPA1_Notes = str((Excel_todo_list[i][key_column_id['RPA1_Notes']])).strip()
                    Resutl2_Status = str(Excel_todo_list[i][key_column_id['Resutl2_Status']]).strip()
                    RPA2_Notes = str(Excel_todo_list[i][key_column_id['RPA2_Notes']]).strip()
                print(Crnt_Data.__dict__) 
                
                Name = Crnt_Data.Name
                
                print('◎ Handle Data' + str(CrntRow) + '/' + str(len(Excel_todo_list)) + '')
                print(Name)
                print('▼ Start from ' + str(datetime.datetime.now()) + '▼')

                if Name not in GirlList_Dic.keys():
                    ws1.write(CrntRow, key_column_id['Resutl2_Status'], 'Error'.strip())
                    ws1.write(CrntRow, key_column_id['RPA2_Notes'], '"URL" Not Found'.strip())
                    continue

                # 檢查檔案是否存在
                Save_Path = os.path.join(save_dir, Name + f' ({Crnt_Data.Age})')
                if os.path.isdir(Save_Path): shutil.rmtree(Save_Path) #若檔案已存在則刪除
                os.mkdir(Save_Path)
                
                try:
                    #向網站索要資料
                    URL = r'https://www.purelovers.com' + GirlList_Dic[Name]
                    request = Request(URL,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"})
                    #以urlopen開啟檔案
                    with urlopen(request) as file: data = file.read().decode("utf8")
                    #解析網頁原始碼
                    warnings.filterwarnings("ignore")
                    html=BeautifulSoup(data) #beautifulsoup4分析工具→快速解析網頁HTML碼   
                    
                    girl_profile = html.find('article', id='girlProfileArea', class_='clearfix')
                    
                    # 分析左邊大頭照區域
                    left_area = girl_profile.find('div', id='girlProfileArea-left')
                    photo_group = left_area.find('div', id='girlPhoto')
                    main_photo = photo_group.find('td', id='girl-main-photo')
                    photo_number = main_photo.get('colspan')
                    
                    #下載圖片
                    already_download = 0
                    for number in range(1, int(photo_number)+1):
                        girl_photos = main_photo.find('span',id=f'images_large_{number}').find('img',alt=Name)
                        download_link = r'https:' + girl_photos.get('src')
                        Img_Save_Path = os.path.join(Save_Path, f'{Name}_{number}.' + download_link.split('.')[-1]) 
                        urlretrieve(download_link, Img_Save_Path) #利用urlretrieve下載檔案
                        if not r'no_girl_image' in download_link: already_download += 1
                        download_link, Img_Save_Path = '',''   
                    # 檢查全部照片是否皆以下載
                    if not already_download == int(photo_number): 
                        Checker_Notes = 'Download Error'
                        raise Exception('Download Error')
                    
                    
                    
                    ws1.write(CrntRow, key_column_id['Resutl2_Status'], 'Completed'.strip())
                    ws1.write(CrntRow, key_column_id['RPA2_Notes'], Checker_Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                
                except KeyboardInterrupt:
                    wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                    sys.exit(1)
        
                except:
                    # Excel結果Log檔案
                    ws1.write(CrntRow, key_column_id['Resutl2_Status'], 'Error'.strip())
                    ws1.write(CrntRow, key_column_id['RPA2_Notes'], Checker_Notes + ' [@ ' + str(datetime.datetime.now()) + ']')
                    wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔
                    continue
                
                wb1.save(SourceFilePath_Excel) # 儲存Excel結果Log檔

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