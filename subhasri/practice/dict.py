d={'a':1,'b':2,'c':4,'d':5,'e':6}
keys=list(d.keys())
vals=list(d.values())
print(keys)
print(vals)
d1={}
for i in range(len(d)):
    d1[vals[i]]=keys[i]
print(d1)


