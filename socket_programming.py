import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5500))
sock.listen(1)
conn, addr = sock.accept()

while true:
    data = conn.recv(1024)
    if not data:
        breal
    conn.sendall(data)
        
conn.close()