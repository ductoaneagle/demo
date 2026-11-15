from comtypes.client import GetModule, CreateObject
import struct

def ReadDevice(mx, StartDevice, count):
    
    prefix = []
    addr = []
    for char in StartDevice:
        if char.isdigit():
            addr.append(char)
        elif char.isalpha():
            prefix.append(char)

    result = []
    if prefix and addr:
        prefix = "".join(prefix)
        addr = "".join(addr)
        start = int(addr)

        for i in range(count):
            register = f"{prefix}{start + i}"
            val, stt = mx.GetDevice(register)
            if stt == 0:
                if val >= 32768:
                    val -= 65536
                result.append(val)
            else:
                result.append(None)
        return result
    else:
        print("Device is invalid!")

def WriteDevice(mx, device, SetVal):
    try:
        mx.SetDevice(device, SetVal)
    except Exception as e:
        print(e)

def WordToFloat(low, high):
    # remove sign bit, obtain 16 low bits
    low = low & 0xFFFF
    high = high & 0xFFFF

    # assembly 2 word 16 to 1 word 32 bit
    value = (high) << 16 | low

    result = struct.unpack('<f', struct.pack('<I', value))[0]
    return result

def WordToString(list):
    result = ""
    for i in list:
        i = int(i) & 0xFFFF
        result += (chr(i & 0xFF) + chr(i >> 8 & 0xFF))
    return result
