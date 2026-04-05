#Accept 4 numbers & find max number
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
n4=int(input("Enter the number:"))
max=n1
if max<n2:
    max=n2
if max<n3:
    max=n3
if max<n4:
    max=n4
print("The maxx number is: ",max)