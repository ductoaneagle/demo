import random
import time
from log.csv_def import WriteCsv, ResetCsv
from log.ReadRTC import ReadRtc
from chart.chart_def import MakeChart

csv_path = "D:\\PROJECT\\Python\\Project1_DataLog\\log\\Data.csv"

rows: int = 0
last_sec = -1
ResetCsv(csv_path)

try:
    while(rows < 20):
        #-----Create data random--------
        Temp = round(random.uniform(20, 40), 2)
        Press = round(random.uniform(0, 3), 2)

        #------Export data every 3 seconds-------
        dt, sec = ReadRtc()
        if sec % 3 == 0 and sec != last_sec:
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