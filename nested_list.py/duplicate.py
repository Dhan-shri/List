# n = [17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# i=0
# k=[]
# count=0
# num=n[i]
# while i<len(n):
#     b=0
#     if n[i]==n[b]:
#         k.append(num)
#         b=b+1
#     i=i+1
# print(k)


n = [17, 12, 17, 17, 18, 10, 17,15, 14, 12, 19, 17, 12, 13, 11] 
i=0
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            del n[i]
        j=j+1
    i=i+1
print(n)

