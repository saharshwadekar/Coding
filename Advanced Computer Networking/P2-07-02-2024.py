
import sys


def intergerToBinary(arrAddress):
    binAddress = []
    for octet in arrAddress:
        n = bin(octet)[2:]
        n = n.zfill(8)
        binAddress.append(n);
    return binAddress

def maskingValue(ipClass):
    match ipClass:
        case 'A':
            return intergerToBinary([255,0,0,0])
        case 'B':
            return intergerToBinary([255,255,0,0])
        case 'C':
            return intergerToBinary([255,255,255,0])
        case 'D':
            return intergerToBinary([255,255,255,255])
        case 'E':
            return intergerToBinary([255,255,255,255])

def checkClassNetHostId(binAddress):
    firstOctet = binAddress[0]
    if '0' == firstOctet[0]:
        return "A", binAddress[:1] , binAddress[1:] , maskingValue("A")
    elif '10' == firstOctet[0:2]:
        return "B", binAddress[:2] , binAddress[2:], maskingValue("B")
    elif '110' == firstOctet[0:3]:
        return "C", binAddress[:3] , binAddress[3:], maskingValue("C")
    elif '1110' == firstOctet[0:4]:
        return "D", binAddress , "", maskingValue("D")
    else:
        return "E", binAddress , "", maskingValue("E")


if __name__ == '__main__':
    # Ipv4 inputing string
    ipAddress = input("Enter IPv4 Address :")

    # spliting into 4 cells by formating with `.`
    arrAddress = ipAddress.split('.')
    
    try:
        arrAddress = list(map(int,ipAddress.split(".")))
        print("Inputed Address in an valid integer string")
    except Exception as e:
        # Exception occur when one of the ipAddress is not in integer
        print(e)
        print("Inputed Address in not an integer string")
        sys.exit(1)     #system should exit the program i.e.,(exit == 1(error))

    binAddress = intergerToBinary(arrAddress)
    ipClass, netId , hostId ,maskValue = checkClassNetHostId(binAddress)
    
    print(binAddress,ipClass, netId, hostId, maskValue)