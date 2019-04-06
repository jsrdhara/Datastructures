import threading
import time

def sleeper(n,name):
    print('Hi I am {} goint to sleep for 5 sec \n'.format(name))
    time.sleep(n)
    print('{} has woken from sleep \n'.format(name))


threads_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper,name='thread {}'.format(i),args=(5,'thread {}'.format(i)))
    threads_list.append(t)
    t.start()
    print('{} has started'.format(t.name))

for t in threads_list:
    t.join()
stop = time.time()
print('All five threads have finished jobs in {}'.format(stop-start))
