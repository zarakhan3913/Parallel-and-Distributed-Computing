import asyncio

lis = [1, 2, 3, 4]

# ---------- Async calculation function ----------
async def calc(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    await asyncio.sleep(0.5)  # simulate processing delay
    return result

# ---------- Main Async Function ----------
async def main():
    print("Running with asyncio tasks:")

    # Step 1: start with first two numbers
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")

    # Step 2: create tasks for remaining numbers
    tasks = []

    # Instead of sequential await, we create tasks
    current_total = total
    for i in range(2, len(lis)):
        # each task adds current_total + lis[i]
        tasks.append(asyncio.create_task(calc(current_total, lis[i])))
        # update current_total for next task
        current_total += lis[i]

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    print("All async tasks completed!")
    print("Results:", results)
    print(f"Final total (manual calculation): {current_total}")

# ---------- Run ----------
asyncio.run(main())
