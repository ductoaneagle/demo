import random
import time
from log.csv_def import WriteCsv, ResetCsv
from log.ReadRTC import ReadRtc
from chart.chart_def import MakeChart

#Import Comtypes library
from comtypes.client import GetModule, CreateObject
from comtypes.gen.ActUtlType64Lib import ActUtlType64
GetModule(r"C:\\Program Files (x86)\\MELSOFT\\ACT\\Control\\ActUtlType64.exe")
from plc.plc_def import Read1Reg, Write1Reg, Read_nReg, WordToFloat, WordToString

mx = CreateObject(ActUtlType64)
mx.ActLogicalStationNumber = 1
conn = mx.Open()

#---------------------------------------------------------------------------------
# # Check PLC connection
# if conn == 0:
#     print("PLC connected successfully!")
#     # Read real value as temperature, pressure
#     d = Read_nReg(mx, "D10", 4)
#     # print("D10 = ", d[0])
#     # print("D11 = ", d[1])
#     # print("D12 = ", d[2])
#     # print("D13 = ", d[3])
#     temp = WordToFloat(d[0], d[1])
#     pres = WordToFloat(d[2], d[3])
#     # print("Temperature (*C) = ", round(temp, 2))
#     # print("Pressure (bar) = ", round(pres, 2))

#     # idList = Read_nReg(mx, "D100", 10)
#     # id = WordToString(idList)
#     # print("ID: ", id)
# else:
#     print("PLC connection error!")
#-----------------------------------------------------------------------------------------

csv_path = "D:\\PROJECT\\PYTHON\\demo\\log\\Data.csv"

rows: int = 0
last_sec = -1
ResetCsv(csv_path)

try:
    while(rows < 20):
        #-----Create data random--------
        # Temp = round(random.uniform(20, 40), 2)
        # Press = round(random.uniform(0, 3), 2)

        #------Export data every 3 seconds-------
        dt, sec = ReadRtc()
        if sec % 3 == 0 and sec != last_sec:
            # conn = mx.Open()
            # time.sleep(1)
            if conn == 0:
                print("PLC connected successfully!")
                d = Read_nReg(mx, "D10", 4)
                Temp = WordToFloat(d[0], d[1])
                Press = WordToFloat(d[2], d[3])
            else:
                print("PLC connection error!")

            WriteCsv(csv_path, dt, Temp, Press)
            last_sec = sec
            rows += 1
            print(f"{dt} - Export data successfully! --> {rows}")
        time.sleep(0.1)

    #---------------Stop writing data to csv file-----------------
    print("Data logging stopped !")
    MakeChart(csv_path)
except KeyboardInterrupt:
    print("Data logging stopped !")