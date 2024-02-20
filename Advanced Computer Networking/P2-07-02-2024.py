'''
    @student     : Saharsh Sanjay Wadekar
    @Sec/Rollno. : B - 48
'''
import sys

def calculateMaskValue(cusMask):
    octet = 0;
    if (cusMask > 32 or cusMask < 0):
        return "Invalid Custome Mask Given!"
    if (cusMask >= 24):
        for x in range((cusMask - 24)):
            octet += pow(2,7-x)
        return f"255.255.255.{octet}"
    elif (cusMask >= 16):
        for x in range((cusMask - 16)):
            octet += pow(2,7-x)
        return f"255.255.{octet}.0"
    elif (cusMask >= 8):
        for x in range((cusMask - 8)):
            octet += pow(2,7-x)
        return f"255.{octet}.0.0"

def identifyNetAddNetHostId(ipAddress,ipClass):
    ipAddress = list(map(str,ipAddress))
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
    ipAddress = list(map(str,ipAddress))
    match ipClass:
        case 'A':
            return ipAddress[0] + ".0.0.0" , ipAddress[0] + ".255.255.255" , (pow(2,24) - 2)
        case 'B':
            return '.'.join(ipAddress[:2]) + ".0.0", '.'.join(ipAddress[:2]) + ".255.255", (pow(2,16) - 2)
        case 'C':
            return '.'.join(ipAddress[:3]) + ".0",  '.'.join(ipAddress[:3]) + ".255", (pow(2,8) - 2)
    return "", "", 0

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

def binToint(x):
    return eval('0b'+f'{x}')

def intergerToBinary(arrAddress):
    binAddress = []
    for octet in arrAddress:
        n = bin(octet)[2:]
        n = n.zfill(8)
        binAddress.append(n);
    return binAddress

if __name__ == '__main__':
    # Ipv4 inputing string
    choice = int(input("\nInputed IP Address will be in\n\t1.Interger\n\t2.Binary\n\nEnter Choice : "))
    ipAddress = input("Enter IPv4 Address :")

    try:
        ipclist = list(map(str,ipAddress.split('/')))
        ipAddress = ipclist[0]
        cusMask = int(ipclist[1])
        ipAddress = list(map(int,ipAddress.split(".")))
        if choice == 2:
            ipAddress = list(map(binToint,ipAddress))
        print("Inputed Address in an valid integer string")
    except Exception as e:
        # Exception occur when one of the ipAddress is not in integer
        print(e)
        print("Inputed Address in not an integer string")
        sys.exit(1)     #system should exit the program i.e.,(exit == 1(error))

    binAddress = intergerToBinary(ipAddress)
    printBinAddress = ".".join(binAddress)
    printintAddress = list(map(str,ipAddress))
    printintAddress = ".".join(printintAddress)

    ipClass = identifyClass(binAddress)

    netAdd, netId, hostId = identifyNetAddNetHostId(ipAddress,ipClass)

    fIpAdd , lIpAdd , tIpAdd = findFLTIpAddress(ipAddress,ipClass)

    customeMask = calculateMaskValue(cusMask)
    bincus = list(map(int,str(customeMask).split(".")))
    bincus = ".".join(intergerToBinary(bincus))
    print(f'''
        Ip (Integer) :{printintAddress}
        Ip (Binary)  :{printBinAddress}

        Class of Ip Address :{ipClass}

        Your Network Address : {netAdd}
        Your Network Id : {netId}
        Your Host Id : {hostId}

        First Ip Address : {fIpAdd}
        Last Ip Address : {lIpAdd}
        Total Ip Address : {tIpAdd}

        Custom Masking Value : {customeMask}
                               {bincus}
        '''
          )