# Import MPI module to enable communication between multiple processes
from mpi4py import MPI

# Initialize the communicator
comm = MPI.COMM_WORLD

# Get rank (ID) of this process (0,1,2,...)
rank = comm.Get_rank()

# Total number of processes
size = comm.Get_size()

# Only root process (rank 0) has the full list of numbers
if rank == 0:
    # The list of numbers we want to sum
    array_to_share = [1, 2, 3, 4]  # You can extend this list
else:
    # Other processes start with None
    array_to_share = None

# Scatter the array: each process receives one element from the root process
recvbuf = comm.scatter(array_to_share, root=0)
# recvbuf now contains the element assigned to this process

# Print what each process received (flush=True ensures immediate output)
print(f"Process {rank} received number: {recvbuf}", flush=True)

# Each process now does its "partial sum" (in this case just its number)
partial_sum = recvbuf  # Here each process's partial sum is just the number itself

# Gather all partial sums back to root process
collected_sums = comm.gather(partial_sum, root=0)

# Root process now combines all received numbers to get final total
if rank == 0:
    # Step 1: Add the first two numbers
    total = collected_sums[0] + collected_sums[1]
    print(f"Step 1: {collected_sums[0]} + {collected_sums[1]} = {total}", flush=True)

    # Step 2: Add remaining numbers one by one
    for i in range(2, len(collected_sums)):
        result = total + collected_sums[i]
        print(f"The sum of {total} and {collected_sums[i]} is {result}", flush=True)
        total = result

    # Final total sum
    print(f"\nTotal sum is: {total}", flush=True)
