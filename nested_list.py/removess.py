# mainStr = ("the quick brown fox jumped over the lazy dog. the dog slept over the verandah.")
# subStr = ("over")
# mainStr=[]
# mainstr_list= mainStr.split("-")
# print(mainstr_list)
# mainStr.remove(subStr)
# print(mainStr)
# #  li = list(string.split("-"))
# #     return li



list=[]
a=input("enter a task")
i=0
while i<len(a):
    list.append(a[i])
    i=i+1
print(list)
j=0
b=input("enter a task")
while i<len(b):
    if b[j]==a[i]:
        del (b[i])
    j=j+1
print(list)