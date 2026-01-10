import asyncio

lis = [1, 2, 3, 4]

# ---------- Async calculation function ----------
async def calc(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    await asyncio.sleep(0.5)  # simulate processing delay
    return result

# ---------- Main Async Function using TaskGroup ----------
async def main():
    print("Running with asyncio TaskGroup:")

    # Step 1: start with first two numbers
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")

    # Step 2: create tasks in a TaskGroup
    results = []

    async with asyncio.TaskGroup() as tg:
        # We will add tasks for remaining numbers
        current_total = total
        for i in range(2, len(lis)):
            # TaskGroup ensures all tasks complete and handles errors
            tg.create_task(calc(current_total, lis[i]))
            current_total += lis[i]

    print("All tasks in TaskGroup completed!")
    print("Final total (manual calculation):", current_total)

# ---------- Run ----------
asyncio.run(main())
