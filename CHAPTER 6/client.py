import socket

# ---------- Create socket ----------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ---------- Get server info ----------
host = socket.gethostname()
port = 12345

# ---------- Connect ----------
client_socket.connect((host, port))

# ---------- Send data ----------
client_socket.send("Hello from Client".encode())

# ---------- Receive response ----------
response = client_socket.recv(1024).decode()
print("Server says:", response)

# ---------- Close ----------
client_socket.close()
