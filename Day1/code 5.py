# Take a 6 digit number from the user and find the sum of the 6 digits in the number without using any loop
no=int(input("Enter the 6-digit number: "))
n1=no%10;
no=no//10;
n2=no%10
no=no//10;
n3=no%10
no=no//10;
n4=no%10
no=no//10;
n5=no%10
no=no//10;
n6=no%10
res=n1+n2+n3+n4+n5+n6
print(res)
