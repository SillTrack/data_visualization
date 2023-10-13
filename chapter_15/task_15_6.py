# 1000 бросков 2 D8

from die import Die
from pprint import pprint
from plotly import offline
from plotly.graph_objs import Bar, Layout


if __name__ == "__main__":
    # Создаем 2 кубика D6  
    die_1 = Die(8)
    die_2 = Die(8)

    # Моделирование серии бросков с сохранением результата в списке.
    results = []
    for roll_num in range(2_550_000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Анализ результатов
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # print(frequencies)
    # Визуализация результатов.
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {"title":"Result", "dtick": 1}
    y_axis_config = {"title":"Frequency of Result"}
    my_layout = Layout(title="Results of rolling two d8 dices 2_550_000 times", title_x=0.5,
                        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({"data":data, "layout":my_layout}, filename="d8_d8.html")

