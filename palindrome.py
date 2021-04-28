name=[ 'n', 'i', 't', 'i', 'n' ] 
i=0
l=len(name)
k=[]
while i<l:
    n=name[i]
    n=name[l-i-1]
    k.append(n)
    i=i+1
if k==name:
    print("it is palindrome ")
else:
    print("it is not palindrome")







