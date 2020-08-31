'''
寄送E-mail的程式
'''
#TODO:準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "acerping0805@gmail.com" #寄件人
msg["To"] = "acer0805@hotmail.com" #收件人
msg["Cc"] = "410134003@gms.ndhu.edu.tw"
msg["Subject"] = "test on python" #信件主題
# msg.set_content("Python Email 發送電子郵件 - 基本教學") #寄送純文字的內容
msg.add_alternative("<h1>Ace</h1>HoChePing", subtype = "html") #寄送比較多樣式的內容(html)
#TODO:連線到SMTP的Server，驗證寄件人身分並發送郵件
import smtplib
#TODO:到網路上搜尋gamil smtp server 或是 yahoo smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("acerping0805@gmail.com","eawssczyunmvsivz") #帳號 / 密碼
server.send_message(msg)
server.close()

