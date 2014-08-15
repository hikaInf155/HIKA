import SM
import re
import json
import os


def control(exp_path):
    #os.system('copy ..\json_file.json '+path)
    path='cgi-bin/'+exp_path
    os.system('cp json_file.json '+path)
    user_json= json.loads(open(path+'/json_file.json').read())
    exp_json= json.loads(open(path+'/j.json').read()) #example json file

    user_struct=SM.BuildStructure(user_json)
    #__SearchTree(a)
    exp_struct=SM.BuildStructure(exp_json)
    SM.StructureMatch(user_struct,exp_struct)
    #output grade===== print(b.grade)
    #print(SM.SearchTree(b))
    dic=SM.SearchTree(exp_struct)
    print(dic)
    dic["j.json"]="json_file.json"
    
    exp_file=open(path+'/example.html','r')
    out_file=open(path+'/out.html','w')
    for i in exp_file:
        tmp=i
        for key in dic:
            tmp=re.sub('"'+key+'"','"'+dic[key]+'"',tmp)
            #print(tmp)
        print(tmp,end='',file=out_file)
    out_file.close()
    exp_file.close()
    return exp_struct.grade

#with open('log','w') as fi:
    #print(os.getcwd(),file=fi)
#control('type2')
