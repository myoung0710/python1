import smtplib

from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login('myoung0710@gmail.com', '')
msg = MIMEText("내용 : 테스트입니다.")
msg["Subject"] = "제목 : 메일 보내기 테스트입니다."
s.sendmail("myoung0710@gmail.com", "myoung0710@gmail.com", msg.as_string())
s.quit()