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
os.chdir(r'D:\Python_Summarize\Python_Training\DBS_Data') #程式執行資料夾
print(os.getcwd())

from Function_Package.Login_Info_Frame import Get_Info
from Function_Package.Function import outlook_is_running
#ConvertNum, ExcelReak, ExcelDateHandler, ErrorMessenger, IE_Killer, Launch_Driver, prevent_screen_lock, SendMail, strTodatetime, timeout
from Function_Package.AVC_Module import Check_Network_Connection
