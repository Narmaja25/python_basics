import smtplib 

from email.message import EmailMessage

# simple message
sender = 'narmajauppalapati@gmail.com' 
password = 'eqnkylflpyxvssxy'
receiver = 'Skbashira277@gmail.com' 
message = 'Hi Bhashira, I have sent this mail from python code, this is my first mail from python code'
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.sendmail(sender, receiver, message)
print('Message sent successfully')


# message with Subject and attachments
sender = 'narmajauppalapati@gmail.com'
sender = 'narmajauppalapati@gmail.com'
password = 'eqnkylflpyxvssxy'
message = EmailMessage()
message['From'] = 'narmajauppalapati@gmail.com'
message['To'] = 'Skbashira277@gmail.com'
message['Subject'] = 'SMTP MAIL'
message.set_content('Hi Bhashira, I have sent this mail from python code, this is my first mail from python code')
files = ['C:\\Users\\asus\\OneDrive\\Desktop\\python_pdf\'s\\Screenshot_11-9-2026_95523_meet.google.com.jpeg']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')


# Bulk mail sending with Subject and attachments
sender = 'narmajauppalapati@gmail.com' 
sender = 'narmajauppalapati@gmail.com' 
password = 'eqnkylflpyxvssxy'
receivers = ['wd.rkad@gmail.com', 'Skbashira277@gmail.com', 'uppalapatiprasad09@gmail.com']
message = EmailMessage()
message['From'] = 'narmajauppalapati@gmail.com'
message['Bcc'] = ','.join(receivers)
message['Subject'] = 'SMTP MAIL'
message.set_content('Hi sir. I am Narmaja, I have been sending this mail from python code & this is my first project, please check the attachment file and pleasegive your valuable feedback')
files = ['C:\\Users\\asus\\OneDrive\\Desktop\\python_pdf\'s\\Screenshot_11-9-2026_95523_meet.google.com.jpeg']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')