#n1 = int(input())
#n2 = int(input())
n1,n2 = map(int,input().split())
list1 = []
list2 = []
list3 = []
for i in range(n1,n2):
    count = 0
    #print(i)
    for j in range (2,int(i//2)+1):
        if (i%j==0):
            count+=1
    if (count==0):
        list1.append(i)
for k in range(len(list1)):
    for l in range(len(list1)):
        if (k!=l):
            list2.append(int(str(list1[k])+str(list1[l])))
for i in range(len(list2)):
    count=0
    for j in range(2,list2[i]//2):
        if(list2[i]%j==0):
            count+=1
    if(count==0):
        list3.append(list2[i])
list3.sort()
s = list3[0]
large = list3[len(list3)-1]
res = []
for i in list3:
    if i not in res:
        res.append(i)
temp = 0
for p in range(len(res)-2):
    temp=s+large
    s=large
    large=temp
print("Final",temp)
    