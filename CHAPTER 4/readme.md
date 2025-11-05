Description:
This project demonstrates five MPI-based parallelism techniques in Python using the mpi4py module — Scatter, Gather, All-to-All, Broadcast, and Point-to-Point.
Each method performs a simple addition task on a list of numbers ([1, 2, 3, 4]) or a variable-sharing example and shows how processes communicate and synchronize data in different ways.

1. Gather (gather.py)

Technique Used:
All processes send their data to a root process using comm.gather().

Working:

Each process picks one element from a list based on its rank.

gather() collects all values at the root process (rank 0).

Root process then adds numbers sequentially to calculate the total sum.

Key Point:
Gather is useful when you want to collect all results at a single process for further computation.

2. Scatter (scatter.py)

Technique Used:
Root process distributes an array among all processes using comm.scatter().

Working:

Root process holds the full array.

Each process receives a single element (or chunk) of the array.

Processes can independently perform operations on the received data.

Key Point:
Scatter is useful when distributing tasks among processes for parallel computation.

3. All-to-All (alltoall.py)

Technique Used:
Every process sends its data to all other processes, simulating full communication.

Working:

Each process sends its value to all others using comm.send().

Each process receives values from all other processes using comm.recv().

Key Point:
All-to-All is useful for problems where each process depends on data from every other process.

4. Broadcast (broadcast.py)

Technique Used:
Root process shares a single value to all processes simultaneously using comm.bcast().

Working:

Root process sets a variable.

bcast() sends this value to every other process.

All processes now have the same variable.

Key Point:
Broadcast is efficient for distributing configuration variables or constants to all processes.

5. Point-to-Point (Send/Recv) (point_to_point.py)

Technique Used:
A specific process sends data to another specific process using comm.send() and comm.recv().

Working:

Sending process uses comm.send(data, dest=target_rank).

Receiving process uses comm.recv(source=source_rank) to get the data.

Key Point:
Point-to-Point communication is useful when only specific processes need to exchange information.