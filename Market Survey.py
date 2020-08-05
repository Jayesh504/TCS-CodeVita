from collections import Counter

n = int(input())

m=int(input())

d=list(map(int,input().split()))

s=[]

for i in range(m):

    x = list(map(int,input().split()))

    s.append(x)

   

r=[]

r.append(d)

def cmp(x,y):

    c=0

    p=0

    for i in range(len(d)):

        if x[i]==y[i]:

            c+=1

    return(c)

 

def latest(r1):

    r.append(r1)

    r.reverse()

    z = list(zip(*r))

    l = []

    for i in range(0,len(z)):

        occurence_count = Counter(z[i])

        l.append(occurence_count.most_common(1)[0][0])

    return(l)

x=d

for i in range(m):

    y=s[i]

    print(cmp(x,y))

    l=latest(y)

#     print(l)

    x=l  #latest key as a fanal key

   

result=[]

for i in range(m):

    y=s[i]

    p=cmp(x,y)

    result.append(p)

   

print(result.index(max(result))+1,max(result))