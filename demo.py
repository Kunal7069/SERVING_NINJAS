import smtplib
from email.message import EmailMessage

# Email details
sender_email = '2100520100135@ietlucknow.ac.in'
receiver_email = 'jaink7069@gmail.com'
subject = 'Test Email from Python'
body = 'This is a test email sent from Python using Gmail SMTP.'

# Compose email
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.set_content(body)

# Gmail SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
app_password = 'pwjk kwcl uvok btya'  # Use the 16-character app password

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)
        server.send_message(msg)
        print('Email sent successfully!')
except Exception as e:
    print(f'Error sending email: {e}')