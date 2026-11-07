import matplotlib.pyplot as plt
import csv

#-------------Get data from csv then make chart for data-----------------
def MakeChart(_file_path):
    time_data = []
    temperature = []
    pressure = []

    with open(_file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            time_data.append(row["TIMESTAMP"])
            temperature.append(float(row["TEMPERATURE (*C)"]))
            pressure.append(float(row["PRESSURE (bar)"]))

    plt.plot(time_data, temperature, label = "Temperature")
    plt.plot(time_data, pressure, label = "Pressure")

    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("PLC Data Monitor")

    plt.legend()
    plt.grid(True)
    plt.xticks(rotation = 45)

    plt.tight_layout()
    plt.show()