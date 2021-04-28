num = [50, 40, 23, 70,100,67,99, 56, 12, 5, 10, 7] 
i=0
k=num[0]
while i<len(num):
    if num[i]>k:
        k=num[i]
    i=i+1
print(k)
