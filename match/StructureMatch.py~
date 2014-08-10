import itertools
import TypeMatch

def StructureMatch(user,design):
    #print('user')
    #print(user)
    #print('design')
    #print(design)
    if len(design.keys())==0:
        return [1,{}]
    if len(user.keys())==0:
        return [0,{}]
        
    DU={}
    matchDU={}
    for iD in design:
        DU[iD]={}
        matchDU[iD]={}
        for iU in user:
            #print('====')
            #print([user[iU],design[iD]])
            [DU[iD][iU],matchDU[iD][iU]]=StructureMatch(user[iU],design[iD])
            DU[iD][iU]+=TypeMatch.TypeMatch(iU,iD)

    #print(DU)

    lenDesKey=len(design.keys())
    cU = itertools.combinations(user.keys(), lenDesKey)
    cD = list(design.keys())
    maxS=0;
    for iU in cU:
        s=sum([DU[cD[i]][iU[i]] for i in range(lenDesKey)])
        if s>maxS:
            maxS=s
            best=iU
        #print(s)
        #print(iU)

    ans={}
    for i in range(lenDesKey):
        ans[cD[i]]=[best[i], matchDU[cD[i]][best[i]]]

    return [maxS,ans]
    #print(ans)

user={'Place':{},
      'String':{
          'Time':{},'Number':{}},
      'Time':{}}
design={'Place':{},
        'String':{
            'Time':{}} }
#design={'Place':{},
        #'String':{}}
print(StructureMatch(user,design))
