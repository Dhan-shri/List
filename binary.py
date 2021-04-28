binary = [1, 0, 0, 1, 1, 1, 1, 1] 
l=len(binary)
i=0
sum=0
while i<l:
    num=binary[l-i-1]
    sum=sum+num*(2**i)
    i=i+1
print(sum)


