import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(cookie)

        assert "HomeWork" in cookie.keys(), "Поля 'HomeWork' нет в cookie"
        assert "hw_value" in cookie.values(), "Поле 'HomeWork' != 'hw_value'"
