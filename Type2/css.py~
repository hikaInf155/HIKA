#!/usr/bin/env python
 
import sys
import cgi

form = cgi.FieldStorage()
 
val = form.getvalue('file')
print "Content-Type: application/css\n\n"
f=open(val,'r')
for i in f:
    print(i)
