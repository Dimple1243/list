magic_square = [[5, 3, 4],[2, 5, 9],[2, 7, 2]]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+(magic_square[i][j])
        j=j+1
    print("row",sum)

    sum1=0
    t=0
    while t<len(magic_square):
        sum1=sum1+(magic_square[t][i])
        t=t+1
    print("col",sum)
    i=i+1
p=0
for i in range(len(magic_square)):
    for c in range(len(magic_square)):
        if i==c:
            p=p+magic_square[i][c]
print("diagonals",p)
s=0
for i in range(len(magic_square)):
    for c in range ( len(magic_square[i])):
        if i+c==len(magic_square[i])-1:
            s=s+magic_square[i][c]
print("diagonals",s)
