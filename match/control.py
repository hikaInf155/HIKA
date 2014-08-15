import SM
import re
import json

f= json.loads(open('j.json').read()) 
g= json.loads(open('data.json').read())

a=SM.BuildStructure(f)
#__SearchTree(a)
b=SM.BuildStructure(g)
SM.StructureMatch(a,b)
print(b.grade)
print(SM.SearchTree(b))
dic=SM.SearchTree(b)

exp_file=open('example.html','r')
out_file=open('out.html','w')
for i in exp_file:
    tmp=i
    for key in dic:
        tmp=re.sub('"'+key+'"','"'+dic[key]+'"',tmp)
    print(tmp)
    print(tmp,end='',file=out_file)
out_file.close()
exp_file.close()
