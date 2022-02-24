import requests


class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header = response.headers
        print(header)

        assert "x-secret-homework-header" in header.keys(), "Поля 'x-secret-homework-header' нет в headers"
        assert "Some secret value" in header.values(), "Поле 'x-secret-homework-header' != 'Some secret value'"
