# Spawn a Process – Process Based Parallelism
import multiprocessing
import time

def calc_sum(a, b, total, lock):
    with lock:
        result = a + b
        print(f"The sum of {a} and {b} is {result}")
        time.sleep(0.5)
        total.value = result  # shared memory me result update
    return

if __name__ == '__main__':
    lis = [1, 2, 3, 4]
    total = multiprocessing.Value('i', lis[0] + lis[1])
    lock = multiprocessing.Lock()

    print("Step 1:", lis[0], "+", lis[1], "=", total.value)
    start = time.time()

    # har iteration me naya process spawn karte hain
    for i in range(2, len(lis)):
        process = multiprocessing.Process(target=calc_sum, args=(total.value, lis[i], total, lock))
        process.start()   # new process spawn hota hai
        process.join()    # wait for process to complete

    end = time.time()

    print(f"\nTotal sum is: {total.value}")
    print(f"Total Execution time: {end - start:.2f} seconds")
