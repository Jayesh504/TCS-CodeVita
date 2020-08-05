n = 3
s = 8
aa = map(int,input().split())
bb = map(int,input().split())
cc = map(int,input().split())
a = list(aa)
b = list(bb)
c = list(cc)
#print(a)
r = []
for i in range(n):
    for j in range(s):
        if i == 0:
            if j == 2:
                 ax = a[-1]*(a[0]+a[1])
                 bx = b[-1]*(b[0]+b[1])
                 cx = c[-1]*(c[0]+c[1])
                 if ax>bx and ax>cx:
                    r.append('a')
                 elif bx>ax and bx>cx:
                    r.append('b')
                 else:
                    r.append('c')
           
        if i == 1:
            if j == 4:
                ax = a[-1]*(a[0]+a[1]+a[2]+a[3])
                bx = b[-1]*(b[0]+b[1]+b[2]+b[3])
                cx = c[-1]*(c[0]+c[1]+c[2]+c[3])
                if ax>bx and ax>cx:
                    r.append('a')
                elif bx>ax and bx>cx:
                    r.append('b')
                else:
                    r.append('c')
        if i == 2:
            if j == 6:
                ax = a[-1]*(a[0]+a[1]+a[2]+a[3]+a[4]+a[5])
                bx = b[-1]*(b[0]+b[1]+b[2]+b[3]+b[4]+b[5])
                cx = c[-1]*(c[0]+c[1]+c[2]+c[3]+b[4]+b[5])
                #print(ax,bx,cx)
                if ax>bx and ax>cx:
                    r.append('a')
                elif bx>ax and bx>cx:
                    r.append('b')
                else:
                    r.append('c')
print(r)
if r.count('a')>r.count('b') and r.count('a')>r.count('c'):
    print(1)
elif  r.count('b')>r.count('a') and r.count('b')>r.count('c'):
    print(2)
else:
    print(3)
        