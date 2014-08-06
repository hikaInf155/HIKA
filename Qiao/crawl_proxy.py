import urllib.request
import re
crawl_proxy_output=open("table3_1.txt","w")
url="http://wdi.worldbank.org/table/3.1"
proxy_support = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
content = urllib.request.urlopen(url).read()
print(content,file=crawl_proxy_output)
crawl_proxy_output.close()

>\(\d\+\.\d\+\)<
