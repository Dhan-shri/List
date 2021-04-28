places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
i=0
l=len(places)
k=[]
while i<len(places):
    n=places[i]
    n=places[l-i-1]
    k.append(n)
    i=i+1
print(k)