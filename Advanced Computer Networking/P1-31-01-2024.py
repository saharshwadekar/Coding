import sys

# Ipv4 inputing string
ipAddress = input("Enter IPv4 Address :")

print('''
      1. Check Interger or Not
      2. Check Octets and Leading Zero's
      3. Valid Range
      4. Classify Class
      5. exit the program
      ''')

arrAddress = []

while(True):
    choice = int(input("Enter Your Choice : "))
    match choice:
        case 1:
            try:
                arrAddress = list(map(int,ipAddress.split(".")))
                print("Inputed Address in an valid integer string")
            except Exception as e:
                # Exception occur when one of the ipAddress is not in integer
                print(e)
                print("Inputed Address in not an integer string")
                sys.exit(1)     #system should exit the program i.e.,(exit == 1(error))

        case 2:
            if((len(arrAddress) != 4) or (arrAddress[0] == 0)):
                # for checking the Address should be 4 cell and No leading of Zero's
                print("INVALID ADDRESS - Not of Length 4")
                sys.exit(1)
            else:
                print("ADDRESS SCHEME IS VALID and NO LEADING ZERO'S FOUND")

        case 3:
            # Checking the all address to be Valid in the range(0,255)
            for x in arrAddress:
                if (0 > x or 255 < x):
                    print("INVALID RANGE ")
                    sys.exit(1)
            else:
                print("Valid Range of IPv4 Address Found")

        case 4:
            #for finding the Class of IPv4 Address
            firstCell = arrAddress[0]
            flag = "A"
            if(ipAddress == "127.0.0.1"):
                flag += " {LoopBack Address}"
            if(ipAddress == "10.0.0.1"):
                flag += " {Private Address}"
            if(firstCell > 127):
                flag = "B"
                if(firstCell == 172 and (16 <= arrAddress[1] <= 31)):
                    flag += " {Private Address}"
                if(firstCell > 191):
                    flag = "C"
                    if(firstCell == 192 and arrAddress[1]==168):
                        flag += " {Private Address}"
                    if(firstCell == 169 and arrAddress[1]==254):
                        flag += " {Link Local Address}"
                    if(firstCell > 223):
                        flag = "D {Multicast Address}"
                        if(firstCell > 239):
                            flag = "E {Reseach Purpose}"

            print("IPv4 " + ipAddress + " Belongs To Class " + flag)

        case 5:
            sys.exit(1)