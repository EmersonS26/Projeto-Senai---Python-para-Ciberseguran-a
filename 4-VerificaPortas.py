import psutil
import socket

# Coletando informações do TCP e UPD
connecttall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet")if conn.type == socket.SOCK_DGRAM]

#Separando informações sobre portas TCP
only_tcp_listening_ports = [conn.laddr.port for conn in connecttall if conn.status == psutil.CONN_LISTEN]

#Separando informações sobre portas UDP
only_udp_listening_ports = [conn.laddr.port for conn in only_udp]

#Removendo portas repetidas
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_tcp_listening_ports))

#Ordenando as portas de forma crescente
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

#Mostrando as portas TCP
for port in only_tcp_listening_ports:
    print(f"Porta TCP = {port} aberta")

print("\n")

#Mostrando as portas UDP
for port in only_tcp_listening_ports:
    print(f"Porta UDP = {port} aberta")


