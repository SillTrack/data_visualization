import csv
from datetime import datetime

from matplotlib import pyplot as plt

if __name__ == "__main__":
    # print(plt.style.available)
    filename = "data/san_francisco_2022_full.csv"
    with open(filename, "r") as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # for index, coloumn_header in enumerate(header_row):
        #     print(index, coloumn_header)

        # чтение дат и  максимальных температур
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            high = int(row[2])
            low = int(row[3])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Форматирование диаграммы
    plt.title(
        "Daily highhest and lowest temperatures - 2021\nSan-Francisco", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
