import socket

# 1️⃣ Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

# 2️⃣ Connect to server
client_socket.connect((host, port))

# 3️⃣ Send data
client_socket.send("Hello Server".encode())

# 4️⃣ Receive response
response = client_socket.recv(1024).decode()
print("Server says:", response)

# 5️⃣ Close connection
client_socket.close()
