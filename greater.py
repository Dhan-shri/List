# numbers=[50, 40, 23, 70, 56, 12, 10, 7] 
# i=0
# c=[]
# while i<len(numbers):
#     num=numbers[i]
#     if num>20 and 40>num:
#         c.append(num)
#     i=i+1
# print(c)
# print( "the length of list is ",len(c))

numbers=[50, 40, 23, 70, 56, 12, 10, 7]
i=0
c=[]
k=[]
while i<len(numbers):
    num=numbers[i]
    if num>20:
        c.append(num)
    if num<40:
        k.append(num)
    i=i+1
print(c)
print(k)