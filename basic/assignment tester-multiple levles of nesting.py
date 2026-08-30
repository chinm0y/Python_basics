score = int(input("Enter the score: "))
attendence = int(input("enter the attendence: "))


#self made boolean function ....... fvking awsome for beginer like me 
#=========================================

x = (input("did they submitted: "))
if x == "yes":
    submitted = True
else:
    submitted = False
    
#===================================
    
    
if score >=60:
    if attendence >=80:
        if submitted:
            print("pass with good standing")
        else:
            print("pass but missing assignment")
    else:
        print("pass but low attendance")
else:
    print("fail")