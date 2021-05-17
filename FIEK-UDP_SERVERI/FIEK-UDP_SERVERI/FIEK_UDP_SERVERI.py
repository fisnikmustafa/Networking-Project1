import socket
from metodat import *

IP = "localhost"
PORT = 14000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    serverSocket.bind((IP, PORT))
except Exception as e:
    print(f"Serveri nuk mundi te lidhej ne {IP}:{PORT}. Detajet: {e}.")
    raise SystemExit(0)
else:
    print(">> Serveri eshte duke punuar dhe po pret per kerkesa...")

    while True:
        msg, addr = serverSocket.recvfrom(128)
        msg = msg.decode("utf-8")

        if msg == "IP":
            response = "IP adresa e klientit eshte " + get_IP(addr)
        elif msg == "NRPORTIT":
            response = "PORTI i klientit eshte " + str(get_PORT(addr))
        elif msg == "KOHA":
            response = KOHA()
        elif msg == "LOJA":
            response = LOJA()
        elif msg == "FATI":
                response = FATI()
        elif msg.startswith("NUMERO "):
            response = "Teksti i pranuar permban " + NUMERO(msg)
        elif msg.startswith("ANASJELLTAS "):
            response = ANASJELLTAS(msg)
        elif msg.startswith("PALINDROM "):
            response = PALINDROM(msg)
        elif msg.startswith("GCF "):
            response = str(GCF(msg))
        elif msg.startswith("KONVERTO "):
            response = str(KONVERTO(msg))
        elif msg.startswith("FIBONACCI "):
            response = FIBONACCI(msg)
        elif msg.startswith("CAESAR "):
            response = CAESAR(msg)
        else:
            response = "Kerkesa nuk eshte bere ne formatin e duhur!"
    
        print(f">> KLIENTI {addr}: {msg}")
        response = f"Pergjigjja: {response}"
        response = response.encode("utf-8")
        serverSocket.sendto(response, addr)
    

