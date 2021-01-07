import smtplib

content = 'yo fagster'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('ktim2018@erhsnyc.net','209014885')

mail.sendmail('ktim2018@erhsnyc.net','ktim2018@erhsnyc.net',content)

mail.close()
