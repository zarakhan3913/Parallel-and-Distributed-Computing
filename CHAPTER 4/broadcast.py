# Import MPI module
from mpi4py import MPI

# Initialize communicator
comm = MPI.COMM_WORLD

# Rank of the current process
rank = comm.Get_rank()

# Total number of processes
size = comm.Get_size()

# Full list of numbers to sum (only root knows it)
numbers = None
if rank == 0:
    numbers = [1, 2, 3, 4]  # Root process has the full list
    print(f"Root process (rank {rank}) has numbers: {numbers}", flush=True)

# ---------- BROADCAST TASK ----------
# Each number will be broadcasted one by one
total = 0  # Running total sum

for i in range(len(numbers) if rank == 0 else 4):
    # Root process picks the number to broadcast
    if rank == 0:
        current_number = numbers[i]
    else:
        current_number = None  # Other processes start with None

    # Broadcast current_number from root to all processes
    current_number = comm.bcast(current_number, root=0)

    # Each process now has the current number and can add it to its total
    total += current_number

    # Print which process received which number
    print(f"Process {rank} received {current_number}, running total = {total}", flush=True)

# After all numbers are broadcasted, root can print final sum
if rank == 0:
    print(f"\nFinal total sum (computed via broadcast) = {total}", flush=True)
