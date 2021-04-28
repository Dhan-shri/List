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
l=0 #for lifeline_option list
n=0
count=0
while i<len(que_list):
    print(que_list[i])
    k=0
    while k<len(optional_list[j]):
        print(optional_list[j][k])
        k=k+1
    j=j+1
    print("you can choose only one lifeline")
    lifeline=input("DO YOU WANT LIFELINE OR NOT")
    count=0
    if count<1:
        if lifeline=="yes":
            l1=0
            while l1<len(lifeline_option[l]):
                print(lifeline_option[l][l1])
                l1=l1+1
            life_option=int(input("which option your choose in lifeline"))
            if life_option==lifeline_solution[n]:
                print("congrats")
            else:
                print("sorry your option is not correct")
        elif lifeline=="no":
            print("what your think which is the correct answer in following option")
            option=int(input("choose one option"))
            if option==solution_list[a]:
                print("congratualation,you win the game")
            else:
                print("sorry")
            a=a+1
        count=count+1
        n=n+1
        l=l+1
    else:
        print("sorry you can use only one lifeline")
        # count=count+1
    # n=n+1
    # l=l+1
    # j=j+1
    i=i+1

