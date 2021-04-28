elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
s=0
k=[]
c=[]
while i<len(elements):
    num=elements[i]
    if num %2==0:
        k.append(num)
        sum=sum+num
        # avg=(sum+num)/len(k)
    else:
        c.append(num)
        s=s+num
        # avg1=(s+num)/len(c)
    i=i+1
print("avg of even number:",sum/len(k))
print("avg of odd number:",s/len(c))
