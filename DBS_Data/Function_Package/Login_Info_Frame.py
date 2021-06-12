# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:48:11 2021

@author: Ace
"""

def Get_Info ( present_text = 'Please Enter Info Below', window_title = 'Login Information'):
    ModuleObj = {'Status':'fail',
                 'Custom_Err_Msg': '',
                 'uid': '',
                 'upw': '',
                 'Error': {'e_detail': '', 'e_fileName': '', 'e_lineNume': '', 'e_funcName': ''}}
    try:
        import tkinter as Tkinter
        window = Tkinter.Tk()
        window.geometry("300x200")
        window.title(window_title)
        window.rowconfigure(7, weight=1)
        window.columnconfigure(3, weight=1)
        mystring1 = Tkinter.StringVar(window)
        mystring2 = Tkinter.StringVar(window)
        def getvalue():
            window.destroy()
        def showvalue():
            if entry2.config()['show'][4] == '*':
                entry2.config(show="")
            elif entry2.config()['show'][4] == '':
                entry2.config(show="*")
        
        main_red = "#990000"
        window.config(bg=main_red, relief=Tkinter.RIDGE)
        
        frame0 = Tkinter.Frame(window, bg='black')
        frame0.pack(fill=Tkinter.X)
        Label_Main = Tkinter.Label(frame0, text = present_text, font=('Calbri', 12, 'bold'), bg='black', fg='white')
        Label_Main.config(anchor=Tkinter.CENTER)
        Label_Main.pack(side = Tkinter.TOP, padx=15, pady=4)
        # Label_Main.grid(column=0, row=0, columnspan=2)
        
        frame_Break_1 = Tkinter.Frame(window, bg=main_red)
        frame_Break_1.pack(fill=Tkinter.X)
        Label_Break_1 = Tkinter.Label(frame_Break_1, text='', bg=main_red)
        Label_Break_1.pack(expand=True)
        # Label_Break_1.grid(column=1, row=1, columnspan=3)
        
        frame1 = Tkinter.Frame(window, bg=main_red)
        frame1.pack(fill=Tkinter.X)
        Label1 = Tkinter.Label(frame1, text='Username:', width=8, bg=main_red, fg='white')
        Label1.pack(side=Tkinter.LEFT, padx=10, pady=5)
        # label1.grid(column=0, row=2)
        entry1 = Tkinter.Entry(frame1, textvariable=mystring1, relief=Tkinter.RIDGE, bd=5)
        entry1.pack(fill=Tkinter.X, padx=5)
        # entry1.grid(column=1, row=2)
        
        # frame_Break_2 = Tkinter.Frame(window, bg=main_red, height=1)
        # frame_Break_2.pack(fill=Tkinter.X)
        # Label_Break_2 = Tkinter.Label(frame_Break_2, text='', height=1, bg=main_red)
        # Label_Break_2.pack(expand=True)
        
        frame2 = Tkinter.Frame(window, bg=main_red)
        frame2.pack(fill=Tkinter.X)
        Label2 = Tkinter.Label(frame2, text='Password:', width=8, bg=main_red, fg='white')
        Label2.pack(side=Tkinter.LEFT, padx=10, pady=5)
        # label2.grid(column=0, row=4)
        entry2 = Tkinter.Entry(frame2, textvariable=mystring2, relief=Tkinter.RIDGE, bd=5, show="*")
        entry2.pack(fill=Tkinter.X, padx=5)
        # entry2.grid(column=1, row=2)
        
        # Label_Break_3 = Tkinter.Label(window, text = '') 
        # Label_Break_3.grid(column=0, row=5, columnspan=3)
        
        frame3 = Tkinter.Frame(window, bg=main_red)
        frame3.pack(fill=Tkinter.X, expand=True)
        btn_Confirm = Tkinter.Button(frame3, text='Submit', command=getvalue, bd=5, bg='#006699',  fg='white')
        btn_Confirm.pack(side=Tkinter.LEFT, padx=15, expand=True)
        btn_Cancel = Tkinter.Button(frame3, text='Check', command=showvalue, bd=5, bg='#ffcc00')
        btn_Cancel.pack(side=Tkinter.RIGHT, padx=15, expand=True)
        # btn.grid(column=0, row=6, columnspan=3)
        
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        window.mainloop()
        
        ModuleObj['uid'] = mystring1.get()
        ModuleObj['upw'] = mystring2.get()
        
        if ModuleObj['uid'] == '' or ModuleObj['upw'] == '':
            ModuleObj['Custom_Err_Msg'] = 'Data entry not correct, cannot be blank.'
            raise Exception
        
        ModuleObj['Status'] = 'success'
        return ModuleObj

    except Exception as e:
        if ModuleObj['Custom_Err_Msg'] == '':
            # ModuleObj['Custom_Err_Msg'] = str(e)
            ModuleObj['Error'] = e
        # print(ModuleObj['Custom_Err_Msg'])
        return ModuleObj