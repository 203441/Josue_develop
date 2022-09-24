import pytube
import threading

mutex= threading.Lock()
videos = ["https://www.youtube.com/watch?v=3hoHzR_13sc",
        "https://www.youtube.com/watch?v=uDS6HHhjK-c",
        "https://www.youtube.com/watch?v=qyMp1ADlRD8",
        "https://www.youtube.com/watch?v=Rq_HzfAj1Ts",
        "https://www.youtube.com/watch?v=SeohEbgglt4",
        "https://www.youtube.com/watch?v=A6CLvslJIAk",
        "https://www.youtube.com/watch?v=ffslI69Ts-o",
        "https://www.youtube.com/watch?v=cVEerfd6OTY",
        "https://www.youtube.com/watch?v=H_RTPXlFfv8",
        "https://www.youtube.com/watch?v=AQOJ4qF0alk"]

def crito(video):
    yt = pytube.YouTube(str(video))
    yt.streams.first().download("C:/descarga")
    print(f'{video} se descargo')

class Hilo(threading.Thread):
    def __init__(self, video):
        threading.Thread.__init__(self)
        self.video=video

    def run(self):
        mutex.acquire()
        crito(self.video)
        mutex.release()

hilos = [Hilo(videos[0]), Hilo(videos[1]), Hilo(videos[2]), Hilo(videos[3]), Hilo(videos[4]), Hilo(videos[5]), Hilo(videos[6]), Hilo(videos[7]), Hilo(videos[8]), Hilo(videos[9])]

for h in hilos:
    h.start()