import socket

IP = "localhost"
PORT = 14000


def informatat():
    i = 0
    kerkesat = ["IP", "NRPORTIT", "NUMERO {hapesire} tekst", "ANASJELLTAS {hapesire} tekst", "PALINDROM {hapesire} tekst", "KOHA", "LOJA", "GCF {hapesire} numer1 {hapesire} numer2", "KONVERTO {hapesire} Opsioni {hapesire} numer", "FIBONACCI {hapesire} numer","CAESAR {hapesire} encrypt/decrypt {hapesire} teksti {hapesire} celesi" , "FATI"]
    opsionet = ["cmNeInch, inchNeCm, kmNeMiles, mileNeKm"]
    print("\n------------------------------------------------------------------------------")
    print("INFORMATA rreth formatit te kerkesave:\n")
    for x in kerkesat:
        if x.startswith("KONVERTO"):
            print("KERKESA: " + x)
            print("  OPSIONET: ")
            for y in opsionet:
                print("    " + y)
        else:
            print("KERKESA: " + x)
    print("------------------------------------------------------------------------------")


def validoIP(ip):
    if ip.lower() == "localhost":
        return True
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for x in octets:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def validoPort(p):
    if p < 1023 or p > 65535:
        return False
    return True

def nderroServer():
    global IP
    global PORT

    newIP = input("Shkruaj IP adresen e serverit: ")
    newPORT = input("Shkruaj portin e serverit: ")
    newPORT = int(newPORT)
    ipValidimi = validoIP(newIP)
    portValidimi = validoPort(newPORT)
    if ipValidimi == True and portValidimi == True:
        IP = newIP
        PORT = newPORT
        print(">> CONNECTING: Po tentohet lidhja me serverin e ri...")
        main()
    else:
        print("Keni dhene IP adrese ose port te gabuar.")
        nderroServer()



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((IP, PORT))
    except Exception as ce: 
        print(f"\n>> FAILED: Lidhja me serverin deshtoi. Detajet: {ce}")
        connected = False
    else:   #kjo pjese ekzekutohet nese nuk ka Exception
        connected = True
        print(f"\n>> Klienti u lidh me serverin ne {IP}:{PORT}")
        print("------------------------------------------------------------------------------\n")

        while connected:
           
            print("Zgjedhni operacionin qe deshironi te kryeni ose shtyp: ")
            print("     !PERFUNDO - Per te perfunduar lidhjen")
            print("     !NDERRO - Per te nderruar serverin")
            msg = input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, FIBONACCI, CAESAR, FATI)?")
            msg = msg.strip()

            try:
                client.send(msg.encode("utf-8"))
            except ConnectionResetError:
                print(">> ERROR: Serveri nderpreu lidhjen papritmas!")
                break
            else: #kjo pjese ekzekutohet nese nuk ka Exception
                if msg == "!PERFUNDO":
                    print("Zgjodhet te perfundoni lidhjen me serverin.")
                    raise SystemExit(0)
                elif msg == "!NDERRO":
                    print("Zgjodhet te nderroni serverin.")
                    connected = False
                    nderroServer()
                else:
                    response = client.recv(128).decode("utf-8")
                    print(f">> SERVERI: {response}")
                    print("----------------------------------------------------------------------------------------------------------------------\n")


if __name__ == "__main__":
    informatat()
    main()