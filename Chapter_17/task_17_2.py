from operator import itemgetter

import requests
from plotly import offline
from plotly.graph_objs import Bar


if __name__ == "__main__":
    # Создание вызова API и сохранение ответа.
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url=url)
    print(f"Status code: {r.status_code}")

    # Обработка информации о каждой статье
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Создание отдельного вызова API для каждой статьи
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url=url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()
        # Построение словаря для каждой статьи
        try:
            submission_dict = {
                "title": response_dict["title"],
                "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
                "comments": response_dict["descendants"],
            }
            submission_dicts.append(submission_dict)
        except KeyError:
            submission_dict = {
                "title": response_dict["title"],
                "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
                "comments": 0,
            }
            submission_dicts.append(submission_dict)

    submission_dicts = sorted(
        submission_dicts, key=itemgetter("comments"), reverse=True)

    titles, comments, links = [], [], []
    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")
        titles.append(submission_dict["title"])
        comments.append(submission_dict["comments"])
        links.append(submission_dict["hn_link"])

    data = [{
            "type": "bar",
            "x": titles,
            "y": comments,
            "hovertext": links,
            "marker": {
                "color": "rgb(60, 100, 150)",
                "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
            },
            "opacity": 0.6,
            }
            ]
    my_layout = {
        "title": "Most-Starred articles on Hacker News",
        "titlefont": {"size": 28},

        "xaxis": {
            "title": "Repository",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
        "yaxis": {
            "title": "Stars",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
    }

    fig = {"data": data, "layout": my_layout}
    offline.plot(fig, filename="articles.html")
