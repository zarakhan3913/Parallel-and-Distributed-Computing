import threading
import time
import random

# ---------- GLOBAL VARIABLES ----------
semaphore = threading.Semaphore(0)
total = 0
lis = [1, 2, 3, 4]
lock = threading.Lock()

# ---------- PRODUCER FUNCTION ----------
def producer(index):
    """Producer prepares the next number from list."""
    global total
    time.sleep(0.5)  # simulating some delay
    num = lis[index]
    print(f"Producer ready with number: {num}")
    semaphore.release()  # signal consumer to process this number
    return num


# ---------- CONSUMER FUNCTION ----------
def consumer(index):
    """Consumer waits until producer gives a number, then adds it."""
    global total
    semaphore.acquire()  # wait for producer
    with lock:
        total += lis[index]
        print(f"Consumer added {lis[index]}, Total = {total}")
    time.sleep(0.5)


# ---------- MAIN ----------
def main():
    global total
    total = lis[0] + lis[1]
    print(f"Initial sum: {lis[0]} + {lis[1]} = {total}")

    for i in range(2, len(lis)):
        t_prod = threading.Thread(target=producer, args=(i,))
        t_cons = threading.Thread(target=consumer, args=(i,))

        t_prod.start()
        t_cons.start()

        t_prod.join()
        t_cons.join()

    print(f"\n✅ Final Total Sum = {total}")


if __name__ == "__main__":
    main()
