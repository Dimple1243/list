elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count_even=0
count1_odd=0
sum1_even=0
sum_odd=0
while i<len(elements):
    if elements[i]%2==0:
        sum1_even=sum1_even+elements[i]

        count_even+=1
    else:
        sum_odd=sum_odd+elements[i]
        count1_odd+=1
    i=i+1
print(count_even,":-even:")
print(count1_odd,":-odd:")
print("sum of even numbers",sum1_even)
print("sum of odd numbers",sum_odd)
print("average of even numbers",sum1_even//count_even)
print("average of odd numbers",sum_odd//count1_odd)




  
 