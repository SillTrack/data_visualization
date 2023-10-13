from random import choice, seed
from time import time

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
            x_step = self.get_step()

            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self):
        step_direction = choice([1, -1])
        step_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
        step = step_direction * step_distance
        return step

