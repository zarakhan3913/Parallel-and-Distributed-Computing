import time
from concurrent.futures import ThreadPoolExecutor, as_completed

lis = [1, 2, 3, 4]

# ---------- Function to run in thread ----------
def calc(a, b):
    print(f"Starting calculation: {a} + {b}")
    time.sleep(0.5)  # simulate delay
    result = a + b
    print(f"Finished calculation: {a} + {b} = {result}")
    return result

# ---------- Main ----------
def main():
    print("Running with Future methods demonstration:")

    # Step 1: start with first two numbers
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")

    current_total = total
    futures = []

    with ThreadPoolExecutor() as executor:
        # Step 2: Submit tasks
        for i in range(2, len(lis)):
            future = executor.submit(calc, current_total, lis[i])
            futures.append(future)
            current_total += lis[i]  # track manually for next task

        # Step 3: Demonstrate Future methods
        for future in futures:
            print("\nChecking future status:")
            print("Running:", future.running())  # True if currently running
            print("Done:", future.done())        # False if not finished

        # Step 4: Attempt to cancel (may fail if task started)
        for i, future in enumerate(futures):
            if future.cancel():
                print(f"Task {i} cancelled successfully")
            else:
                print(f"Task {i} could not be cancelled (already running or finished)")

        # Step 5: Get results (blocks until finished)
        results = []
        for future in futures:
            result = future.result()
            results.append(result)
            print(f"Result retrieved from future: {result}")

    print("\nAll tasks completed!")
    print("Final total (manual calculation):", current_total)
    print("Results from futures:", results)

# ---------- Run ----------
if __name__ == "__main__":
    main()
