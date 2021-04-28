que_list=[
    "who is the prime minister of our india?",
    "which is the national flower of india?",
    "which is capital of maharashtra?"
]
optional_list=[ [ "1.Devendra Fadvanis","2.narendra modi", "3.Rajnath Singh","4.manmohan singh"],
                ["1.lotus","2.rose","3.Mogra","4.lily"],
                ["1.pune", "2.nagpur","3.mumbai","4.gondia"]
]
solution_list=[2, 1, 3]
lifeline_option=[["1. Devendra Fadvnis","2.Narendra Modi"],["1.lotus","2.Mogra"],["1.nagpur","2.mumbai"]]
lifeline_solution=[2,1,2]
print("welcome to KBC😁😁")
print("here we go")
i=0 # for question list
j=0 # for optional list
a=0 #for solution list
l=0
n=0
count=0
while i<len(que_list):
    print("aapka sawal hai")
    print(que_list[i])
    # while j<len(optional_list):
    k=0 #for list in optional_list
    # count=1
    while k<len(optional_list[j]):
        print(optional_list[j][k])
        # count=count+1
        k=k+1
    j=j+1
    lifeline=input("Do you want lifeline or not")
    if count<1:
        if lifeline=="yes":
            while l<len(lifeline_option):
                l1=0
                while l1<len(lifeline_option[l]):
                    print(lifeline_option[l][l1])
                    l1=l1+1
                life_option=int(input("choose option from lifeline"))
                if life_option==lifeline_solution[n]:
                    print("your option is correct")
                    break
                else:
                    print("your lost your one lifeline,sorry")
                # count=count+1
        else:
            print("what you think which is the correct answer")
            option=int(input("choose one option:"))
            if option==solution_list[a]:
                print("your option is correct. congratualtion") 
            else:
                print("your option is not correct.")  
                break
            a=a+1
        count=count+1
        l=l+1
        n=n+1
    else:
        print("sorry your lifeline is finished")
    # a=a+1
    i=i+1
  
    