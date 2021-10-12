# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("*",end=" ")
#         else:
#             print(end="  ")  
#     print()          

row=0
while row<6:
    col=0
    while col<7:
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="  ")
        else:    
            print(end="   ") 
        col=col+1  
    print() 
    row=row+1
   
       
       


    
 
   
        
  
    
     
              
                   
        
            

