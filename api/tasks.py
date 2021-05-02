from celery import shared_task
import requests

CURRENCY_API = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=3c43fac79a2cc3e14edecaf8911f8e2c'

# Lets us create tasks without having concrete app
@shared_task()
def get_currency(seconds):
    
    result = 0
    for i in range(seconds):
        # time.sleep(4)
        result += i

        r = requests.get(CURRENCY_API)
        print(r.json())