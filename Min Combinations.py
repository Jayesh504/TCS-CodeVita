import math
t = int(input())

for i in range(0,t):

    n1,n2 = map(int,input().split())

    print(math.gcd(n1,n2))