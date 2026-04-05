#Writing a code to reverse any type of number given by the user
no=int(input("Enter any number from the user: "))
rev=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("The reversed number is: ",rev)