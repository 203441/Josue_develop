import random
import queue
import threading
import time

buffer = queue.Queue(10)

def productor():
    while True:
        if buffer.qsize() < 10:
            valor = random.randint(1, 10)
            buffer.put(valor)
            print(f'Productor inserta el producto: {valor}')
            print(f'Queue actual: {list(buffer.queue)}')
            time.sleep(3)
        else:
            time.sleep(3)

def consumidor():
    while True:
        if buffer.qsize() > 0:
            valor = buffer.get()
            print(f'Consumidor toma el producto: {valor}')
            print(f'Queue actual: {list(buffer.queue)}')
            time.sleep(5)
        else:
            time.sleep(5)

productor = threading.Thread(target=productor)
consumidor = threading.Thread(target=consumidor)

productor.start()
consumidor.start()

