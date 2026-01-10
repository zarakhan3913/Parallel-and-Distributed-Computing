import asyncio
import time

lis = [1, 2, 3, 4]

async def calc(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    await asyncio.sleep(0.5)  # simulate processing delay
    return result

async def main():
    print("Running asynchronously:")
    
    # Step 1: start with first two numbers
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")

    start = time.time()

    # Step 2: add remaining numbers asynchronously
    for i in range(2, len(lis)):
        total = await calc(total, lis[i])

    end = time.time()
    print(f"Total sum is: {total}")
    print(f"Total execution time: {end - start:.2f} seconds")

# Run the async main
asyncio.run(main())
