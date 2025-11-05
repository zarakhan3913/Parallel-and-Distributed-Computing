# Importing MPI module to enable message passing between processes
from mpi4py import MPI

# Initializing communicator for all processes
comm = MPI.COMM_WORLD

# Total number of processes involved
size = comm.Get_size()

# Rank (unique ID) of each process (0, 1, 2, ...)
rank = comm.Get_rank()

# Full list of numbers that we want to sum
lis = [1, 2, 3, 4]

# Dividing the work: each process will handle one element from the list
# For simplicity, we assume number of processes == length of list
# Each process picks its corresponding element from the list based on its rank
data = lis[rank]

# Printing which process is handling which number
print(f"Process {rank} handling number: {data}", flush=True)

# Each process now sends its number to the root process (rank = 0)
# gather() collects all the data into a list at the root
collected_data = comm.gather(data, root=0)

# Only the root process will execute this block
if rank == 0:
    print(f"\nRoot process (rank {rank}) received data from all processes: {collected_data}", flush=True)

    # Step 1: Add the first two numbers (like your earlier code)
    total = collected_data[0] + collected_data[1]
    print(f"Step 1: {collected_data[0]} + {collected_data[1]} = {total}", flush=True)

    # Step 2: Add the remaining numbers one by one
    for i in range(2, len(collected_data)):
        result = total + collected_data[i]
        print(f"The sum of {total} and {collected_data[i]} is {result}", flush=True)
        total = result

    # Final total sum after combining all parts
    print(f"\nTotal sum is: {total}", flush=True)
