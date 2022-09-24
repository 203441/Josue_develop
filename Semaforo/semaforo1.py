import requests 
import threading
import concurrent.futures
from pprint import pprint
import psycopg2
import json
import pytube
from threading import Thread, Semaphore

guardar = "C:/descarga"
url = ["https://www.youtube.com/watch?v=3hoHzR_13sc",
        "https://www.youtube.com/watch?v=uDS6HHhjK-c",
        "https://www.youtube.com/watch?v=qyMp1ADlRD8",
        "https://www.youtube.com/watch?v=Rq_HzfAj1Ts",
        "https://www.youtube.com/watch?v=SeohEbgglt4",
        "https://www.youtube.com/watch?v=A6CLvslJIAk",
        "https://www.youtube.com/watch?v=ffslI69Ts-o",
        "https://www.youtube.com/watch?v=cVEerfd6OTY",
        "https://www.youtube.com/watch?v=H_RTPXlFfv8",
        "https://www.youtube.com/watch?v=AQOJ4qF0alk"]
semaforo = Semaphore(1)

def descargar(id):
    global x;
    global y;
    y=y+id;
    video = pytube.YouTube(url[x])
    video.streams.first().download(guardar)
    print("video "+ str(y) + " descargado")
    y=1
    x=x+1

def region_critica(id):
    global x;
    x=x+id;
    print ("El hilo"+str(id)+" valor de x="+str(x));
    x=1;
    
class Hilo(Thread):
    def __init__(self,id):
         Thread.__init__(self);
         self.id=id;
 
    def run(self):
          semaforo.acquire();
          descargar(self.id);
          semaforo.release();

hilos = [Hilo(1),Hilo(2),Hilo(3),Hilo(4),Hilo(5),Hilo(6),Hilo(7),Hilo(8),Hilo(9),Hilo(10)];
x=0;
y=0;
for h in hilos: 
     h.start();
