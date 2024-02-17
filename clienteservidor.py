import socket

HOST = '127.0.0.1'
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall(str.encode("Alunos"))
data = sock.recv(1024)
print("Mensagem que foi e voltou: ", data.decode())