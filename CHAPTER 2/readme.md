Chapter 2 — Thread Synchronization in Python

This chapter demonstrates three important synchronization mechanisms in Python’s threading module — Lock, RLock, and Semaphore — using a simple list-item addition program. These mechanisms help manage how multiple threads access shared resources safely.

1. Lock — Simple Thread Synchronization

File: lock_list_addition.py

Concept:
A Lock allows only one thread to access a specific block of code at a time.
If another thread tries to enter that block, it has to wait until the lock is released.

Program Explanation:

The program starts multiple threads, each performing addition on a shared variable (total).

A threading.Lock() ensures that only one thread modifies total at a time.

This prevents inconsistent or corrupted results caused by race conditions.

2. RLock — Reentrant Lock

File: rlock_list_addition.py

Concept:
An RLock (Reentrant Lock) is like a normal lock but allows the same thread to acquire the lock multiple times without blocking itself.
It’s useful when a thread needs to call multiple functions that each use the same lock.

Program Explanation:

Similar to the Lock version, but we use threading.RLock().

Inside the Box class, methods like add() and remove() both acquire the same lock, and they internally call another locked method execute().

This nesting is only possible with RLock because a normal Lock would block the same thread.

3. Semaphore — Thread Signaling

File: semaphore_list_addition.py

Concept:
A Semaphore controls how many threads can access a resource simultaneously.
It’s often used to manage producer-consumer relationships or to limit the number of concurrent operations.

Program Explanation:

Two threads — one producer and one consumer — share a semaphore.

The consumer waits (using semaphore.acquire()) until the producer produces an item and releases the semaphore.

This coordination ensures the consumer only processes items when they are available.

Adapted here for list addition tasks — each operation waits for the signal before proceeding.