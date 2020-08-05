n=int(input())

f=[0,1] #previous two sub factorials

i=3

if n==1:

    print(f[n-1])

elif n==2:

    print(f[n-1])

else:

    while i<(n+1):

        f.append(((i-1)*(f[0]+f[1]))%1000000007)

        f.pop(0)

        i=i+1

print(f[1],end="")
#print(f)