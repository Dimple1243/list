a=[[2,8,7],[7,1,3],[1,9,5]]
list=[]
for i in range(len(a)):
    sum=0
    for j in a[i]:
        print(j) 
        sum+=j
    list.append(sum)
print(list) 
max=0
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
print(max) 