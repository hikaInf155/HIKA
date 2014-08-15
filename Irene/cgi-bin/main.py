#!/usr/bin/env python3

import cgi,cgitb
import combined
import control
import os

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

combined.take_user_variables(v1, v2, v3)

grade_type1=control.control('type1')
grade_type2=control.control('type2')

print('''
<html>
	<head>
		<title>Data Visualization</title>
	</head>
  <body>
      This is the result for grade the data form user to a specific type of chart.<br>
      <a href="type1/out.html">type1</a> grade:{0}
      <br>
      <a href="type2/out.html">type2</a> grade:{1}
  </body>
</html>
'''.format(grade_type1,grade_type2))
