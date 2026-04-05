#Accept 9 digit no and find sum of 1st and ;ast digit in 3 steps
x=int(input("Enter the 9 digit number: "))
n1=x%10
n2=x//100000000
res=n1+n2
print(res)