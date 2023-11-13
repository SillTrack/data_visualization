# измените вызов API в программе python_repos.py так, чтобы на диаграмме отображались
# самые популярные проекты на других языках. Попробуйте JS, Ruby, C, Java, Perl ...


import requests

from plotly.graph_objs import Bar
from plotly import offline

if __name__ == "__main__":
    responses_dict = []
    # Создание вызова API и сохранение ответа.
    languages = ["java", "javascript", "ruby", "C"]
    for language in languages:
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        r = requests.get(url=url, headers=headers)
        print(f"Status code: {r.status_code}")

        # Сохранение ответа APi в переменной
        response_dict = r.json()
        responses_dict.append(response_dict)

    for response_dict in responses_dict:
        print(f"Total repositories: {response_dict['total_count']}")

        # Анализ информации в репозиториях
        repo_dicts = response_dict["items"]
        print(f"Repositories returned: {len(repo_dicts)}")
        repo_links, stars, labels = [], [], []

        print("\nSelected information about each repository:")
        current_language = 0
        for repo_dict in repo_dicts:

            repo_name = repo_dict["name"]
            repo_url = repo_dict["html_url"]
            repo_link = f"<a href:'{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)
            stars.append(repo_dict["stargazers_count"])

            owner = repo_dict["owner"]["login"]
            description = repo_dict["description"]
            label = f"{owner}<br />{description}"
            labels.append(label)

        # Построение визуализации
        data = [{
            "type": "bar",
            "x": repo_links,
            "y": stars,
            "hovertext": labels,
            "marker": {
                "color": "rgb(60, 100, 150)",
                "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
            },
            "opacity": 0.6,
        }
        ]
        my_layout = {
            "title": f"Most-Starred {languages[current_language].capitalize()} Projects on GitHub",
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
        offline.plot(
            fig, filename=f"popular_repos_on_{languages[current_language].capitalize()}.html")
        current_language += 1
