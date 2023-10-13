from random import choice, seed
from time import time
import matplotlib.pyplot as plt

class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000) -> None:
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

        seed(time())
        
    def fill_walk(self):
        """Вычисляет все точки блуждания."""

        # Шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:
            
            # определение направления и длины перемещения 
            x_direction = choice([1, -1])
            # x_direction = 1
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            # y_direction = 1
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            

if __name__ == "__main__":
    while True:
        # Построение случайного блуждания
        rw = RandomWalk(50_000)
        rw.fill_walk()

        # Нанесение точек на диаграмму
        plt.style.use("classic")
        fig, ax = plt.subplots(figsize=(13,8), dpi=128)
        point_numbers = range(rw.num_points)

        ax.scatter(rw.x_values, rw.y_values,c=point_numbers,
                    cmap=plt.cm.twilight_shifted, edgecolors="none", s=1)
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
