'''
寄送E-mail的程式
'''
#TODO:準備訊息物件設定
import email.message
def Send_Mail(To='', Cc='', Subject='', text=''):
    msg = email.message.EmailMessage()
    msg["From"] = "acerping0805@gmail.com" #寄件人
    msg["To"] = To # "acer0805@hotmail.com" #收件人
    msg["Cc"] = Cc # "410134003@gms.ndhu.edu.tw"
    msg["Subject"] = Subject # "test on python" #信件主題
    msg.set_content(text) #寄送純文字的內容
    # msg.add_alternative(text, subtype = "html") #寄送比較多樣式的內容(html)
    #TODO:連線到SMTP的Server，驗證寄件人身分並發送郵件
    import smtplib
    from send_email_config import Mail_Account, Mail_Password
    #TODO:到網路上搜尋gamil smtp server 或是 yahoo smtp server
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(Mail_Account, Mail_Password) #帳號 / 密碼
    server.send_message(msg)
    server.close()

