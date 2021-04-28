# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19] 
# i=0
# sum=0
# k=[]
# while i<len(n):
#     num=n[i]
#     a=number-num
#     k.append(num)
    
n=[10,11,12,13,14,17,18,19]
number=30
i=0
k=[]
while i<len(n):
    b=0
    while n[i]>n[b]:
        if n[i]+n[b]==number:
            k.append([n[i],n[b]])
        b=b+1
    i=i+1
print(k)