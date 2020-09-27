import array as arr

a= arr.array('I',[10,3,4,5,6]) #arry takes max 2 arguments in array()

print(a)

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i],end=" ")
print("hi",end=" ")
print(type(a))

a.insert(2,56)
print(a)

a.insert(1, 4)
print ("Array after insertion : ", end =" ")
for i in a:
    print (i, end =" ")
