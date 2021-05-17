import socket
import random
import math
from decimal import Decimal
from datetime import datetime

def get_IP(addr):
    #hostname = socket.gethostname()
    #return socket.gethostbyname(hostname)
    return addr[0]

def get_PORT(addr):
    return addr[1]

def NUMERO(kerkesa):
    zanoret = "aeiouy"
    bashketingelloret = "bcdfghjklmnpqrstvwxz"
    nrZanoreve = 0
    nrBashketingelloreve = 0
    teksti = kerkesa[kerkesa.find(' ')+1:].lower()

    for char in teksti:
        if char in zanoret:
            nrZanoreve += 1
        if char in bashketingelloret:
            nrBashketingelloreve += 1
    return f"{nrZanoreve} zanore dhe {nrBashketingelloreve} bashketingellore."

def ANASJELLTAS(kerkesa):
    char_array = []
    teksti = kerkesa[kerkesa.find(' ')+1:]
    index = len(teksti)
    while index != 0:
        index -= 1
        char_array.append(teksti[index])
    return "".join(char_array)

def PALINDROM(kerkesa):
    teksti = kerkesa[kerkesa.find(' ')+1:]
    reversed_teksti = ANASJELLTAS("ANASJELLTAS " + teksti)
    if (reversed_teksti == teksti):
        return "Teksti i pranuar eshte palindrom"
    return "Teksti i pranuar nuk eshte palindrom"

def KOHA():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def LOJA():
    random_numbers = random.sample(range(1,35), 5)
    random_numbers.sort()
    return (random_numbers)

def GCF(kerkesa):
    try:
        first_num = int(kerkesa[kerkesa.find(' ')+1:kerkesa.rfind(' ')])
        second_num = int(kerkesa[kerkesa.rfind(' ')+1:])
   
        gcf = math.gcd(first_num, second_num)
    except Exception as e:
        return "Kerkesa nuk eshte bere ne formatin e duhur!"
        
    return gcf




def Konvertimet(lloji, numri):
    if(lloji.startswith("cmNeInch")):   #nese lloji i konvertimit fillon me cmNeInch
        return numri * Decimal(0.393701)
    elif(lloji.startswith("inchNeCm")): 
        return numri * Decimal(2.54)
    elif(lloji.startswith("kmNeMiles")): 
        return numri * Decimal(0.621371)
    elif(lloji.startswith("mileNeKm")): 
        return numri * Decimal(1.60934)
    else:
        return "Konvertimet e mundshme: cmNeInch xx, inchNeCm xx, kmNeMiles xx, mileNeKm xx   "

def KONVERTO(kerkesa):
    llojiKonvertimit = kerkesa[kerkesa.find(' ') + 1:]
    try:
        numri = Decimal(kerkesa[kerkesa.rfind(' ') + 1:])
    except Exception as e:
        return "Kerkesa nuk eshte bere ne formatin e duhur!"
    return Konvertimet(llojiKonvertimit, numri)



#FUNKSIONET SHTESE


def FATI():
    min = 1
    max = 6

    nr1 = random.randint(min,max)
    nr2 = random.randint(min,max)

    nr1 = str(nr1)
    nr2 = str(nr2)

    rez = nr1 + " " + nr2

    return rez



#------------ FIBONACCI -------------------------------------------------------------
def Fib(n): #kthen anetarin e caktuar te serise Fibonacci
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

def FIBONACCI(kerkesa): #sherben per thirrjen e funksionit Fib dhe per printim
    n=0
    try:
        x = int(kerkesa[kerkesa.find(' ')+1:])    #merr numrin e termave
    except Exception as e: 
        return "Kerkesa nuk eshte bere ne formatin e duhur!"
    series = "Fibonacci Series: "
    while n<x:
        series += " " + str(Fib(n))
        n+=1

    return series   #kthehen x termat e pare te serise Fibonacci
#--------------------------------------------------------------------------------------





#----------------------CAESAR---------------------
def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char == ' ':
            ciphertext += " "
        elif char.isdigit():
            ciphertext += char
        elif char.isupper():
            charPosition = ord(char) - 65
            charPosition = (charPosition + key) % 26
            char = charPosition + 65
            ciphertext += chr(char)
        else:
            charPosition = ord(char) - 97
            charPosition = (charPosition + key) % 26
            char = charPosition + 97
            ciphertext += chr(char)

    return ciphertext

def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char == ' ':
            plaintext += " "
        elif char.isdigit():
            plaintext += char
        elif char.isupper():
            charPosition = ord(char) - 65
            charPosition = (charPosition - key + 26) % 26 # p.sh (0 - 3 + 26) % 26 = 23 % 26 = 23
            char = charPosition + 65
            plaintext += chr(char)
        else:
            charPosition = ord(char) - 97
            charPosition = (charPosition - key + 26) % 26
            char = charPosition + 97
            plaintext += chr(char)
   
    return plaintext

def CAESAR(kerkesa):
    # kerkesa = "CAESAR {lloji} {teksti} {key}"

    

    lloji = kerkesa[kerkesa.find(' ')+1:] #kthen "{lloji} {teksti} {key}" 
    teksti = lloji[lloji.find(' ')+1:lloji.rfind(' ')]
    key = (lloji[lloji.rfind(' ')+1])

    try:
        key = int(key)
    except Exception:
        return "Kerkesa nuk eshte bere ne formatin e duhur!"

    lloji = lloji.upper()

    if (lloji.startswith("ENKRIPTO")):
        return caesar_encrypt(teksti, key)
    elif (lloji.startswith("DEKRIPTO")):
        return caesar_decrypt(teksti, key)
    else:
        return "Kerkesa nuk eshte bere ne formatin e duhur!"


  