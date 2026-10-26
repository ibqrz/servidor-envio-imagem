import socket

def iniciar_servidor_udp():
    HOST = '127.0.0.1'
    PORTA = 4545

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((HOST, PORTA))
        print("Serv. Ativo\n")

        dados, addr = servidor.recvfrom(65535)
        print("Pacote recebido")
        print(f"Tamanho: {len(dados)} bytes")
        print(f"IP: {addr[0]}")
        print(f"Porta: {addr[1]}")

        with open("imagem_recebida.jpg", "wb") as arquivo:
            arquivo.write(dados)
        print("Imagem salva em imagem_recebida.jpg")

        servidor.sendto("Imagem recebida!".encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        iniciar_servidor_udp()
    except OSError as e:
        print(f"Erro: {e}")