while True:
    n1 = int(input("ENTER YOUR FIRST NUMBER:"))
    n2=int(input("ENTER YOUR SECOUND NUMBER:"))
    o=input("SELECT NUMBERS : 1.ADD 2.MUL 3.SUB 4.DIV 5.MOD 6.POWER:  ")
    if (o=="1"):
        print("output = " ,(n1+n2))
    elif(o=="2"):
        print("output = " ,(n1*n2))
    elif(o=="3"):
        print("output = ",( n1-n2))
    elif(o=="4"):
        print("output = ",( n1/n2))
    elif(o=="5"):
        print("output = " ,(n1%n2))
    elif(o=="6"):
        print("output = " ,(n1**n2))
    check=int(input("Wanna continue? if yes press 1,if not press 0 "))
    if(check==0):
        break
        
            
    

