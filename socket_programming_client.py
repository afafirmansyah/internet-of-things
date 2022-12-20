import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5500))
sock.send(b"Hello")
conn, addr = sock.accept()
data = conn.recv(1024)
print(data)
conn.close()
