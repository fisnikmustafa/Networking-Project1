import socket
import threading
from metodat import *

IP = "localhost"
PORT = 14000
THREADCOUNT = 0

def handle_client(conn, addr):
    global THREADCOUNT
    print(f">> {addr} u lidh.")
    response = ''
    connected = True
    while connected: 
        try:
            msg = conn.recv(128).decode("utf-8") #merr mesazhin nga klienti
        except ConnectionResetError:
            print(">> ERROR: Klienti nderpreu lidhjen papritmas!")
            break
        else:
            if msg == "!PERFUNDO":
                connected = False
            elif msg == "!NDERRO":
                connected = False
            elif msg == "IP":
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
            conn.send(response.encode("utf-8"))
    print(f"Lidhja me {addr} perfundoi.")
    THREADCOUNT -= 1
    print(f">> ACTIVE CONNECTIONS: {THREADCOUNT}")
    conn.close()

def main():
    global THREADCOUNT
    print(">> Serveri eshte duke u nisur...")
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((IP,PORT))
    except Exception as e:
        print(str(e))
    serverSocket.listen(10)
    print(f">> Serveri eshte duke degjuar ne {IP}:{PORT}")

    while True:
        conn, addr = serverSocket.accept() #prano lidhjen nga klienti
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        THREADCOUNT += 1
        print(f">> ACTIVE CONNECTIONS: {THREADCOUNT}")

if __name__ == "__main__":
    main()