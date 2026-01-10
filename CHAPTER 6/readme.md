Description:
This project demonstrates network communication in Python using sockets and remote procedure calls with Pyro4. It includes client-server examples for sending and receiving messages and a remote object example for performing calculations across machines.

Socket Server (server.py)

Technique Used: Creates a TCP socket server that listens for a single client connection.

Working:

Server creates a socket and binds it to host and port.

Listens for incoming client connections (listen()).

Accepts a connection with accept() and receives data from the client.

Prints the received message and sends a response back.

Closes the connection after communication.

Key Point: A basic TCP server allows a client to connect, send data, and receive a response in a sequential manner.

Socket Client (client.py)

Technique Used: Creates a TCP socket client to connect to a server and exchange messages.

Working:

Client creates a socket and connects to the server’s host and port.

Sends a message using send().

Receives server’s response using recv().

Closes the connection after communication.

Key Point: Socket clients are used to communicate with servers over TCP/IP by sending and receiving byte streams.

Multi-Client Socket Server (socket_server.py)

Technique Used: TCP server capable of handling multiple sequential clients.

Working:

Creates a listening socket and binds to host and port.

Uses an infinite loop to accept multiple clients one by one.

Receives data from each client and sends a response.

Closes only the client’s connection while keeping the server running.

Key Point: Useful for servers that need to continuously serve multiple clients sequentially.

Multi-Client Socket Client (socket_client.py)

Technique Used: TCP client to connect to a continuously running server.

Working:

Connects to the server and sends a message.

Receives response from the server and prints it.

Closes the client socket.

Key Point: Allows multiple clients to interact with a single server over TCP.

Pyro4 Server (pyro_server.py)

Technique Used: Remote object server using Pyro4.

Working:

Defines a Calculator class with remote methods add() and multiply().

Exposes the class with @Pyro4.expose.

Registers the object with Pyro daemon and Name Server.

Keeps listening for remote method calls with daemon.requestLoop().

Key Point: Pyro4 allows Python objects to be called remotely over the network as if they were local objects.

Pyro4 Client (pyro_client.py)

Technique Used: Remote object client using Pyro4.

Working:

Connects to the remote object using Pyro4.Proxy and the logical name PYRONAME:example.calculator.

Calls remote methods add() and multiply() as if they were local functions.

Receives and prints results returned by the server.

Key Point: Pyro4 clients can invoke methods on remote servers transparently, making distributed computing simple.