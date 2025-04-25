#1.print 2 lists by using single line
l1=[1,2,3]
l2=['a','b','c']
print(l1+l2)
#l1.extend(l2)
#print(l1)
print([*l1,*l2])
print([i for i in l1+l2])


#2.print even numbers in list
l=[1,2,3,4,5,6,7,8,9,10]
print([i for i in l if i%2==0])