#!/usr/bin/env python
 
import sys
import cgi

form = cgi.FieldStorage()
 
val1 = form.getvalue('file')
print "Content-Type: application/json\n\n"
f=open(val1,'r')
for i in f:
    print(i)
