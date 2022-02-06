import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
url_quantity = len(response.history)
final_url = response.history[-1]

print(url_quantity)
print(final_url.url)