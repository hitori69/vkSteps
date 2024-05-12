import requests
import time
from datetime import datetime, timedelta
from my_token import ACCESS_TOKEN


def setSteps(sess, date, steps, distance):
    params = {
        'date': date,
        'steps': steps,
        'distance': distance,
    }
    return sess.get('https://api.vk.com/method/vkRun.setSteps', params=params).json()


with requests.Session() as sess:
    sess.headers.update({'Authorization': 'Bearer ' + ACCESS_TOKEN})
    sess.params = {'v': 5.131}

    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=31)

    current_date = start_date
    while current_date <= end_date:
        response = setSteps(sess, current_date.strftime('%Y-%m-%d'), 80000, 50000)
        print(current_date.strftime('%Y-%m-%d'), response)
        if 'response' in response:
            current_date += timedelta(days=1)
        time.sleep(0.05)
