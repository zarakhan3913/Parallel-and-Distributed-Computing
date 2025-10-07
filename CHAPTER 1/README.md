Program Description

This Python program calculates a cumulative sum using both Threads and Multiprocessing.

The program is designed to:

1. Calculate the sum of the first two elements.

2. Add the next element to the previous sum.

3. Continue this step-by-step until all elements in the list are included in the cumulative sum.

Additionally, it demonstrates how to control the execution order in threads and processes to ensure correct cumulative sums.

Code Structure:
1. Thread Function (calc)
Takes two numbers a and b and calculates their sum.

Uses a lock to prevent race conditions between threads.

Stores the result in result_list so the main loop can update the cumulative total.

time.sleep(0.5) is added to clearly visualize sequential thread execution.

2. Multiprocessing Function (calc_proc)

Similar to the thread function, but works with process-safe shared values (multiprocessing.Value).

lock ensures that only one process updates the shared total at a time.

Delay (time.sleep) is used to make sequential execution visible.

3. Main Program

First, the sum of the first two elements is calculated.

Next elements are added sequentially using threads.

t.join() ensures threads run in order — the next thread starts only after the previous finishes.

This guarantees correct cumulative sums.

Multiprocessing:

shared_total is a process-safe shared integer.

Each process updates the cumulative sum in order.

join() ensures sequential execution of processes.

Input Data:

Example list: lis = [1, 2, 3, 4]

Data size: 4 integers (4 bytes each) → ~16 bytes for the list.

Threading and multiprocessing require small additional memory for locks and temporary variables (~few KB).
