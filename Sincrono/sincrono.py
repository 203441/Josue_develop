import requests
import time
import psycopg2
import concurrent.futures
import threading
import pytube
threading_local = threading.local()
conexion1 = psycopg2.connect(user='postgres', 
                            password='gamemode2', 
                            host='localhost', 
                            port='5432', 
                            database='Db_a3')

cursor = conexion1.cursor()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service_db, url)

def get_service_db():
    response = requests.get("https://randomuser.me/api/?results=2500")
        
    if response.status_code == 200:
        lista = response.json().get('results')
        for i in lista: 
            write_db(i['name']['first'])

def write_db(x):
    cursor.execute("insert into name(nombre) values('"+x+"')")
    conexion1.commit()

links = [
    'https://www.youtube.com/watch?v=Mr61JbHOyTo',
    'https://www.youtube.com/watch?v=xh01ZHoJ50w',
    'https://www.youtube.com/watch?v=M1rIGnlHwbc',
    'https://www.youtube.com/watch?v=A6CLvslJIAk',
    'https://www.youtube.com/watch?v=SeohEbgglt4'
]

def download_videos(enlaces):
    yt = pytube.YouTube(enlaces)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download("C:/descarga")
    print(f'{enlaces} se ha descargado...')
with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_videos, links)

def get_services():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name=results[0].get('name').get('first')
        print(name)

if __name__ == "__main__": #main
    init_time = time.time()
    th2=threading.Thread(target=get_service_db)
    th3= threading.Thread(target= download_videos, args=[links])  
    th2.start()
    th3.start()

    for x in range(0,50):
        th1 = threading.Thread(target=get_services)        
        th1.start()
        th1.join()
    
    end_time = time.time() - init_time
    print(end_time)