elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
k=[]
c=[]
sum=0
s=0
while i<len(elements):
    num=elements[i]
    if num%2==0:
        k.append(num)
        sum=sum+num
    else:
        c.append(num)
        s=s+num
    i=i+1
a=sum+s
print("total odd number in list:",len(k))
print("sum of even number:",sum)
print("avg of even number:",sum/len(k))
print("total sum number in list:",len(c))
print("sum of odd number:",s)
print("avg of odd number:",s/len(c))
print("total number in list:",len(elements))
print("sum of total number:",a)
print("avg of total number:",a/len(elements))