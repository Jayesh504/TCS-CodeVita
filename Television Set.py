n = int(input("Enter: "))
month=[31,28,31,30,31,30,31,31,30,31,30,31]
patients=[]
for m in range(len(month)):
    for d in range (month[m]):
        temp=(6-(m+1)) **2+abs (d-15)
        patients.append(temp)
for i in range (n,1,-1):
    rtv=n-i
    rntv=i
    cost=0
    for p in range(len(patients)):
        if(patients[p]>=n):
            cost=cost+1000*rntv+1500*rtv
        elif(rntv<=patients[p]<n):
            cost=cost+1000*rntv+1500* (patients[p]-rntv)
        else:
            cost=cost+1000*patients[p]
    if(cost>= 7000000) :
       print("total TV Rooms", rtv)
       break