#Take the reverse of 6 digit number
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
res=n1*100000+n2*10000+n3*1000+n4*100+n5*10+n6
print(res)