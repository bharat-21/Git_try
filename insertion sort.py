number=[int(x) for x in input("Elements ").split()]

print("your entered list is "+ str(number))

for idx,val in enumerate(number[1:],start=1):
    temp = val
    ptr = idx-1
    while (temp<=number[ptr]):
        number [ptr+1]= number[ptr]
        ptr = ptr-1
    number[ptr+1]=temp

print("your sorted list is "+ str(number))