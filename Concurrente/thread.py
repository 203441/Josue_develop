import pytube
import concurrent.futures
import threading
import time
import psycopg2
import requests

try:
    conexion = psycopg2.connect(
        host="localhost",
        database='Db_a3', 
        user='postgres', 
        password='gamemode2')
    cursor=conexion.cursor()
    cursor.execute('select version()')
    version=cursor.fetchone()
except Exception as err:
    print('Error')

def write_nombres():
    url = "https://randomuser.me/api/?results=5"
    r = requests.get(url)
    data = r.json()
    photos = data
    for photo in photos:
        write_db(photo["title"])
    print("Se ha completado la inserción de los 5000 datos")

def write_db(title):
    try:
        cursor.execute("insert into title (name) values ('"+title+"')")
    except Exception as err:
        print('Hubo un error en la inserción: '+ err)
    else:
        conexion.commit()

enlaces = [
    'https://youtu.be/fgoUZjaS8eE',
    'https://youtu.be/sKyU3wHodlI',
    'https://youtu.be/0X8uwcpnyfE',
    'https://youtu.be/6GDgPh_ilEM',
    'https://youtu.be/0aiIvcBe298',
    'https://youtu.be/RU8T8qHfljQ',
    'https://youtu.be/TP_CWS14-fg',
    'https://youtu.be/RYc6YXVtJSI'

]

def download_videos(enlaces):
    yt = pytube.YouTube(enlaces)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download("C:/descarga")
    print(f'{enlaces} se ha descargado...')
with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_videos, enlaces)


def get_services(dato=0):
    print(f'Dato={dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
      
         
         
if __name__ == '__main__':

    for x in range(0,50):
         th1 = threading.Thread(target=get_services, args=[x])
         th1.start()
    th2=threading.Thread(target=write_nombres)
    th3= threading.Thread(target= download_videos, args=[enlaces])  
    th2.start()
    th3.start()