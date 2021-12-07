import smtplib
import os

email_Address = os.environ.get('EMAIL')
email_pass = os.environ.get('EMAIL_PASS')


'''         This is using simple SMTP class where port is 587
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
# with smtplib.SMTP(host='localhost', port=1025) as smtp:  #Uncomment this for local server
    smtp.ehlo() # Comment this for local server
    smtp.starttls() # Comment this for local server
    smtp.ehlo() # Comment this for local server

    smtp.login(email_Address, email_pass) # Comment this for local server
    for i in range(10):
        subject = 'Lets get dinner' + str(i)
        body = 'Wanna go out for dinner?'

        msg = f'Subject: {subject}\n\n {body}'
        smtp.sendmail(from_addr=email_Address, to_addrs=email_Address, msg=msg)
        print(i, 'done')
'''

'''This is using simple SMTP_SSL class where port is 465

with smtplib.SMTP_SSL(host = 'smtp.gmail.com', port=465) as smtp:
    smtp.login(email_Address, email_pass) # Comment this for local server
    subject = 'Lets get dinner'
    body = 'Wanna go out for dinner?'

    msg = f'Subject: {subject}\n\n {body}'
    smtp.sendmail(from_addr=email_Address, to_addrs=email_Address, msg=msg)
    print('Mail sent')
'''

'''     Email sending using SMTP_SSL and using EmailMessage
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Hey python program'
msg['To'] = email_Address
msg['From'] = email_Address
msg.set_content('Hey this is a python program sending you mail.')
with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
    smtp.login(email_Address, email_pass)
    smtp.send_message(msg)
'''

'''     Adding attachments
from email.message import EmailMessage
import imghdr

contacts = [email_Address, 'manavachawla@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Andy Samberg'
msg['To'] = contacts
msg['From'] = email_Address
msg.set_content('Image file attached below')

# files = ['andy.png', 'andy2.png']
files = ['Gmail - Issue during Exam subject Discrete Structure CET 201A.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        # file_type = imghdr.what(f.name)
        file_name = f.name

    # msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_Address, email_pass)
    smtp.send_message(msg)
'''

from email.message import EmailMessage
msg = EmailMessage()
msg['To'] = email_Address
msg['From'] = email_Address
msg['Subject'] = 'Testing HTML'
msg.set_content('Plain text if the HTML is blocked on an email')
with open('article_1.html') as f:
    html_content = f.read()
# msg.add_alternative('''\
# <DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;"> This is an HTML Email </h1>
#     </body
# </html>
# ''', subtype='html')
msg.add_alternative(html_content, subtype='html')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login(email_Address, email_pass)
    smtp.send_message(msg)
