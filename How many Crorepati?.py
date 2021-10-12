kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
people=0
people_1=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]<=100000:
        count+=1
    elif kitna_paisa_hai[i]>100000 and kitna_paisa_hai[i]<10000000:
        people_1+=1
    else:
        people+=1
    i+=1
print(count,"dilwale")          
print(people_1,"lakhpati")
print(people,"crorepati")  

