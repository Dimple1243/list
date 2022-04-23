var=[[2,4,36],5,[9,3,6],2,[4,5,89]]
# Output=[[2,4,36,5],[9,3,6,2],[4,5,89]]
i=0
b=[]
c=[]
while i<len(var):
    if type(var[i])==list:
        b.append(var[i])
    else:
        c.append([var[i]])
    i+=1
for i in range(len(c)):
    b[i].extend(c[i])
print(b)
# i=0
# b=[]
# c=[]
# while i<len(var):
#     if type(var[i])==list:
#         b.append(var[i])
#     else:
#         c.append([var[i]])

#     i+=1
# for i in range(len(c)):
#     b[i].extend(c[i])
# print(b)