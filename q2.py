# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n<=0:
#             return False 
#         while n>1:
#             if n%2==1:
#                 return False
#             n=n//2
#         return True    
        



n=int(input("enter the num:-"))
if n<=0:
    print(False)
while n>0:
    if n%2==1:
        print(False)
    n=n//2
print(True)