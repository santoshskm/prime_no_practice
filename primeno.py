number = int(input("enter a number: "))
sqrt = number ** 0.5
print("square root:", sqrt)
n=int(sqrt)
n+=1
for num in range(2,n+1):
    for item in range(1,num+1):
        r=num%item
        count=0
        if(r==0):
            count+=1
        else:
            continue
    if(count==2):
        print(n,"is prime no")
        
    
        
        