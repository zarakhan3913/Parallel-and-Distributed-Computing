# Import MPI module
from mpi4py import MPI

# Initialize communicator
comm = MPI.COMM_WORLD

# Rank (ID) of the current process
rank = comm.Get_rank()

# Total number of processes
size = comm.Get_size()

# Full list of numbers to sum (only root process knows full list)
numbers = None
if rank == 0:
    numbers = [1, 2, 3, 4]  # This can be any list
    print(f"Root process (rank {rank}) has numbers: {numbers}", flush=True)

# ---------- SEND TASK ----------
# Here, root process sends each number to a specific process
if rank == 0:
    # Send 2nd number to process 1
    comm.send(numbers[1], dest=1)
    print(f"Process {rank} sending {numbers[1]} to process 1", flush=True)

    # Send 3rd number to process 2
    comm.send(numbers[2], dest=2)
    print(f"Process {rank} sending {numbers[2]} to process 2", flush=True)

    # Send 4th number to process 3
    comm.send(numbers[3], dest=3)
    print(f"Process {rank} sending {numbers[3]} to process 3", flush=True)

# ---------- RECEIVE TASK ----------
# Processes 1,2,3 receive their numbers from root
if rank in [1, 2, 3]:
    recv_number = comm.recv(source=0)  # Receive number from root
    print(f"Process {rank} received number: {recv_number}", flush=True)
else:
    # Root process also keeps its first number
    recv_number = numbers[0]

# ---------- GATHER BACK TO ROOT ----------
# Each process sends its "partial sum" (number) back to root
if rank != 0:
    comm.send(recv_number, dest=0)  # Non-root processes send to root

# Root process collects all numbers
if rank == 0:
    total = recv_number  # Start with its own number
    for i in range(1, 4):  # Expect numbers from processes 1,2,3
        received = comm.recv(source=i)
        print(f"Root received {received} from process {i}", flush=True)
        total += received  # Add to running total
        print(f"Updated total: {total}", flush=True)

    # Final total sum
    print(f"\nTotal sum is: {total}", flush=True)