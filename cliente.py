import socket

def iniciar_cliente_udp():
    HOST = '127.0.0.1'
    PORTA = 4545
    ARQUIVO = "exemplo.jpg"  # imagem a enviar (menor que ~64 KB)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
            # Lê a imagem em bytes e envia em um único datagrama
            with open(ARQUIVO, "rb") as arquivo:
                dados = arquivo.read()
            cliente.sendto(dados, (HOST, PORTA))
            print(f"Imagem enviada: {len(dados)} bytes")

            resposta, addr = cliente.recvfrom(512)
            print(resposta.decode('utf-8'))

    except (OSError, FileNotFoundError) as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    iniciar_cliente_udp()