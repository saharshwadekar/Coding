'''
    @student     : Saharsh Sanjay Wadekar
    @Sec/Rollno. : B - 48
'''
import sys
import P1 as p

def classlessFLTAddress(ipAddress,subNMask,cusMask):
    firstIpAddress = []
    lastIpAddress = []
    for i in range(4):
        firstIpAddress.append(str(ipAddress[i] & subNMask[i] & 0xFF ))
        lastIpAddress.append(str(ipAddress[i] | (~subNMask[i] & 0xFF)))
    return ".".join(firstIpAddress), ".".join(lastIpAddress) , pow(2,32-cusMask)

def BinaryOctet(intOctet):
    return bin(intOctet)[2:].zfill(8)

def calcOctet(ran):
    octet = 0
    for x in range(ran):
        octet += pow(2,7-x)
    return octet

def calcMaskValue(cusMask):
    if (cusMask > 32 or cusMask < 0):
        return "Invalid Custome Mask Given!"
    if (cusMask >= 24):
        return f"255.255.255.{calcOctet(cusMask - 24)}"
    elif (cusMask >= 16):
        return f"255.255.{calcOctet(cusMask - 16)}.0"
    elif (cusMask >= 8):
        return f"255.{calcOctet(cusMask - 8)}.0.0"
    elif (cusMask >= 0):
        return f"{calcOctet(cusMask)}.0.0.0"

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
            return '.'.join(ipAddress), '.'.join(ipAddress), 'NULL'
        case 'E':
            return '.'.join(ipAddress), '.'.join(ipAddress), 'NULL'
    return "NULL", "NULL", "NULL"

def identifyClass(firstOctet):
    if "0" == firstOctet[0]:
        return "A"
    elif "10" == firstOctet[0:2]:
        return "B"
    elif "110" == firstOctet[0:3]:
        return "C"
    elif "1110" == firstOctet[0:4]:
        return "D"
    elif "1111" == firstOctet[0:4]:
        return "E"
    return "INVALID"

if __name__ == '__main__':
    ip = input("Enter IP Address : ")

    try:
        ip, cusMask = ip.split("/")
        cusMask = int(cusMask)
    except Exception as e:
        print(e ,"  <--- Failed")
        sys.exit(1)

    p.checkInProcess(ip)

    subMask = calcMaskValue(cusMask)

    ipArr = list(map(int,ip.split('.')))
    subMaskArr = list(map(int,str(subMask).split('.')))

    ipClass = identifyClass(BinaryOctet(ipArr[0]))
    netAdd , netId , hostId = identifyNetAddNetHostId(ipArr,ipClass)
    firstIP, lastIP, blockIP = classlessFLTAddress(ipArr, subMaskArr, cusMask)

    print(f'''
        Ip : {ip}/{cusMask}

        Class of Ip : {ipClass}

        Your Network Address : {netAdd}
        Your Network Id      : {netId}
        Your Host Id         : {hostId}

        First Ip Address : {firstIP}/{cusMask}
        Last Ip Address  : {lastIP}/{cusMask}
        Total Ip Address : {blockIP}

        Subnet Mask : {subMask}
        ''')