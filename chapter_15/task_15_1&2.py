"""Кубы, нанесите на диаграппу первые 5000 кубов. Примените цветовую карту"""

import matplotlib.pyplot as plt

if __name__ == "__main__":
    style = "ggplot"

    x_values = list(range(1, 5001))
    y_values = [x**3 for x in x_values]

    plt.style.use(style)
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno, s=10)

    # Назначение заголовка и меток осей
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Square of Value", fontsize=14)
    ax.set_ylabel("Value", fontsize=14)

    ax.tick_params(axis="both", labelsize=14)

    ax.axis ([0, 5500, 0, 130000000000])

    plt.savefig("img/cubes_plot.png")

