from threading import Thread, Semaphore
import pytube
semaforo = Semaphore(1) #crea la variable semaforo

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

def crito(id, video):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

    yt = pytube.YouTube(str(video))
    yt.streams.first().download("C:/descarga")
    print(f'{video} descargado')

class Hilo(Thread):
    def _init_(self, id, video):
        Thread._init_(self)
        self.id=id
        self.video=video

    def run(self):
        semaforo.acquire()
        crito(self.id, self.video)
        semaforo.release()

threads_semaphore = [Hilo(1, url[0]), Hilo(2, url[1]), Hilo(3, url[2]), Hilo(4, url[3]), Hilo(5, url[4]), Hilo(6, url[5]), Hilo(7, url[6]), Hilo(8, url[7]), Hilo(9, url[8]), Hilo(10, url[9])]
x=0;
for t in threads_semaphore:
    t.start()