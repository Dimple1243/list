l1=[4,5,6],[5,6,8],[9,10,11]
i=0
sum=0
while i<len(l1):
    if i==0:
        for j in l1[i]:
            sum+=j
    elif i!=0:
        s=len(l1[i])
        sum+=(l1[i][s-1])
    i+=1
print(sum)
