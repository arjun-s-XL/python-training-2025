lb=int(input("enter lower bound: "))
ub=int(input("enter upper bond: "))
for num in range(lb,ub+1):
    if num==1:
        continue
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num) 
