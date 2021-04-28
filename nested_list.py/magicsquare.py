magic = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
i=0
while i<len(magic):
    j=0
    sum=0
    while j<len(magic[i]):
        num=magic[i][j]
        sum=sum+num
        j=j+1
    i=i+1
# k=1
# while k<len(magic):
#     j=0
#     s=0
#     while j<len(magic[k]):
#         num1=magic[k][j]
#         s=s+num1
#         j=j+1
#     k=k+1
# print(sum)
# print(s)



