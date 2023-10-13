import matplotlib.pyplot as plt
import numpy as np
from random_walk import RandomWalk
import matplotlib.colors as mcolors


if __name__ == "__main__":
    while True:
        # Построение случайного блуждания
        rw = RandomWalk(5_000)
        rw.fill_walk()

        # Нанесение точек на диаграмму
        plt.style.use("classic")
        fig, ax = plt.subplots(figsize=(13,8), dpi=128)
        point_numbers = range(rw.num_points)

        ax.plot(rw.x_values, rw.y_values,c="darkturquoise", linewidth = 1)
        ax.scatter(0,0, c="red", edgecolors="none", s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c="blue", edgecolors="none", s=100)

        ax.set_title("Random Walk", fontsize=24)
        # ax.set_xlabel("Random X", fontsize=14)
        # ax.set_ylabel("Random y", fontsize=14)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        ax.tick_params(axis="both", labelsize=14)


        fig.savefig("img/rm_visual")
        plt.show()
        keep_running = input("Make another walk? (y/n):\n")
        if keep_running != "y":
            break


