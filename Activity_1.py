import time
import threading
import multiprocessing

# ---------- THREAD FUNCTION ----------
total = 0
lock = threading.Lock()

def calc(a, b):
    global total
    with lock:
        result = a + b
        print(f"The sum of {a} and {b} is {result}")
        time.sleep(0.5)
        total = result
    return result

# ---------- PROCESS FUNCTION ----------
def calc_proc(a, b, total, lock):
    with lock:
        result = a + b
        total.value = result
        print(f"The sum of {a} and {b} is {result}")
        time.sleep(0.5)

# ---------- MAIN ----------
if __name__ == "__main__":
    lis = [1, 2, 3, 4]

    # ---------- THREADING ----------
    print("Running with Threads:")
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")
    start = time.time()

    for i in range(2, len(lis)):
        t = threading.Thread(target=calc, args=(total, lis[i]))
        t.start()
        t.join()
        total = total  # already updated inside calc()

    end = time.time()
    print(f"Total sum is: {total}")
    print(f"Total Execution time is: {end - start:.2f} seconds\n")

    # ---------- MULTIPROCESSING ----------
    print("Now, Running with Multiprocessing:")
    shared_total = multiprocessing.Value('i', lis[0] + lis[1])
    lock = multiprocessing.Lock()

    s = time.time()
    for i in range(2, len(lis)):
        p = multiprocessing.Process(target=calc_proc, args=(shared_total.value, lis[i], shared_total, lock))
        p.start()
        p.join()
        # shared_total.value already updated inside calc_proc()

    e = time.time()
    print(f"Total sum is: {shared_total.value}")
    print(f"Total Execution time is: {e - s:.2f} seconds\n")
