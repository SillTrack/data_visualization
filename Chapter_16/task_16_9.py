import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

if __name__ == "__main__":
    # изучение струкутуры данных
    filename = "Chapter_16/data/world_fires_1_day.csv"
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        coloumns_names = next(reader)

        brightnesses, lons, lats, hover_texts = [], [], [], []
        for row in reader:
            brightnesses.append(float(row[2]))
            lons.append(float(row[1]))
            lats.append(float(row[0]))
            hover_texts.append(row[5])

    # all_eq_dicts = all_eq_data["features"]
    # mags, lons, lats, hover_texts = [], [], [], []
    # for eq_dict in all_eq_dicts:
    #     title = eq_dict["properties"]["title"]
    #     mags.append(eq_dict["properties"]["mag"])
    #     lons.append(eq_dict["geometry"]["coordinates"][0])
    #     lats.append(eq_dict["geometry"]["coordinates"][1])
    #     hover_texts.append(title)

    # Нанесение данных на карту
    data = [{
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [brightness/20 for brightness in brightnesses],
            "color": brightnesses,
            "colorscale": "Hot",
            "reversescale": True,
            "colorbar": {"title": coloumns_names[2].title()},
        },
    }]
    my_layout = Layout(title=coloumns_names[2].title())
    fig = {"data": data, "layout": my_layout}
    offline.plot(fig, filename="global_fires.html")
