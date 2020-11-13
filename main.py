import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
s =smtplib.SMTP('smtp.gmail.com',587)
sender_email_id='leesterhorne8@gmail.com'
reciever_email_id='adonisamber36@gmail.com'
password= input('Enter senders email password')
subject='greetings'
msg=MIMEMultipart()
msg['From']=sender_email_id
msg['To']=reciever_email_id
msg['subject']=subject

s.starttls()
s.login(sender_email_id, password)
msg.attach(MIMEText(body,'plain'))
body='hi guys\n'
body= body+ 'how was your task'
s.sendmail(sender_email_id,reciever_email_id,body)
s.quit()