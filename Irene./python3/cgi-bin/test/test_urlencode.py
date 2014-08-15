#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
val1 = form.getvalue('first')
val2 = form.getvalue('last')
 
#print "Content-type: text/html"
#print '''
#<html><head><title>Test URL Encoding</title></head><body>
#Hello my name is
#</body></html>
#'''
#print """ 
#<html><head><title>Test URL Encoding</title></head><body>
#Hello my name is %s %s
#</body></html>""" % (val1, val2)


print ("Content-type: text/html")
print ('''
<html><head><title>Test URL Encoding</title></head><body>
<a href="http://localhost:8000/cgi-bin/test_urlencode.py?first=Jack&last=Trades">Link</a>
''')
print (val1)
print ("</body></html>")
