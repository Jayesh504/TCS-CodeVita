import math
a=int(input())
for i in range(a):
    count=0
    temp=0
    n,t,m=list(map(int,input().split()))
    for i in range(n):
        c=0
        for j in range(i+(t-1),n):
            count=count+1
            c=c+1
        if (m>0):
            temp=temp+c
            m=m-1
    #print(temp,count)
    s=float(temp/count)
    #print(s)
    print(math.ceil(s*1000000007))
    
