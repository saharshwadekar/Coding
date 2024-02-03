
import sys
import timeit

# Ipv4 inputing string
ipAddress = input("Enter IPv4 Address :")

startTime = timeit.default_timer()
# spliting into 4 cells by formating with `.`
arrAddress = ipAddress.split('.')  
try:
    arrAddress = list(map(int,ipAddress.split(".")))
except Exception as e:         
    # Exception occur when one of the ipAddress is not in integer
    print(e)
    print("Inputed Address in not an integer string")
    sys.exit(1)     #system should exit the program i.e.,(exit == 1(error))

if((len(arrAddress) != 4) or (arrAddress[0] == 0)): 
    # for checking the Address should be 4 cell and No leading of Zero's
    print("INVALID ADDRESS - Not of Length 4")
    sys.exit(1)
else:
    print("ADDRESS SCHEME IS VALID and NO LEADING ZERO'S FOUND")
    
if(arrAddress[0] == 0):
    print("INVALID ")
    
# Checking the all address to be Valid in the range(0,255)    
for x in arrAddress:  
    if (0 > x or 255 < x):
        print("INVALID RANGE ")
        sys.exit(1)
else:
    print("Valid IPv4 Address Found")

#for finding the Class of IPv4 Address
firstCell = arrAddress[0]     
flag = "A"
if(ipAddress == "127.0.0.1"):
    flag = "A {LoopBack Address}"
if(firstCell > 127): 
    flag = "B"
    if(firstCell > 191):
        flag = "C"
        if(firstCell > 223):
            flag = "D {Multicast address}"
            if(firstCell > 239):
                flag = "E"
                
print("IPv4 " + ipAddress + " Belongs To Class " + flag)


print(timeit.default_timer() - startTime)
        

