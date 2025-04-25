sq=lambda x:x*x
print(sq(5))
list1=[1,2,3,4]
double=list(map(lambda num:num*2,list1))
print(double)
l=[10,15,12,13,14,12,11,6]
d=list(filter(lambda y:y>=12,l))
print(d)

def make_multiplier(n):
    return lambda z:z*n
op=make_multiplier(4)(5)
print(op)