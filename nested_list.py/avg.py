marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
l=len(marks)
while i<len(marks):
    j=0
    sum=0
    avg=0
    while j<len(marks[i]):
        if i==0:
            sum=0
            j=0
            while j<len(marks[i]):
                num=marks[i][j]
                sum=sum+num
                j=j+1
                avg=sum/len(marks[i])
            print("avg of first year:", avg)
        if i==1:
            sum=0
            j=0
            avg=0
            while j<len(marks[i]):
                num=marks[i][j]
                sum=sum+num
                j=j+1
                avg=sum/len(marks[i])
            print("ave of second year:",avg)
    i=i+1
