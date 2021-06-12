# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:09:18 2021

@author: Ace
"""

def outlook_is_running():
    import win32ui
    try:
        win32ui.FindWindow(None, "Microsoft Outlook")
        return True
    except win32ui.error:
        return False

#IE 殺手
def IE_Killer():
    os.system("taskkill /f /im iexplore.exe") 
    os.system("taskkill /f /im IEDriverServer.exe") 
    
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
        import xlrd
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
        