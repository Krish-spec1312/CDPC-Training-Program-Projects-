#How to use the list function
ls=[]
print(type(ls))
print(ls)

ls=list()
print(type(ls))

ls=[11,22,33,44,55,66,77]
print(ls)

ls=[11,22,33,44,55,66,77,88,99]
print(ls)
for i in range(len(ls)):
    print(ls[i])


for x in ls:
    print(x)


ls=[11,22,33,44,55,66,77,88,99,100]
print(ls[0])
print(ls[5])
print(ls[-1])
print(ls[-2])
print(ls[2:5])
print(ls[3:7])
print(ls[:5])
print(ls[4:])
print(ls[:])
print(ls[::1])
print(ls[::2])
print(ls[::-2])
