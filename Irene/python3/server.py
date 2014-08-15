#!/usr/bin/env python3
 
import http.server
import http.server
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
server_address = ("", 8000)
#handler.cgi_directories = ["/cgi-bin/"]
handler.cgi_directories = ["/cgi-bin"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
