def prime(start,end):
    for num in range(start, end + 1):
        if num== 1:  
            continue
        for i in range(2, num):
            if num % i == 0:
                break  
        else:
            print(num)  
start=int(input("enter starting range:"))
end=int(input("enter ending range:"))
prime(start,end)
