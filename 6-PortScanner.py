import socket
from time import sleep


def verificar_porta(ip, porta):
    """
    Verifica se uma porta específica está aberta em um determinado endereço IP.

    Argumentos:
        ip (str): Endereço IP a ser verificado.
        porta (int): Porta a ser verificada.

    Retorno:
        True se a porta estiver aberta, False caso contrário.
    """
    try:
        # Cria um socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define o tempo limite de conexão
        sock.settimeout(0.5)
        # Conecta ao endereço IP e porta
        sock.connect((ip, porta))
        # Fecha o socket
        sock.close()
        return True
    except socket.error:
        return False

def gerar_relatorio(lista_portas_abertas):
    """
    Cria/Gera um relatório em formato de texto com as portas abertas encontradas no local.

    Argumentos do processo:
        lista_portas_abertas (list): Lista de tuplas (ip, porta) representando as portas abertas.
    """
    relatorio = "**Relatório de Portas Abertas**\n\n"
    for ip, porta in lista_portas_abertas:
        relatorio += f"Endereço IP: {ip}\nPorta: {porta}\n\n"
    print(relatorio)

# Definir a lista de endereços IP
lista_ips = ["192.168.1.1", "192.168.1.2"]

# Definindo a lista de portas prt
lista_portas = [22, 80, 443]

# Listinha para armazenar as portas abertas
lista_portas_abertas = []

# Executar o scanner
for ip in lista_ips:
    for porta in lista_portas:
        if verificar_porta(ip, porta):
            lista_portas_abertas.append((ip, porta))
            # Pausa para evitar sobrecarga na rede
            sleep(0.1)

# Aqui a mágia acontece, (Gerar o relatório)
gerar_relatorio(lista_portas_abertas)
