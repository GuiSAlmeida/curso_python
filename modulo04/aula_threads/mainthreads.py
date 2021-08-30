from time import sleep
from threading import Thread


class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


def slow(text, time):
    sleep(time)
    print(text)


t1 = MyThread('thread1', 5)
t1.start()

t2 = Thread(target=slow, args=('olá', 5))
t2.start()
# t2.join() bloquea a sequencia da stack

for i in range(10):
    print(i)
    sleep(1)

while t1.is_alive():
    print('Esperando a thread 1')
    sleep(2)
