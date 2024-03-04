import requests
import datetime
import threading
from notifypy import Notify


def notiNews():
    i=0
    while(i < 5):
        threading.Timer(5.0, notiNews).start()
        notification = Notify()
        notification.title = newsArr[i]["title"]
        notification.message = newsArr[i]["summary"]
        notification.icon = f'''{newsArr[i]["banner_image"]},size=(50,50)'''
        # notification.icon = requests.get(f'''{newsArr[i]["banner_image"]},size=(50,50)''')
        notification.send()
        i+=1


current_time = datetime.datetime.now()
y,m,d,h,mi = str(current_time.year),str(current_time.month),str(current_time.day),str(current_time.hour),(current_time.minute)
url = f'''https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey=L3II1KJ3ZK303WM5&topics=technology&sort=LATEST&limit=1&datatype=csv'''
try:
    r = requests.get(url)
    print("SUCCESS")
except :
    print("CHECK YOUR INTERNET !")
data = r.json()
newsArr = data["feed"]
notiNews()