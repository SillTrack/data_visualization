import matplotlib.pyplot as plt
import csv
from datetime import datetime

if __name__ == "__main__":
    filename = "data/sitka_weather_2021_full.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        coloumns_names = next(reader)

        dates, prcps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            prcp = float(row[5])
            dates.append(current_date)
            prcps.append(prcp)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.bar(dates, prcps, width=1, color="green",
           edgecolor="white", linewidth=0.5)
    fig.autofmt_xdate()
    plt.show()
