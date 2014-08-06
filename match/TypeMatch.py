import pickle

#def TypeChain(inp,dic) -> list:
def TypeChain(inp,dic):
    if dic[inp]=="":
        ans=[inp]
    else:
        ans=TypeChain(dic[inp],dic)
        ans.append(inp)
    return ans

def TypeMatch(a,b):

    """
    Compute how like two types is.

    >>> TypeMatch('String','Place')
    1
    """

    dicFile=open('dataDic.dat','rb')
    dataDic=pickle.load(dicFile)
    dicFile.close()

    aC=TypeChain(a,dataDic)
    bC=TypeChain(b,dataDic)
    n=0
    minLen=min(len(aC),len(bC))
    while n+1<minLen and aC[n+1]==bC[n+1]:
        n+=1
    return n

#print(TypeMatch('String','Time'))
if __name__ == "__main__":
    import doctest
    doctest.testmod()
