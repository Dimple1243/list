
question_list = [
    "How many continents are there",
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"
]

option_list=[
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
a=0
b=1
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<=len(option_list):
        print(option_list[i][j])
        j+=1
    ans=["3 seven", "4 eight","4 delhi","1 Chandigarh","1 Software Engineering","2 Counseling"]
    print("YOU HAVE 50-50 LIFE LINE ")
    life_line=input("IF YOU WANT LIFE LINE ...FOR:- YES ,PRESS'Y' AND FOR:- NO ,PRESS 'N'")
    if life_line=="y":
        if count==0:
            print(ans[i+a])
            print(ans[i+b])
            answer=int(input("ENTER YOUR ANSWER "))
            if solution_list[i]==answer:
                print("BILKUL SHI JAWAB ....")
                count+=1
            else:
                print("YOUR ANSWER IS WRONG ")
        else:
            print("YOUR LIFE IS FINISHED")
            print("NOW YOUR LIFELINE IS OVER SO PLZ MAKE UP YOUR MIND")
            if solution_list[i]==a:
                print("right ")
            else:
                print("YOUR ANSWER IS WRONG")
                break
    elif life_line=="n":
        user=int(input(" CHOOSE THE ANSWER BY  YOURSELF "))
        if solution_list[i]==user:
            print("YOUR ANSWER IS CORRECT,")
        else:
            print("YOUR ANSWER IS WRONG")
    else:
        print("THANKS FOR PLAY THIS GAME")
        break
    a+=1
    b+=1
    i+=1