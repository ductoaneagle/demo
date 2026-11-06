import csv
import os

#------------Write data to csv file------------------------
def WriteCsv(_file_path, _dt, _Temp, _Press):
    file_exists = os.path.exists(_file_path) and os.path.getsize(_file_path) > 0
    with open(_file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Header
        if not file_exists:
            writer.writerow(["TIMESTAMP", "TEMPERATURE (*C)", "PRESSURE (bar)"])
        # Data
        writer.writerow([_dt, _Temp, _Press])

#------------Delete data from csv file (except header)--------------
def ResetCsv(_file_path):
    with open(_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["TIMESTAMP", "TEMPERATURE (*C)", "PRESSURE (bar)"])
    print("CSV data reset successfully !")