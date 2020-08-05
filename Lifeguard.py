x_1=1
y_1=1
x_w=1
y_w=-1
f=1.2
x_b=x_w+1
temp=((x_1-x_w)*2+(y_1-y_w)*2)
while(1):
    d_w=((x_w-x_b)**2+(y_w)**2)**(1/2)
    d_b=((x_w-x_1)**2+(y_1)**2)**(1/2)
    time=d_w+(d_b/f)
    if(time<=temp):

        temp=time
        #print(time)
        x_b=x_b-0.000005

    else:
        break
print (round(x_b+0.01,6))