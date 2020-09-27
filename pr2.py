import array as arr
a=arr.array('u','bob') #we can create array of character by using 'u' typecode
b=arr.array('u',['h','b','g']) #ctl+/ use for cmt
print(b)
print(a)

for i in range(len(b)):
    print(b[i])
