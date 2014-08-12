#!/usr/bin/env python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

 #Get data from fields
if form.getvalue('v1'):
  v1= form.getvalue('v1')
else:
  v1= "Not entered"
if form.getvalue('v2'):
  v2= form.getvalue('v2')
else:
  v2= "Not entered"
if form.getvalue('v3'):
  v3= form.getvalue('v3')
else:
  v3= "Not entered"


print ("Content-type:text/html")
print ('''
<html>
	<head>
		<title>Data Visualization</title>
	</head>''')
print("<body>")
print("<h2>selected variable one is "+v1+"</h2>")
print("<h2>selected variable one is "+v2+"</h2>")
print("<h2>selected variable one is "+v3+"</h2>")
print("</body>")
print("</html>")