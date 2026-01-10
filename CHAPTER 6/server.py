import socket

# ---------- Create socket ----------
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ---------- Get host and port ----------
host = socket.gethostname()   # machine name
port = 12345

# ---------- Bind ----------
server_socket.bind((host, port))

# ---------- Listen ----------
server_socket.listen(1)
print("Server listening on", host, port)

# ---------- Accept connection ----------
conn, address = server_socket.accept()
print("Connected to client:", address)

# ---------- Receive data ----------
data = conn.recv(1024).decode()
print("Client says:", data)

# ---------- Send response ----------
conn.send("Hello from Server".encode())

# ---------- Close ----------
conn.close()
server_socket.close()
