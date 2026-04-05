#To count the number of digits in the given number
no=int(input("Enter the number: "))
count = 0
while no>0:
        no=no//10
        count=count+1
print(count)
