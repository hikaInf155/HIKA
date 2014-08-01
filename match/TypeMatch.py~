import pickle

def TypeChain(inp,dic)->list:
    if dic[inp]=="":
        ans=[inp]
    else:
        ans=TypeChain(dic[inp],dic)
        ans.append(inp)
    return ans

dicFile=open('dataDic.dat','rb')
dataDic=pickle.load(dicFile)
dicFile.close()

a='String'
b='Place'
aC=TypeChain(a,dataDic)
bC=TypeChain(b,dataDic)
n=0
minLen=min(len(aC),len(bC))
while n+1<minLen and aC[n+1]==bC[n+1]:
    n+=1
print(n)

