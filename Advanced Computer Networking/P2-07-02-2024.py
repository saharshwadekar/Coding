import sys

def intergerToBinary(arrAddress):
    binAddress = []
    for octet in arrAddress:
        n = bin(octet)[2:]
        n = n.zfill(8)
        binAddress.append(n);
    return binAddress

def identifyClass(binAddress):
    firstOctet = binAddress[0]
    if '0' == firstOctet[0]:
        return "A"
    elif '10' == firstOctet[0:2]:
        return "B"
    elif '110' == firstOctet[0:3]:
        return "C"
    elif '1110' == firstOctet[0:4]:
        return "D"
    else:
        return "E"

def identifyNetAddNetHostId(ipAddress,ipClass):
    match ipClass:
        case 'A':
            return ipAddress[0] + ".0.0.0" , '.'.join(ipAddress[:1]), '.'.join(ipAddress[1:])
        case 'B':
            return '.'.join(ipAddress[:2]) + ".0.0", '.'.join(ipAddress[:2]), '.'.join(ipAddress[2:])
        case 'C':
            return '.'.join(ipAddress[:3]) + ".0", '.'.join(ipAddress[:3]), '.'.join(ipAddress[3:])
        case 'D':
            return '.'.join(ipAddress), '.'.join(ipAddress), '.'.join(ipAddress)
        case 'E':
            return '.'.join(ipAddress), '.'.join(ipAddress), '.'.join(ipAddress)
    return "", "", ""


def findFLTIpAddress(ipAddress,ipClass):
    match ipClass:
        case 'A':
            return ipAddress[0] + ".0.0.0" , '.'.join(ipAddress[0]) + ".255.255.255" , 255*255*255
        case 'B':
            return '.'.join(ipAddress[:2]) + ".0.0", '.'.join(ipAddress[:2]) + ".255.255", 255*255
        case 'C':
            return '.'.join(ipAddress[:3]) + ".0",  '.'.join(ipAddress[:3]) + ".255", 255
    return "", "", 0

def calculateMaskValue(cusMask):
        i = 0
        octet = 0;
        if (cusMask >= 24):
            i = (cusMask - 24)
            for x in range(i):
                octet += pow(2,7-x)
            return f"255.255.255.{octet}"
        elif (cusMask >= 16):
            i = (cusMask - 16)
            for x in range(i):
                octet += pow(2,7-x)
            return f"255.255.{octet}.0"
        elif (cusMask >= 8):
            i = (cusMask - 8)
            for x in range(i):
                octet += pow(2,7-x)
            return f"255.{octet}.0.0"


if __name__ == '__main__':
    # Ipv4 inputing string
    ipAddress = input("Enter IPv4 Address :")
    arrAddres = []
    try:
        arrAddress = list(map(int,ipAddress.split(".")))
        print("Inputed Address in an valid integer string")
    except Exception as e:
        # Exception occur when one of the ipAddress is not in integer
        print(e)
        print("Inputed Address in not an integer string")
        sys.exit(1)     #system should exit the program i.e.,(exit == 1(error))

    print(
        '''
        1. Convert To Binary Notation
        2. Identify Class of Ip
        3. Identify Network Address, Network Id, Host Id
        4. Find First Address , Last Address , Total Address
        5. Calculate Custome Subnet Mask
        6. Exit
        '''
    )
    binAddress = []
    ipClass = "";
    ipAddress = list(map(str,ipAddress.split(".")))
    while(True):
        choice = int(input("Enter Your Choice : "))
        match choice:
            case 1:
                binAddress = intergerToBinary(arrAddress)
                printBinAddress = ".".join(binAddress)
                print(printBinAddress)

            case 2:
                ipClass = identifyClass(binAddress)
                print("Class of Given Ip Address is :" , ipClass)

            case 3:
                netAdd, netId, hostId = identifyNetAddNetHostId(ipAddress,ipClass)
                print(
                    f'''
                    Your Network Address : {netAdd}
                    Your Network Id : {netId}
                    Your Host Id : {hostId}
                    ''')

            case 4:
                fIpAdd , lIpAdd , tIpAdd = findFLTIpAddress(ipAddress,ipClass)
                print(
                    f'''
                    First Ip Address : {fIpAdd}
                    Last Ip Address : {lIpAdd}
                    Total Ip Address : {tIpAdd}
                    ''')

            case 5:
                cusMask = int(input(f"Enter custome Subnet Mask : {'.'.join(ipAddress)}/"))
                customeMask = calculateMaskValue(cusMask)
                print(
                    f'''
                    Custom Masking Value : {customeMask}
                    '''
                      )

            case 6:
                sys.exit(0)