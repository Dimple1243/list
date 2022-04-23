a=["anjali","dimple","anki"]
i=0
max=0
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        b=a[i]
    i+=1
print(b,max)

