from threading import Thread, Semaphore
from turtle import st
semaforo = Semaphore(1) #crea la bariable semaforo
 
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() #inicializa, lo adquiere
        crito(self.id)
        semaforo.release() #libera un semaforo e incrementa la variable semaforo

threads_semaphore = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for t in threads_semaphore:
    t.start()

#crear una aplicacion en la cual descargarán 10 recursos diferentes integrando el concepto de semaforización