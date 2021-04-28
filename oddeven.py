elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
k=[]
c=[]
while i<len(elements):
    num=elements[i]
    if num%2==0:
        k.append(num)
    else:
        c.append(num)
    i=i+1
print(k)
print("the total even number:",len(k))
print(c)
print("the total odd number",len(c))
