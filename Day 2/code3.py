#Find the sum of the digits of any given number
no=int(input("Enter the number: "))
sum=0
while no>0:
    rem=no%10
    sum=sum+rem
    no=no//10
print("The sum of the digits is: ",sum)


