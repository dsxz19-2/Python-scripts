import time

print("""
                              ▄▄▄  
  ██▀▀█▄ ▀██▀   ▀██▀    █    ▀███  
 ███  ▀██  ▀██ ▄█▀      █      ██  
      ▄██    ███    █████████  ██  
    ▀▀██▄  ▄█▀ ██▄      █      ██  
       ██▄██▄   ▄██▄    █    ▄████▄
███  ▄█▀                           
 █████▀                            

By dsxz19-2
Copywrite dsxz19-2

"Young mathematicians are warned not to wast time on this conjecture. So I forced a computer to do it for me. :)"
-me
P.S Your going to need a powerful computer
""")
num = 295147905179352825856

def calculate(num):
   while True:
      try:
         if (num % 2) == 0:
            num = num/2
            if (num == 1):
               print("[-] Does not disprove conjecture.")
               break
            else:
               exit()
         else:
            num = (num * 3) + 1
      except:
         pass

while True:
   print("\n[+] Calculating for " + str(num))
   calculate(num)
   time.sleep(sleep)
   num = num + 1
