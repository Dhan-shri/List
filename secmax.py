num = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
k=num[0]
while i<len(num):
    if num[i]>k:
        k=num[i]
    i=i+1
num.remove(k)
j=0
a=num[0]
while j<len(num):
    if num[j]>a:
        a=num[j]
    j=j+1
print(a)
      
    