import requests
import time

creating_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
task_token = creating_task.json()["token"]
task_time = creating_task.json()["seconds"]

not_ready_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": task_token})
if not_ready_task.json()["status"] != "Job is NOT ready":
    print("Задача должна быть еще не готова")

time.sleep(task_time)

ready_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": task_token})
if ready_task.json()["result"] is None:
    print("Поле result пустое")
if ready_task.json()["status"] != "Job is ready":
    print("Некорректный статус")
