def groovingmonkeys(a):

    y = a   #containing replaced value

    x=[0]*len(a)   #used as a buffer
    #print(x)
    count=0

    while(x!=a):

        count+=1

        x=[0]*len(a)    #refresh the x
        #print(x)
        for i in range(len(a)):
            #print(i)
            x[a[i]-1] = y[i]
            #print(x)
            #print(y) 
        y=x

    return(count)

 
T = int(input())     #no of test cases

for i in range(T):

    n = int(input())

    monkeys = list(map(int,input().split()))  #monkeys[]

    result = groovingmonkeys(monkeys)

    print(result)

