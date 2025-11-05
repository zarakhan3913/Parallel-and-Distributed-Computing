import multiprocessing   # multiple processes banane ke liye module import kar rahe hain

def worker(rank, lis, shared_list, barrier):
    """
    har process ye function run karega
    rank = process number (0,1,2,...)
    lis = number list
    shared_list = ek shared memory list jisme sab apne results likhenge
    barrier = synchronization point tak sab processes rukte hain
    """

    # har process apna local number lega
    local_sum = lis[rank]  # apni index ka number uthaya
    print(f"Process {rank}: initial value {local_sum}")

    # apna result shared list me likh do
    shared_list[rank] = local_sum  # shared memory me likh diya

    # sab processes barrier tak rukenge, taake sab likh chuke ho
    barrier.wait()

    # ab har process shared list ke through sab numbers read karega
    for i, val in enumerate(shared_list):
        if i != rank:  # khud ka value skip
            print(f"Process {rank} received {val} from Process {i}")
            local_sum += val  # har value apne total me add karo

    print(f"Process {rank}: final total = {local_sum}")  # final sum print

if __name__ == "__main__":
    lis = [1, 2, 3, 4]  # list of numbers
    n = len(lis)        # number of processes

    with multiprocessing.Manager() as manager:  # shared memory manager start
        shared_list = manager.list([0]*n)       # sab processes ke liye ek shared list banai
        barrier = multiprocessing.Barrier(n)    # sab processes ek point pe synchronize karenge

        processes = []  # sab process objects yahan store honge
        for i in range(n):
            p = multiprocessing.Process(target=worker, args=(i, lis, shared_list, barrier))
            processes.append(p)
            p.start()   # process start karo

        for p in processes:
            p.join()    # sab processes ke complete hone ka wait karo
    print("All processes completed.")