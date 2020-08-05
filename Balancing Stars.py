string = str(input())

open=['[','{',"("]

close=[']','}',')']

stack=[]

count=0

br=0   #brackets counting

sc=0   #stars counting

f=0    #if conditon failed

ob=0   #for open brackets

obs=0  #for counting open bracket stars

for i in string:

    if i in open:

        stack.append(i)

        br=br+1

        ob=1    

        obs=0

    elif i=='*' and ob==1:

        sc=sc+1

        obs=obs+1

    elif i in close:

        pos = close.index(i)

        if (len(stack)>0) and (open[pos] == stack[len(stack)-1]):

            stack.pop()

            if obs==0 or obs==1:

                br=br-1

                f=1

            if sc>=2:

                count = count + br

                sc=0

                ob=0

                br=0

            elif ob==1:

                f=1

        else:

            f=1

           

if len(stack)==0 and f==0 and count>0:

    print('Yes',count, end="")

else:

    print('No',count, end="")