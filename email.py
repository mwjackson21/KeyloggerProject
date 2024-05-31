import smtplib

def send_email(self, email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

send_email('testemailforprojects30@gmail.com', 'GsP78HN45A9', 'Hello')
