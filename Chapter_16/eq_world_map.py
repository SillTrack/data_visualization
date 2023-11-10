import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

if __name__ == "__main__":
    # изучение струкутуры данных
    filename = "Chapter_16/data/eq_data_30_day_m1.geojson"
    with open(filename, encoding="utf-8") as f:
        all_eq_data = json.load(f)

    all_eq_dicts = all_eq_data["features"]
    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mags.append(eq_dict["properties"]["mag"])
        lons.append(eq_dict["geometry"]["coordinates"][0])
        lats.append(eq_dict["geometry"]["coordinates"][1])
        hover_texts.append(eq_dict["properties"]["title"])

    # Нанесение данных на карту
    data = [{
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [5*mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }]
    my_layout = Layout(title=all_eq_data["metadata"]["title"])
    fig = {"data": data, "layout": my_layout}
    offline.plot(fig, filename="global_earthquakes.html")

    # readble_file = "Chapter_16/data/readable_eq_data.geojson"
    # with open(readble_file, "w") as f:
    #     json.dump(all_eq_data, f, indent=4)
