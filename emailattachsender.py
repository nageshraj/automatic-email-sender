import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'enter your email here'
email_password = 'enter your password here'

subject = 'test run' #your email subject here

e= pd.read_excel("emaillist.xlsx") #name of the excel file in same directory
emails=e['emails'].values

msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = subject

body = 'heyyyyyy' #your body here
msg.attach(MIMEText(body,'plain'))

filename='download.jpg' #attachment in same directory
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

for email in emails:
   server.sendmail(email_user,email,text)
server.quit()
