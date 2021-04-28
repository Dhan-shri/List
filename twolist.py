list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
i=0
k=[]
while i<len(list1):
    num=list1[i]
    if num  not in list2:
        k.append(num)  
    i=i+1
print(k)