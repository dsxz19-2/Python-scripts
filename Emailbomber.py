import smtplib

print("""  
+----------------------------------------------------------------------------------------------------------------+
|▀███▀▀▀███                          ██  ▀███     ▀███▀▀▀██▄                          ▄██                        |
| ██    ▀█                                 ██       ██    ██                           ██                        |
| ██   █  ▀████████▄█████▄  ▄█▀██▄ ▀███    ██       ██    ██ ▄██▀██▄▀████████▄█████▄   ██▄████▄   ▄▄█▀██▀███▄███ |
| ██████    ██    ██    ██ ██   ██   ██    ██       ██▀▀▀█▄▄██▀   ▀██ ██    ██    ██   ██    ▀██ ▄█▀   ██ ██▀ ▀▀ |
| ██   █  ▄ ██    ██    ██  ▄█████   ██    ██       ██    ▀███     ██ ██    ██    ██   ██     ██ ██▀▀▀▀▀▀ ██     |
| ██     ▄█ ██    ██    ██ ██   ██   ██    ██       ██    ▄███▄   ▄██ ██    ██    ██   ██▄   ▄██ ██▄    ▄ ██     |
|▄██████████████  ████  ████▄████▀██▄████▄▄████▄   ▄████████  ▀█████▀▄████  ████  ████▄ █▀█████▀   ▀█████▀████▄  |                     
+----------------------------------------------------------------------------------------------------------------+
By DSXZ19-2
Copywrite DSXZ19-2
For this to work you need to allow lees secure apps to send emails: https://bit.ly/3yn1d9v
""")

sender_email = input(str("Enter your email here: "))
victVm_email = input(str("Enter victim email here: "))
password = input(str("Enter your email password here: "))
message = input(str("Enter your message here: "))
loop = int(input("How many emails would you like to send: "))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

for i in range (loop):
	server.login(sender_email, password)
	server.sendmail(sender_email, victim_email, message)
	print("Done email sent to", victim_email)
