import smtplib  
from email.message import EmailMessage  

def send_email(to, subject, body):  
    email = EmailMessage()  
    email['From'] = 'mardika200@gmail.com'  
    email['To'] = to  
    email['Subject'] = subject  
    email.set_content(body)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  
        smtp.login('mardika200@gmail.com', 'ejwq saqv vrxs uftq')  
        smtp.send_message(email)  

# Example usage  
send_email('alwansyahmardika@gmail.com', 'Test Subject', 'Hello, this is a test email!')

#  Try Modifying:  
# - Add file attachments  
# - Send HTML formatted messages  
# - Send bulk emails from a CSV list
