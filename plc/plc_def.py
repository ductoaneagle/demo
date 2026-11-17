import struct

# Read 1 register
def Read1Reg(mx, register):
    val, stt = mx.GetDevice(register)
    if stt == 0:
        if val >= 32768:
            val -= 65536
    return val
 # Write 1 register
def Write1Reg(mx, register, value):
    try:
        mx.SetDevice(register, value)
    except Exception as e:
        print(e)

# Read n register from plc
# Register type from PLC Mitsubishi: D10, SD100, W, ....
def Read_nReg(mx, StartDevice, n):
    prefix = []     # only text
    addr = []       # only numeric
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

        for i in range(n):
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
        print("StartDevice is invalid!")

# Convert word to float
# low: value of low register (16 bits)
# high: value of high register (16 bits)
def WordToFloat(low, high):
    # Remove sign bit, obtain 16 low bits
    low = low & 0xFFFF
    high = high & 0xFFFF

    # Assembly 2 word 16 bits to 1 word 32 bits
    ass = high << 16 | low

    result = struct.unpack('<f', struct.pack('<I', ass))[0]
    return result

# Convert Word to String
def WordToString(list):
    result = ""
    for i in list:
        i = int(i) & 0xFFFF
        result += (chr(i & 0xFF) + chr(i >> 8 & 0xFF))
    return result