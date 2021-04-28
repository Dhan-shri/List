elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
s=0
while i<len(elements):
    num=elements[i]
    if num%2==0:
        sum=sum+num
    else:
        s=s+num
    i=i+1
print("sum even number:",sum)
print("sum of odd number:",s)