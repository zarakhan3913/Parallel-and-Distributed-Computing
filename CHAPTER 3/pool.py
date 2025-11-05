# Using a Process Pool – Process Based Parallelism
import multiprocessing
import time

def add_numbers(pair):
    a, b = pair
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    time.sleep(0.5)
    return result

if __name__ == '__main__':
    lis = [1, 2, 3, 4]

    print("Step 1:", lis[0], "+", lis[1], "=", lis[0] + lis[1])
    start = time.time()

    # Step 1: starting total
    total = lis[0] + lis[1]

    # Step 2: prepare pairs for pool
    pairs = [(total, lis[i]) for i in range(2, len(lis))]

    # Step 3: create a process pool with 4 workers
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(add_numbers, pairs)

    # Step 4: last result = total sum
    final_sum = results[-1] if results else total

    end = time.time()
    print(f"\nTotal sum is: {final_sum}")
    print(f"Total Execution time: {end - start:.2f} seconds")
# In pool.py, the pairs are made for each addition operation before the processing starts. Thats why 
#its adding 3 and 4 in the last last step rather than 6 and 4 because 6 is the result of 3 + 3 and were not
# present at the time when the pairs were created.