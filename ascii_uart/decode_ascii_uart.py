#!/usr/bin/python3

import soundfile as sf
import numpy as np

OFFSET=638

def binary(v):
    if v > 0:
        return 1
    return 0

def get_binary(data):
    return list(format(list(map(binary, np.array(data)))))

def get_byte(data):
    try:
        # identification de l'index du bit de start
        start = data.index(0)
    except:
        # expetion levée lorsqu'aucun bit de start est trouvé (aka la fin)
        return None, data, -1
    
    # redimensionnement à partir du bit de start
    data = data[start:]
    byte = []
    # identification de l'index du bit de stop
    stop = data.index(1, 8)

    # si l'index est supérieur à 10 nous avons une break condition
    if stop > 10:
        return None, data[stop:], -2

    # récupétration des 8 bits de donnés pour former notre octet
    for i in range(1, 9):
        byte.append(data[i])
    # inversement des bits pour les avoir dans l'ordre (LSB-first)
    byte.reverse()

    # récupération du bit de parité
    parity = data[9]
    # calcul de la parité de l'octet
    c1 = byte.count(1)

    # test de la parité
    if (c1 % 2) != 0 and parity == 0:
        return byte, data[stop:], -3
    elif (c1 % 2) == 0 and parity == 1:
        return byte, data[stop:], -3

    return byte, data[stop:], None

def sample(data):
    s = []
    for i in range(len(data)):
        if i == 0:
            s.append([data[i], 1])
        elif data[i-1] != data[i]:
            s.append([data[i], 1])
        else:
            s[len(s) -1 ][1] += 1
    return [ (r[0], round(r[1]/OFFSET)) for r in s]

def format(data):
    data = sample(data)
    for b in data:
        value = b[0]
        number = b[1]
        for i in range(number):
            yield value

def byte2chr(byte):
    return chr(int(''.join([str(bit) for bit in byte]),2))

def decode(data):
    return ''.join([byte2chr(byte) for byte in data])

def main():
    # lecture du fichier comme un fichier audio en 8 bits signés
    data, _ = sf.read('ascii_uart.raw', channels=1, samplerate=9600,subtype='PCM_S8')
    # conversion du fichier en binaire et nettoyage des doublons avec l'OFFSET identifié
    data = get_binary(data)
    code = []
    while len(data) > 0:
        # lecture octets par octets avec gestion des erreurs
        b, data, error = get_byte(data)
        if error is None:
            code.append(b)
        elif error == -1:
            break
        elif error == -2:
            print("break partial code '%s'" % decode(code))
        elif error == -3:
            print("remove parity error: '%s'" % byte2chr(b))
    # conversion des octets en ascii
    print("flag is '%s'" % decode(code))

main()
