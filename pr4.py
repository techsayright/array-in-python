import array as arry
a=arry.array('i')

# for i in range(len(a)):
for i in range(5):
    a.append(int(input("enter the value:")))
print(a)

sum=0
for i in range(len(a)):
    sum=sum+i
print("sum:",sum)

