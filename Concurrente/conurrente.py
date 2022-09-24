from urllib import response
import requests
import time
import psycopg2
#concurrent.future

conexion1 = psycopg2.connect(user='postgres', password='gamemode2', host='localhost', port='5432', database='Db_a3')
cursor = conexion1.cursor()

def get_service():
    response = requests.get("https://randomuser.me/api/?results=5")
    
    if response.status_code == 200:
        lista = response.json().get('results')
        
        for i in lista: 
            write_db(i['name']['first'])

def write_db(x):
    cursor.execute("insert into name(nombre) values('"+x+"')")
    conexion1.commit()

if __name__ == "__main__": #main
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)

    conexion1.close()
