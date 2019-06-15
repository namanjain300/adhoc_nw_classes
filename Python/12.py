# Problem 12: 

# write a python code to do the following

# i)  take input from user and search in google
# ii)   pick the first 3 url of google search
# iii)  make  QR-code of all 3 url's
# iv)   Store all these qr-code in  apache web server in aws cloud
# v)   share link of qrcode using aws public IP

# Note:   v) option you can do it manually there is no need of programing

import os
import subprocess
import time
from googlesearch import search 
search1=input('Type your search here')
url= 'http://www.google.com/search?q='+search1
for i in search(url,stop=3):
    print(i)
    time.sleep(1)
    j = subprocess.Popen(qrencode -s 16X16 -o i.png i,
            stdout=subprocess.PIPE
            stderr=subprocess.STDOUT)
     


