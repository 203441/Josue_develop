import threading
import time

mutex = threading.Lock()

def tomar(id):
    if id == 8:
        print("Persona {} no pudo tomar su palillo".format(id))
        mutex.acquire()
        time.sleep(1.5)
    else:
        print("Persona {} tomo su palillo".format(id))
        mutex.acquire()
        time.sleep(1.5)

def dejar(id):
    print("Persona {} dejo los palillos".format(id))
    mutex.release()
    time.sleep(1.5)

def comer(id):
    print("Persona {} comiendo".format(id))
    time.sleep(2)
    print("Persona {} termino de comer".format(id))

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        tomar(self.id)
        comer(self.id)
        dejar(self.id)


Hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6), Hilo(7), Hilo(8)]

for h in Hilos:
    h.start()