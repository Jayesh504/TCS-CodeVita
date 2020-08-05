n=int(input())
t=int(input())
ply=[]
for i in range(n):
    x=list(map(int,input().split()))
    y=x[-1]
    x=x[:-1]
    x[0]=x[0]*y
for i in range(1,t):
    x[i] *= y
    x[i] += x[i-1]
    ply.append(x)
if t%2==0:
    t -= 2
else:
    t -= 1
d={}
for i in range(1,n+1):
    d[i] = 0
for i in range(2,t+1,2):
    m = 0
    t1 = []
    for j in range(n):
        x = ply[j][i-1]
if m < x:
    m = x
    t1 = []
    t1.append(j+1)
elif m == x:
    t1.append(j+1)
for k in t1:
    d[k] += 1
    m = max(d.values())
for i in d.keys():
    if d[i] == m:
        print(i)
        break