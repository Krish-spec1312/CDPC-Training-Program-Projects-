#Check whether the given number is armstrong or not
no=int(input("Enter the number: "))
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
    print("The given number is a armstrong number")
else:
    print("The given number is not a armstrong number")