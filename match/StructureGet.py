def StrGet(inp):
    if isinstance(inp,(set,dict,list)):
        return 'Set'
    else:
        try:
            a=float(inp)
            return 'Number'
        except ValueError:
            return 'String'

a={'hello':'3',
    'aa':4,
    'ab':[1,2,3]}
print(StrGet(a))
print(StrGet('f23'))
print(StrGet('23'))
for key, value in a.items():
    print(key)
