# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:31:33 2021

@author: Ace
"""

def Check_Network_Connection():
    try:
        import sys, traceback, win32com.client
        print('Checking Network...')
        #NetConnectionStatus
        strComputer = ''
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_NetworkAdapter")
        Connect_Alive = False
        for objItem in colItems:
            if objItem.NetConnectionStatus != None:
                print(str(objItem.Name) + " : Status" + str(objItem.NetConnectionStatus))
                if str(objItem.NetConnectionStatus) == '2':
                    print('Network Connected')
                    Connect_Alive = True
                    break
        if Connect_Alive == False: print("Network offline")
        
        #IP Enable
        IP_Acquired = False
        IPConfigSet = objSWbemServices.ExecQuery("Select * From Win32_NetworkAdapterConfiguration Where IPEnabled = True")
        for IPConfig in IPConfigSet:
            if IPConfig.IPAddress != None:
                IP_Acquired = True
                print('IP address: ' + str(IPConfig.IPAddress).replace('(','').replace(')','').replace(',',''))
        if IP_Acquired == False: print("No available IP Address.")
        
        #Result Check
        if Connect_Alive and IP_Acquired: return True
        else: return False
    
    except Exception as erel:
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_stack(tb)[-1] #取得Call Stack的最後一筆資料
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(lastCallStack[0], lastCallStack[1], lastCallStack[2], erel.__class__.__name__, erel.args[0])
        print(errMsg)
        return False