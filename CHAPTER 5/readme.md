Description:
This project demonstrates five asynchronous and concurrent programming techniques in Python — async/await, asyncio tasks, TaskGroup, event loop control, and ThreadPoolExecutor with futures. Each method performs a simple addition task on a list of numbers [1, 2, 3, 4] and shows how Python handles concurrent execution and asynchronous operations.

Async Sequential (async.py)

Technique Used: Uses async and await to perform sequential asynchronous operations.

Working:

Starts with the sum of the first two numbers in the list.

Each remaining number is added sequentially using await calc(total, number).

Simulates processing delays using asyncio.sleep(0.5).

Key Point: Sequential async is useful when tasks need to run one after another, but still take advantage of asynchronous I/O to avoid blocking the main thread.

Async Concurrent with Tasks (async_concurrent.py)

Technique Used: Creates multiple asyncio tasks using asyncio.create_task() for concurrent execution.

Working:

Starts with the sum of the first two numbers.

Creates tasks for remaining numbers to run concurrently.

Uses asyncio.gather(*tasks) to wait for all tasks to complete.

Key Point: Concurrent tasks allow independent operations to run simultaneously, improving efficiency in I/O-bound scenarios.

TaskGroup (asyncio.taskgrup.py)

Technique Used: Groups multiple asynchronous tasks using asyncio.TaskGroup (Python 3.11+).

Working:

Starts with the sum of the first two numbers.

Adds remaining numbers as tasks inside a TaskGroup.

TaskGroup automatically ensures all tasks finish and handles exceptions.

Key Point: TaskGroup simplifies managing multiple async tasks and provides better error handling compared to manually created tasks.

Event Loop Control (event_loop.py)

Technique Used: Manual event loop management using loop.create_task() and loop.run_forever().

Working:

Creates a new asyncio event loop.

Schedules the main async function with loop.call_soon().

Runs the loop manually with loop.run_forever() and stops it after completion.

Key Point: Understanding the event loop allows fine-grained control over asynchronous program execution.

Concurrent Futures (concurrent_future.oy)

Technique Used: Uses ThreadPoolExecutor and Future objects for thread-based concurrent execution.

Working:

Starts with the sum of the first two numbers.

Submits remaining additions as separate tasks to the thread pool.

Checks task status with future.running() and future.done().

Attempts to cancel tasks using future.cancel().

Retrieves results with future.result().

Key Point: ThreadPoolExecutor is useful for CPU-bound or I/O-bound tasks that can run in parallel on separate threads.