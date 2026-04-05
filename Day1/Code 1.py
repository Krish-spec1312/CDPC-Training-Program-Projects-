# Take a 3 digit number from the user and find the sum of the 3 digits in the number without using any loop
x = int(input("Enter the number:"))
a = x//100
b= (x//10)%10
c=(x%10)
sum_digits=a+b+c
print("Sum of digits= ", sum_digits)