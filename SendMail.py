import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
#from email import encoders
import os

gmail_user = "myoung0710@gmail.com" # gmail address
gmail_pwd = "sksajtwu123" # gmail password

def send_gmail(to, subject, text):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    #part.set_payload(open(attach, 'rb').read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.quit()

send_gmail("myoung0710@naver.com", "SendMail Test", "Send_gamil 함수 테스트입니다." )
