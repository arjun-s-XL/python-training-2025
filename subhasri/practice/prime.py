low=int(input("enter a number:"))
up=int(input("enter a number:"))
def prime(low,up):
    for num in range(low,up+1):
        if num==1:
            continue
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
prime(low,up)