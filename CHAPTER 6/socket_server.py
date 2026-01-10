import socket

# 1️⃣ Create listening socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

# 2️⃣ Bind and listen
server_socket.bind((host, port))
server_socket.listen(5)

print("Server is running and waiting for clients...")

while True:
    # 3️⃣ Wait for clients
    conn, address = server_socket.accept()   # new data socket
    print("Client connected:", address)

    # 4️⃣ Receive data
    data = conn.recv(1024).decode()
    print("Client says:", data)

    # 5️⃣ Send response
    conn.send("Hello Client, connection established!".encode())

    # 6️⃣ Close client data socket
    conn.close()
