def bpmonitor():
  l=800
    while l > 0:
        bp=int(input("BP: "))
        l=l+10
        if bp >=140 :
            print("\t\t\t***ALERT***")
            print("\t\t\tHigh BP")
            break
        elif bp <= 60:
            print("\t\t\t***ALERT***")
            print("\t\t\tLow BP")

def diabetic():
  o=100
    while o > 0:
        db=int(input("Sugar level: "))
        o=o+10
        if db in range(140,199):
            print("\t\t\t***ALERT***")
            print("\t\t\tPrediabetic Stage")
            
        elif db in range(53,70):
            print("\t\t\t***ALERT***")
            print("\t\t\tLow Blood Sugar Level")
            break
        elif db >= 200:
            print("\t\t\t***ALERT***")
            print("\t\t\tHigh Blood Sugar Level")
            break
        else:
            print("\t\t\tNORMAL")
    
         
dict1={'Babu':8851,'Yuvan':136391,'Vigneshwar':10319}
print("\t\t\tMED PORTAL")
print("")
print("Motosid Pharma Industries Pvt. Ltd")
cse=int(input("Press (1) for Administration Login: "))
if cse == 1:
 name=str(input("Your name=\t"))
 ids=int(input("Your ID number=\t"))
    if (name,ids) in dict1.items():
        print("Login Successful")
        print("")
        print("Welcome %s"%name)
        print("\t\t\tHealth monitor System")
        print("Press (1) for BP Monitor")
        print("Press (2) for Blood Sugar Monitor")
        was=int(input("1/2 : "))
        if was == 1:
             print("\t\t\tBP MONITOR")
            bpmonitor()
        elif was == 2:
            print("\t\t\tBLOOD SUGAR MONITOR")
            diabetic()
        else:
            print("Wrong Choice")
        
    else:
        print("-------Invalid Login--------")
        
else:

    print("Thank You")        
        