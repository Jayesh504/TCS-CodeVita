n = input()
x = []
for i in range (int(n)):
    x.append(int(input()))
for i in range(len(x)):
    temp = 0
    count = 0
    for j in range(1, x[i]):
        temp+=j
        count+=1
        if(temp>=x[i]):
            print("No of coins",count)
            break