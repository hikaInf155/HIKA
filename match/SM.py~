import copy
import itertools
import json

class MyList(list):
    def __eq__(self,inp):
        if len(self)!=len(inp):
            return False
        if (not self) and (not inp):
            return True
        for i in self:
            tmp=False
            for j in inp:
                if (i==j):
                    tmp=True
                    break
            if not tmp:
                return False
        return True

    def add(self,inp)->None:
        #for i in self:
            #if i==inp:
                #return self
        self.append(inp)
        return self

class TypeNode:
    def __init__(self,value='value',child=[],key=''):
        self.child=MyList(child)
        self.type_of_data=value
        self.key=key
        self.match=''
        self.grade=0
    
    def __eq__(self,inp):
        return (self.type_of_data==inp.type_of_data)and\
                (self.child==inp.child)

def __TypeCompare(a,b):
    #print("TypeCopmare")
    #print(a.key,' ',b.key)
    #print(a.type_of_data,' ',b.type_of_data)
    #print(a.type_of_data==b.type_of_data)
    if a.type_of_data==b.type_of_data:
        return 1
    else:
        return 0

def StructureMatch(user,design):
    #if (not user.child)or(not design.child):
    len_user_child=len(user.child)
    len_design_child=len(design.child)
    if (len_design_child>len_user_child)or(len_user_child==0):
        design.match=user.key
        design.grade=__TypeCompare(user,design)
        return design
        
    len_user_child=len(user.child)
    len_design_child=len(design.child)
    grade_between_UD=[copy.deepcopy(design.child) for i in range(len(user.child))]
    for i in range(len_design_child):
        for j in range(len_user_child):
            grade_between_UD[j][i]=StructureMatch(user.child[j],grade_between_UD[j][i])

    
    tmp = itertools.permutations(range(len_user_child), len_design_child)
    maxS=-10;
    best=[]
    for i in tmp:
        s=sum([grade_between_UD[u][d].grade for d in range(len_design_child) for u in i])
        print([s,maxS])
        if s>maxS:
            maxS=s
            best=i
    print(best)
    for d in range(len_design_child):
        print('d ',d)
        design.child[d].grade=grade_between_UD[best[d]][d].grade
        design.child[d].match=grade_between_UD[best[d]][d].match
    design.grade=maxS+__TypeCompare(user,design)
    design.match=user.key
    return design

def BuildStructure(inp):
    type_of_inp=type(inp).__name__
    if type_of_inp == 'list':
        ans=TypeNode('List')
        ans.child.add(BuildStructure(inp[0]))
    elif type_of_inp == 'dict':
        ans=TypeNode('Dict')
        for i in inp:
            #print(i)
            tmp=TypeNode('String',key=i)
            tmp.child.add(BuildStructure(inp[i]))
            ans.child.add(tmp)
    elif type_of_inp == 'str':
        ans=TypeNode('String',key=inp)
    else:
        ans=TypeNode('Number')
    return ans

def __SearchTree(inp):
    print(inp.key,'-',inp.match,' ',inp.key)
    if inp.child:
        print("===")
        #print(inp.child)
        #print(type(inp.child))
        for i in range(len(inp.child)):
            __SearchTree(inp.child[i])
            #print(type(inp.child[i]))

f= json.loads(open('f.json').read())
a=BuildStructure(f)
g= json.loads(open('g.json').read())
b=BuildStructure(g)
StructureMatch(a,b)
print(b.grade)
__SearchTree(b)

#print(a.type_of_data)
#print([a.child[i].key for i in range(len(a.child))])
#b=a.child[0].child
#print(b.child[0].type_of_data)

#st=TypeNode('String',key='stD')
#nu=TypeNode('Number',key='nn')
#design=TypeNode('value',[st,TypeNode('Number',key='nD')])
#user=TypeNode('value',[TypeNode('Number',key='nU'),TypeNode('String',key='stU')])
#print(design==user)
#StructureMatch(user,design)
#print(design.grade)

