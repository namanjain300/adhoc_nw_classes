# Problem 2 : 
# write a code using  that will take user input from and search on google and store top 10 url in the list.
# conditions : 
#     i )   URL must be stored permanently as well
#     ii)   user can give input using keyboard and  voice both

import webbrowser
import time
from googlesearch import search
search1=input('Type your google search = ')
url= 'http://www.google.com/search?q='+search1
# webbrowser.open_new_tab(url)
list1 = []
for i in search(url,stop=10):
    print(i)
    time.sleep(1)
    list1.append(i)
print(list1)
f = open('url.txt','a+')
for i in list1:
    f.write(i+'\n')
f.close()


 
