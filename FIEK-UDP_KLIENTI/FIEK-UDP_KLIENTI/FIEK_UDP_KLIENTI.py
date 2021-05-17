import socket

IP = "localhost"
PORT = 14000

def informatat():
    i = 0
    kerkesat = ["IP", "NRPORTIT", "NUMERO {hapesire} tekst", "ANASJELLTAS {hapesire} tekst", "PALINDROM {hapesire} tekst", "KOHA", "LOJA", "GCF {hapesire} numer1 {hapesire} numer2", "KONVERTO {hapesire} Opsioni {hapesire} numer", "FIBONACCI {hapesire} numer","CAESAR {hapesire} enkripto/dekripto {hapesire} teksti {hapesire} celesi" , "FATI"]
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
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
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
        main()
    else:
        print("Keni dhene IP adrese ose port te gabuar.")
        nderroServer()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        print("\n-------------------------------------------------------------------------------")
        print("Zgjedhni operacionin qe deshironi te kryeni ose shtyp: ")
        print("     !NDERRO - Per te nderruar serverin")
        msg = input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, FIBONACCI, CAESAR, FATI)?")
        msg = msg.strip()

        if msg == "!NDERRO":    #nese vjen ky mesazh atehere perdoruesit i mundesohet te nderroje adresen ne te cilen deshiron te dergoje mesazhin
             nderroServer()
        else:
            try:
                msg = msg.encode("utf-8")
                client.sendto(msg, (IP, PORT))
                response, addr = client.recvfrom(128)   #pranohet pergjigjja, dhe adresa nga e cila vjen kjo pergjigje
            except ConnectionResetError as ce:
                print(f">> ERROR: Mesazhi nuk mund te dergohet. Detajet: {ce}.")
                raise SystemExit(0)
            except Exception as e:
                print(f">> ERROR: Mesazhi nuk mund te dergohet. Detajet: {ce}.")
                raise SystemExit(0)
            else: 
               print(">> SERVERI: " + str(response))
               print("-------------------------------------------------------------------------------")


if __name__ == "__main__":
    informatat()
    main()