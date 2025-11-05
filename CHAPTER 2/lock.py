import time                     # time module ko import kiya delay (sleep) aur timing measure karne ke liye
import threading                # threading module import kiya threads create aur manage karne ke liye
import multiprocessing          # multiprocessing module import kiya multiple processes banane ke liye

# ---------- THREAD FUNCTION ----------
total = 0                       # ek global variable 'total' banaya jo shared data hoga sab threads ke liye
lock = threading.Lock()          # lock object create kiya jo ek time pe sirf ek thread ko access allow karega

# Thread function define kiya
def calc(a, b):
    global total                 # global variable use ho raha hai
    with lock:                   # lock acquire ho gaya (sirf ek thread yahan kaam karega)
        result = a + b           # do numbers ka sum nikala
        print(f"The sum of {a} and {b} is {result}")   # result print kiya
        time.sleep(0.5)          # 0.5 second ka delay diya taake threads overlapping effect na dein
        total = result           # global total update kiya
    return result                # function sum return karta hai


# ---------- PROCESS FUNCTION ----------
def calc_proc(a, b, total, lock):
    # yeh function multiprocessing ke liye use ho raha hai
    with lock:                   # lock acquire (ek time pe ek hi process shared memory ko access karega)
        result = a + b           # do numbers ka sum nikala
        total.value = result     # shared variable (multiprocessing.Value) ko update kiya
        print(f"The sum of {a} and {b} is {result}")   # result print kiya
        time.sleep(0.5)          # 0.5 second delay


# ---------- MAIN FUNCTION ----------
if __name__ == "__main__":       # ensure karta hai ke ye code sirf tab chale jab direct run ho
    lis = [1, 2, 3, 4]           # ek list banayi jisme numbers hain jinhe sum karna hai

    # ---------- THREADING ----------
    print("Running with Threads:")
    total = lis[0] + lis[1]      # list ke first two elements ka sum nikala aur total me store kiya
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")   # pehla step print kiya
    start = time.time()           # start time note kiya execution time calculate karne ke liye

    # list ke remaining elements pe threads run kiye
    for i in range(2, len(lis)):  # loop list ke 3rd element se start hota hai
        t = threading.Thread(target=calc, args=(total, lis[i]))  # ek new thread banaya jo calc() function ko run karega
        t.start()                # thread start kiya
        t.join()                 # join() se ensure kiya ke ek thread complete ho tab next chale

    end = time.time()             # end time note kiya
    print(f"Total sum is: {total}")   # final total print kiya
    print(f"Total Execution time is: {end - start:.2f} seconds\n")  # total time display kiya


    # ---------- MULTIPROCESSING ----------
    print("Now, Running with Multiprocessing:")
    shared_total = multiprocessing.Value('i', lis[0] + lis[1])  # shared memory variable banaya jisme initial sum store kiya
    lock = multiprocessing.Lock()        # multiprocessing ke liye alag lock banaya

    s = time.time()                      # multiprocessing ke start time note kiya
    for i in range(2, len(lis)):         # loop list ke 3rd element se start hota hai
        # ek new process banaya jo calc_proc() function ko run karega
        p = multiprocessing.Process(target=calc_proc, args=(shared_total.value, lis[i], shared_total, lock))
        p.start()                        # process start kiya
        p.join()                         # process complete hone ka wait kiya

    e = time.time()                      # end time note kiya
    print(f"Total sum is: {shared_total.value}")   # final shared total print kiya
    print(f"Total Execution time is: {e - s:.2f} seconds\n")  # total execution time print kiya
