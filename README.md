# KeyloggerProject

Overview

This project combines keylogger functionality with email reporting, allowing users to capture keystrokes and receive logs via email at regular intervals. It consists of multiple Python scripts that provide different functionalities related to keylogging and email communication.

Files

keylogger_project.py

  KeyLogger Class:

  init(self, time_interval, email, password): Initializes the keylogger with the specified time interval for sending logs via email, along     with the sender's email address and password.

  append_log(self, string): Appends the specified string to the log.

  on_press(self, key): Callback function invoked when a key is pressed. Captures keystrokes and appends them to the log.

  send_email(self, email, password, message): Sends the log via email using SMTP with the specified email address and password.

  report_send(self): Periodically sends email reports containing the log at the specified time interval.

  start(self): Starts the keylogger by capturing keystrokes and sending email reports.


email.py

  send_email(email, password, message): Sends an email using SMTP. Takes the sender's email address, password, and message as parameters.
  report.py

threading.py

  report(): Defines a function for scheduling periodic tasks using threading. Creates a timer that triggers a task after a specified time      interval.
  
execute_keylogger.py

  Demonstrates the integration of the keylogger functionality into an existing Python project. Initializes the keylogger   with specific parameters and executes it.


Configuration:

Adjust parameters such as time interval, email address, and password according to your requirements in the respective files (execute_keylogger.py, email.py, threading.py, keylogger_project.py).
Running the Scripts:

Legal and Ethical Considerations
Privacy: Ensure that you have proper authorization before deploying a keylogger, as monitoring keystrokes without consent may violate privacy laws.

Security: Take precautions to secure email communications, especially when transmitting sensitive data. Use secure email protocols and consider encryption.

Compliance: Adhere to relevant laws and regulations governing surveillance activities and data collection.


Disclaimer
This project is provided for educational and informational purposes only. It is essential to use keylogging and email communication tools responsibly and ethically, respecting the privacy and security of others. The author assumes no liability for any misuse of these scripts. Always ensure compliance with applicable laws and obtain proper authorization before deploying surveillance tools
