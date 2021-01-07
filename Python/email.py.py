import smtplib

content = 'hey'

mail + smtplib.SMTP('smtp.gmail.com',465)

mail.ehlo()

mail.starttls()

mail.login('ktim2018@erhsnyc.net','209014885')

mail.sendmail('ktim2018@erhsnyc.net','ktim2018@erhsnyc.net',content)

mail.close()

