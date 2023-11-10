import csv
from datetime import datetime
import matplotlib.pyplot as plt 

if __name__ == "__main__":
    filename = "data/death_valley_2021_simple.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[3])
                low = int(row[4])
            except ValueError:
                print(f"Missing data for {current_date}")
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Форматирование диаграммы
    plt.title("Daily highhest and lowest temperatures - 2021\nDeath Valley, CA", fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
        