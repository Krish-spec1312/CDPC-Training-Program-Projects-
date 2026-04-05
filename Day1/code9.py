#Accept basic salary and find gross salary where
#TA=20%
#DA=30%
#HRA=40%
Basic=int(input("Enter the salary: "))
TA=Basic*0.20
DA=Basic*0.30
HRA=Basic*0.40
Gross_salary=Basic+TA+DA+HRA
print(Gross_salary)