from die import Die
from pprint import pprint
from plotly import offline
from plotly.graph_objs import Bar, Layout


if __name__ == "__main__":
    # Создаем 2 кубика D6  
    die_1 = Die()
    die_2 = Die(6)

    # Моделирование серии бросков с сохранением результата в списке.
    results = []
    for roll_num in range(250_000):
        result = die_1.roll() * die_2.roll()
        results.append(result)

    # Анализ результатов
    frequencies = []
    max_result = die_1.num_sides * die_2.num_sides
    for value in range(1, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # print(frequencies)
    # Визуализация результатов.
    x_values = list(range(1, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {"title":"Result", "dtick": 1}
    y_axis_config = {"title":"Frequency of Result"}
    my_layout = Layout(title="Results of rolling 2 D6 dices  and multiplying their values 250_000 times", title_x=0.5,
                        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({"data":data, "layout":my_layout}, filename="d6_d6_multiply.html")


