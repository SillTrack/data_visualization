# использовать модуль unittest для проверки что status code в python_repos.py
# после вызова API действительно 200 и придумать другие условия проверки
# например что получено ожидаемое количество элементов и количество репозиториев больше
# определенного порога
import requests
import unittest


class TestRequests(unittest.TestCase):

    def setUp(self) -> None:
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        self.request = requests.get(url=url, headers=headers)

    def test_return_code(self):
        self.assertEqual(self.request.status_code, 200)

    def test_repos(self):
        self.assertGreater(self.request.json()["total_count"], 20_000)


if __name__ == "__main__":

    unittest.main()
    # # Создание вызова API и сохранение ответа.
    # url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    # headers = {"Accept": "application/vnd.github.v3+json"}
    # r = requests.get(url=url, headers=headers)
    # assert (r.status_code)
    # print(f"Status code: {r.status_code}")

    # # Сохранение ответа APi в переменной
    # response_dict = r.json()

    # print(f"Total repositories: {response_dict['total_count']}")
