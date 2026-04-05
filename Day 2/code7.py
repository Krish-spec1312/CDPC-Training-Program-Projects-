#to get the logic of sum=1+x^1+x^2-------------n
n=int(input("Enter n: "))
x=int(input("Enter x: "))
sum=1
for i in range(1,n):
    sum=sum+(x**1)/i
    print(sum)