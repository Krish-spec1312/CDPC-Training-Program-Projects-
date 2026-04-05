# Take a 3 digit number from the user and find the sum of the 3 digits in the number without using any loop
no=int(input("Enter the number:"))
n1=no%10;
no=no//10;
n2=no%10
no=no//10;
n3=no%10
res=n1+n2+n3
print(res)