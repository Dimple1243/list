print("WELCOME TO UBER APPLICATION ")
vechiciles=input("ENTER WHICH VECHICILES YOU WANT")
if vechiciles=="CAB" or "BIKE" or "AUTO":
    print("NEXT")
else:
    print("OTHER VECHICILES IS NOT THERE") 

charges=input("different uber different charges for 1k/m")
if charges=="CAB" or "BIKE" or "AUTO":
    print("for cab=250,Bike=75,Auto=150")
else:
    print("it is avilabe for only 1k/m")
pickup=input("ENTER YOUR PICKUP LOCATION")  
print("NEXT>")  
dropup=input("ENTER YOUR DROPUP LOCATION")   
print("NEXT>") 
payment=input("ENTER YOUR PAYMENT TYPE")
if payment=="CASH" or "BY CARD":
    print("NEXT>")
else:("card only master card")
Driver_Details=input("THEIR ARE SOME DRIVER DETAILS")

print("FOR CAB NAME=Mr.Rahul Rajput"," /n","Phone No=987654376"
"FOR BIKE- NAME=mr.prakash singh","n/","Phone No=3456765454"
"FOR AUTO NAME=Mr.salman khan"," n/","Phone No=876547654")

Riders_Details=input("THEIR ARE SOME VECHICILES DETAILS")
print("CAB IS IN RED COLOUR","N/","PLAT NO.3466,THEIR IS ONLY 4 SEAT",
"BIKE- IT IS IN BLACK COLOUR","N/","PLAT NO-DL2345","AUTO-IT IS IN BLACK AND YELLOW COLOUR","PLAT NO-MB2345")
print("your uber is confirm  for riding")