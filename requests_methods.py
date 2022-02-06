import requests

response_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("GET запрос без параметра method:", response_1.status_code, response_1.text)

response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print("http-запрос не из списка:", response_2.status_code, response_2.text)

response_3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print("Запрос с правильным значением method:", response_3.status_code, response_3.text)

methods = ["GET", "POST", "PUT", "DELETE"]

for method_type in methods:
    responseGet = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": method_type})
    print(f"GET запрос с параметром {method_type} возвращает {responseGet.status_code, responseGet.text}")
    if responseGet.text == '{"success":"!"}' and method_type != "GET":
        print("Успешный ответ, но тип запроса не совпадает со значением параметра")
    elif responseGet.text != '{"success":"!"}' and method_type == {"method": "GET"}:
        print("Неуспешный ответ, хотя тип запроса == значению параметра")

for method_type in methods:
    responsePost = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method_type})
    print(f"POST запрос с параметром {method_type} возвращает {responsePost.status_code, responsePost.text}")
    if responsePost.text == '{"success":"!"}' and method_type != "POST":
        print("Успешный ответ, но тип запроса не совпадает со значением параметра")
    elif responsePost.text != '{"success":"!"}' and method_type == {"method": "POST"}:
        print("Неуспешный ответ, хотя тип запроса == значению параметра")

for method_type in methods:
    responsePut = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method_type})
    print(f"PUT запрос с параметром {method_type} возвращает {responsePut.status_code, responsePut.text}")
    if responsePut.text == '{"success":"!"}' and method_type != "PUT":
        print("Успешный ответ, но тип запроса не совпадает со значением параметра")
    elif responsePut.text != '{"success":"!"}' and method_type == {"method": "PUT"}:
        print("Неуспешный ответ, хотя тип запроса == значению параметра")

for method_type in methods:
    responseDelete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method_type})
    print(f"DELETE запрос с параметром {method_type} возвращает {responseDelete.status_code, responseDelete.text}")
    if responseDelete.text == '{"success":"!"}' and method_type != "DELETE":
        print("Успешный ответ, но тип запроса не совпадает со значением параметра")
    elif responseDelete.text != '{"success":"!"}' and method_type == {"method": "DELETE"}:
        print("Неуспешный ответ, хотя тип запроса == значению параметра")
