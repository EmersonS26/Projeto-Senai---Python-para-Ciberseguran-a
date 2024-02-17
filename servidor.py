import socket
HOST = "localhost"
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen()
print("Aguardando conexão do cliente")
conn, ender = sock.accept()
print("conectado em", ender)
while True:
    data = conn.recv(1024)
    if not data:
        print("Fechar a conexão, sem dados")
        conn.close()
        break
    conn.sendall(data)