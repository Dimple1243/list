l1=[2,4,3]
l2=[5,6,7]
s=""
d=""
i=1
while i<len(l1)+1:
    s+=str(l1[-i])
    d+=str(l2[-i])
    i+=1
print(d)
print(s)
b=int(s)+int(d)
e=""
c=str(b) 
print(c)
for i in range(1,len(c)+1):
    e+=c[-i]
print(e)