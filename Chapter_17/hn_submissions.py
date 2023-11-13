from operator import itemgetter

import requests


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

    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")