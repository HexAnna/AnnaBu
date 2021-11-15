# «Задачи об обедающих философах»

import time
import threading
from threading import Event, BoundedSemaphore

event = Event()
bs = BoundedSemaphore(2)
variable = [1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
mutex = threading.Lock()

a = [0, 0]
b = [0, 0]
c = [0, 0]
e = [0, 0]
f = [0, 0]


# check

def philosopher_a(interval):
    while True:
        bs.acquire()
        if variable[0] == 1:
            print('Philosopher_a: Time for a snack!')
            variable.append(variable.pop(0))
            bs.release()
            a[0] += 1
            time.sleep(interval)

        else:
            print('Philosopher_a: I think we should think more!')
            bs.release()
            a[1] += 1
            time.sleep(interval)


def philosopher_b(interval):
    while True:
        bs.acquire()
        if variable[0] == 2:
            print('Philosopher_b: I am hungry!')
            variable.append(variable.pop(0))
            bs.release()
            b[0] += 1
            time.sleep(interval)

        else:
            print('Philosopher_b: I think we should think more!')
            bs.release()
            b[1] += 1
            time.sleep(interval)


def philosopher_c(interval):
    while True:
        bs.acquire()
        if variable[0] == 3:
            print('Philosopher_c: Its my turn!')
            variable.append(variable.pop(0))
            bs.release()
            c[0] += 1
            time.sleep(interval)

        else:
            print('Philosopher_c: This is genius! Lets do it!')
            bs.release()
            c[1] += 1
            time.sleep(interval)


def philosopher_e(interval):
    while True:
        bs.acquire()
        if variable[0] == 4:
            print('Philosopher_e: Can we have some tea?')
            variable.append(variable.pop(0))
            bs.release()
            e[0] += 1
            time.sleep(interval)

        else:
            print('Philosopher_e: So what is the meaning of life ?!')
            bs.release()
            e[1] += 1
            time.sleep(interval)


def philosopher_f(interval):
    while True:
        bs.acquire()
        if variable[0] == 5:
            print('Philosopher_f: And I would have some coffee!')
            variable.append(variable.pop(0))
            bs.release()
            f[0] += 1
            time.sleep(interval)

        else:
            print('Philosopher_f: I think we should think more!')
            bs.release()
            f[1] += 1
            time.sleep(interval)


def static(interval):
    while True:
        print(variable)
        print(a, b, c, e, f)
        time.sleep(interval)


if __name__ == '__main__':
    thread1 = threading.Thread(target=philosopher_a, args=(0.1,))
    thread2 = threading.Thread(target=philosopher_b, args=(0.1,))
    thread3 = threading.Thread(target=philosopher_c, args=(0.1,))
    thread4 = threading.Thread(target=philosopher_e, args=(0.1,))
    thread5 = threading.Thread(target=philosopher_f, args=(0.1,))
    static_thread = threading.Thread(target=static, args=(30,))

    # Поток проверки все ли поели и подумали

    threads = [thread1, thread5, thread4, thread3, thread2, static_thread]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
