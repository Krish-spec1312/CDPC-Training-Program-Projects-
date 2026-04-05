#Check whether the given number is palindrome or not
no=int(input("Enter any number from the user: "))
rev=0
temp=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
if temp==rev:
    print("The given number is palindrome")
else:
    print("The given number isn't palindrome")
