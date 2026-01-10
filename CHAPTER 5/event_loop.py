import asyncio

lis = [1, 2, 3, 4]

# ---------- Async calculation ----------
async def calc(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    await asyncio.sleep(0.5)
    return result

# ---------- Main async logic ----------
async def main(loop):
    print("Running with EVENT LOOP methods\n")

    # loop.time()
    print("Loop time at start:", loop.time())

    # Step 1
    total = lis[0] + lis[1]
    print(f"Step 1: {lis[0]} + {lis[1]} = {total}")

    # Step 2: sequential async additions
    for i in range(2, len(lis)):
        total = await calc(total, lis[i])

    print("Final total:", total)

    # stop loop after work is done
    loop.stop()

# ---------- Callback for call_soon ----------
def start_main(loop):
    loop.create_task(main(loop))

# ---------- EVENT LOOP CONTROL ----------
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# loop.call_soon()
loop.call_soon(start_main, loop)

# loop.run_forever()
loop.run_forever()

# loop.close()
loop.close()
