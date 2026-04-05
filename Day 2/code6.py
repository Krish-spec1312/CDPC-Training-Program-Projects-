#To print all the amstrong numbers from 1 to 10000
for i in range(1,10000):
    no=i
    sum=0
    temp=no
    count = 0
    while no>0:
        no=no//10
        count=count+1
    no=temp
    while no>0:
        rem=no%10
        sum=sum+rem**count
        no=no//10
    if temp==sum:
        print("The amstrong numbers between 1 and 10000 are: ",i)