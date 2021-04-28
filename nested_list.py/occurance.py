# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
# i=0
# k=[]
# b=char_list[0]
# while i<len(char_list):
#     char=char_list[i]
#     # count=0
#     if b==char:
#         k.append(b)
#         count=len(k)  
#         b=char_list[i]                                                                                                                                                                                                                                                                                  
#     i=i+1
# print([b,count])



# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
# i=0
# k=[]
# a=[]
# while i<len(char_list):
#     num=char_list[i]
#     j=0
#     count=0
#     while j<len(char_list):
#         if num==char_list[j]:
#             del char_list[j]
#             count=count+1
#         k.append(char_list)
#         a.append(count)
#         j=j+1
#     i=i+1
# print([k,a])
            

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
k=[]
while i<len(char_list):
    num=char_list[i]
    j=1
    while j<len(char_list):
        
    x=char_list.count(num)
    # print([num,x])
    i=i+1
    print([num,x])

















    
