# Сделать поиск Tmax и Tmin определяемым из заголовка,
# а также использовать название станции для создания заголовка
# графика при его создании. Сделать так, чтобы программа работа и
# с файлом death_valley_2021_full.csv и с sitka_weather_2021_full.csv

import csv
from datetime import datetime

from matplotlib import pyplot as plt

if __name__ == "__main__":
    # print(plt.style.available)
    filename = "Chapter_16/data/death_valley_2021_full.csv"
    with open(filename, "r") as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for index, coloumn_header in enumerate(header_row):
            if coloumn_header == "NAME":
                name_index = index
            elif coloumn_header == "TMAX":
                tmax_index = index
            elif coloumn_header == "TMIN":
                tmin_index = index

        # чтение дат и  максимальных температур
        dates, highs, lows = [], [], []
        name = None
        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[tmax_index])
                low = int(row[tmin_index])
            except ValueError:
                print("Missing data for ", current_date)
            if name == None:
                name = row[name_index]
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Форматирование диаграммы
    plt.title(name, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
