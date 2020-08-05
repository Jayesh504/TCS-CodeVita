for i in range (int(input())):
    N = int(input())
    arr = []
    for i in range(1,N+1):
        if N % i == 0:
            arr.append(i)
for i in arr:
    print(i, end=" ")