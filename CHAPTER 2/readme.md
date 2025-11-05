Description:
This chapter demonstrates three synchronization mechanisms in Python — Lock, Reentrant Lock (RLock), and Semaphore — using both threading and multiprocessing.
Each file performs a simple addition task on a list of numbers ([1, 2, 3, 4]) to show how shared resources can be safely accessed in concurrent environments.

1. Using Lock (lock.py)

Technique Used:
Basic mutual exclusion lock (Lock) ensures that only one thread or process accesses a shared variable at a time.

Working:

For threading, a global Lock prevents two threads from updating total simultaneously.
For multiprocessing, a separate Lock ensures only one process updates shared memory (multiprocessing.Value).
The .join() method ensures that one thread/process finishes before the next starts.

Key Point:
Guarantees thread-safe access to shared data — avoiding race conditions.

2. Using Reentrant Lock (r_lock.py)

Technique Used:
A Reentrant Lock (RLock) allows a thread to acquire the same lock multiple times safely.

Working:

Similar to a regular Lock, but RLock can be acquired recursively by the same thread.

This is useful when a function that holds a lock calls another function that also tries to acquire the same lock.

Threading and multiprocessing sections behave similarly, ensuring safe access to shared memory.

Key Point:
Ideal for complex, nested functions where the same thread needs to re-acquire the lock without deadlocking.

3. Using Semaphore (semaphore.py)

Technique Used:
A Semaphore is a signaling mechanism that controls how many threads can access a shared resource simultaneously.

Working:

The producer thread prepares a number and releases the semaphore.
The consumer thread waits (acquire()) until the semaphore is released.
A Lock ensures the total is updated safely.
Together, they demonstrate producer-consumer synchronization.

Key Point:
Semaphores are best for managing resource availability or coordination between threads.

Summary:
All three techniques help prevent race conditions and maintain data consistency during parallel execution:
Lock → Simplest mutual exclusion
RLock → Safer for recursive code
Semaphore → Ideal for coordination between threads

