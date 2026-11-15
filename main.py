import random
import time
from log.csv_def import WriteCsv, ResetCsv
from log.ReadRTC import ReadRtc
from chart.chart_def import MakeChart

# Import comtypes library----------------------------------------
from comtypes.client import GetModule, CreateObject
from comtypes.gen.ActUtlType64Lib import ActUtlType64
from plc.plc_def import ReadDevice, WriteDevice, WordToFloat, WordToString
GetModule(r"C:\Program Files (x86)\MELSOFT\ACT\Control\ActUtlType64.exe")

mx = CreateObject(ActUtlType64)
mx.ActLogicalStationNumber = 1
conn = mx.Open()

if conn == 0:
    print("PLC connected successfully!")

    tempList = ReadDevice(mx, "D10", 2)
    temp = round(WordToFloat(tempList[0], tempList[1]), 2)

    pressList = ReadDevice(mx, "D12", 2)
    press = round(WordToFloat(pressList[0], pressList[1]), 2)

    idList = ReadDevice(mx, "D100", 1)
    id = WordToString(idList)

    print(temp)
    print(press)
    print(id)
    # WriteDevice(mx, "D11", 1994)
else:
    print("PLC connection error!")

csv_path = "D:\\PROJECT\\Python\\Project1_DataLog\\log\\Data.csv"

rows: int = 0
last_sec = -1
# ResetCsv(csv_path)

# try:
#     while(rows < 20):
#         #-----Create data random--------
#         Temp = round(random.uniform(20, 40), 2)
#         Press = round(random.uniform(0, 3), 2)

#         #------Export data every 3 seconds-------
#         dt, sec = ReadRtc()
#         if sec % 3 == 0 and sec != last_sec:
#             WriteCsv(csv_path, dt, Temp, Press)
#             last_sec = sec
#             rows += 1
#             print(f"{dt} - Export data successfully! --> {rows}")
#         time.sleep(0.1)

#     #---------------Stop writing data to csv file-----------------
#     print("Data logging stopped !")
#     MakeChart(csv_path)
# except KeyboardInterrupt:
#     print("Data logging stopped !")