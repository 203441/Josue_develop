import time
from threading import Thread
from weakref import finalize
import requests
urls = ["https://classroom.google.com", "http://docs.python-requests.org", "https://w12w.digite.com",
    "https://www.sogeti.es", "https://www.youtube.com/watch?v=R04XlO-xsvw&t=441s", "https://www.muycomputer.com", "https://www.instagram.com/oscarmezar",
    "https://facebook.com",
    "https://web.whatsapp.com",
    "https://wikipedia.org",
    "https://classroom.google.com",
    "https://ww2.youtube.com/watch?v=HWVlxMwx8KY",
    "https://www.amazon.com.mx",
    "https://spa.myservername.com",
    "https://auto.mercadolibre.com.m",
    "https://www.msn.com/",
    "http://classroom.google.com",
    "https://www.mercadolibre.com.mx",
    "https://www.instagram.com/bemu.m",
    "https://www.starplus.com",
    "https://www.hbomax.com",
    "https://w2ww.msn.com",
    "https://www.disneyplus.com",
    "https://www.instagram.com/chefschwarz",
    "https://www.netflix.com",
]

def check_site(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            time.sleep(4)
            response = requests.head(url)
            if response.status_code == 200:
                print(f"la url {url} esta activa")
            else:
                print(f"la url {url} esta inactiva")
        else:
            print(f"la {url} esta inactiva")
    except:
        print(f"la url {url} esta inactiva")      

class Hilo(Thread):
    def _init_(self, url):
        Thread._init_(self)
        self.url = url

    def run(self):
        check_site(self.url)

h1 =  [Hilo(urls[0]), Hilo(urls[1]), Hilo(urls[2]), Hilo(urls[3]), Hilo(urls[4]), Hilo(urls[5]), Hilo(urls[6]), Hilo(urls[7]), Hilo(urls[8]), 
        Hilo(urls[9]), Hilo(urls[10]), Hilo(urls[11]), Hilo(urls[12]), Hilo(urls[13]), Hilo(urls[14]), Hilo(urls[15]), Hilo(urls[16]), Hilo(urls[17]), 
        Hilo(urls[18]), Hilo(urls[19]), Hilo(urls[20]), Hilo(urls[21]), Hilo(urls[22]), Hilo(urls[23]), Hilo(urls[24])]

for h in h1:
    h.start()





