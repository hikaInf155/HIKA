#!/usr/bin/env python3
 
print("Content-type: text/html")
f=open("cgi-bin/index.html",'r')
for i in f:
    print(i)
