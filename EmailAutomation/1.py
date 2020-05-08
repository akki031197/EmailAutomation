import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = 'akshayjee6@gmail.com'
to_addr = ['snehapatwari93@gmail.com', 'hisbdcuegf.@gmail.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = " ,".join(to_addr)
msg['subject'] = 'just to check'

body = 'if you received this mail reply '\
       'plz reply with VEG_BURGER' \
       'this msg is send by code not through gmail'


msg.attach(MIMEText(body, 'plain'))

email = 'akshayjee6@gmail.com'
password = 'Pay@270499'

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_addr, to_addr, text)
mail.quit()