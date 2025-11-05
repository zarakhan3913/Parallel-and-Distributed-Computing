Project Description:
This project demonstrates three process-based parallelism techniques in Python using the multiprocessing module — Spawning, Pool, and Barrier.
Each method performs a simple addition task on a list of numbers ([1, 2, 3, 4]) and compares how processes synchronize and communicate.

1. Spawning a Process (spawning.py)

Technique Used:
Each addition operation runs in a separate process that is spawned dynamically using multiprocessing.Process().

Working:

A new process is created for every addition step.

Shared memory (Value) is used to keep track of the total sum.

A Lock ensures that only one process updates the total at a time.

Key Point:
Each process starts and ends before the next one begins due to .join() — giving controlled parallel execution.

2. Using a Process Pool (pool.py)

Technique Used:
Uses a process pool — a fixed number of worker processes created in advance using multiprocessing.Pool().

Working:

The pool distributes multiple addition tasks to its worker processes.

The pairs to be added are prepared before the pool starts processing.

Since pairs are pre-generated, later additions (like 6 + 4) are not updated dynamically.

Key Point:
This technique improves efficiency when dealing with a large number of tasks but doesn’t maintain real-time dependency between steps.

3. Using Barrier Synchronization (barrier.py)

Technique Used:
Combines Barrier and Lock for synchronized parallel execution.

Working:

Two processes run simultaneously at each step.

Barrier ensures both reach the same point before proceeding.

Lock prevents overlapping console output and shared memory conflicts.

Key Point:
Useful when processes must reach the same stage together before continuing, ensuring controlled parallel synchronization.