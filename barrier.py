import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import sleep, time
from datetime import datetime

# ---------- Function ----------
def calc_sum(a, b, synchronizer, serializer, total):
    name = multiprocessing.current_process().name
    synchronizer.wait()  # sab processes yahan tak rukenge
    result = a + b
    with serializer:  # ek time pe ek hi process print kare
        print(f"{name} --> The sum of {a} and {b} is {result} at {datetime.now()}")
    sleep(0.5)
    total.value = result

# ---------- MAIN ----------
if __name__ == '__main__':
    lis = [1, 2, 3, 4]
    total = multiprocessing.Value('i', lis[0] + lis[1])  # shared memory
    print(f"Step 1: {lis[0]} + {lis[1]} = {total.value}\n")

    synchronizer = Barrier(2)  # 2 processes ek saath synchronize honge
    serializer = Lock()
    start = time()

    # Har step me 2 processes ek saath run karte hain
    for i in range(2, len(lis)):
        p1 = Process(name=f'P{i}-A', target=calc_sum, args=(total.value, lis[i], synchronizer, serializer, total))
        p2 = Process(name=f'P{i}-B', target=calc_sum, args=(total.value, lis[i], synchronizer, serializer, total))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    end = time()
    print(f"\nFinal Total Sum: {total.value}")
    print(f"Total Execution Time: {end - start:.2f} seconds")
