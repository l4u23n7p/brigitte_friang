#!/usr/bin/python3

def format(line):
    return (line[2:6], line[8:12])

def unique(data):
    for i in range(len(data)):
        if i == 0:
            yield data[i]
        else:
            if data[i] != data[i-1]:
                yield data[i]

def block(data):
    for r in range(round(len(data) / 4)):
        start = r * 4
        stop = (r+1) * 4
        yield data[start:stop]

def check(data):
    num = 1
    for b in range(1, len(data)):
        current = data[b]
        previous = data[b-1]
        # si la valeur précédente est différente on check
        if current != previous:
            # check si le block correspond à une touche pressé et que le nombre d'itération est suffisant (valeur arbitraire de 100)
            if has_key_press(previous) and num > 100:
                yield get_key_press(previous)
            num = 1
        # sinon on ajoute 1 au compteur
        else:
            num += 1

def get_key(obj):
    row = obj[0].index('0')
    column = obj[1].index('0')

    return matrix[column][row]

def has_key_press(block):
    for b in block:
        if '0' in b[0]:
            return True
    return False

def get_key_press(block):
    for b in block:
        if '0' in b[0]:
            return b
    return None


# matrice de correspondance avec le keypad (ici par column mais on peut la faire par row)
matrix = [['1', '4', '7', 'A'], ['2', '5', '8', '0'], ['3', '6', '9', 'B'], ['F', 'E', 'D', 'C']]

# lecture du fichier
data = open('keypad_sniffer.txt', 'r').readlines()
# suppression des sauts de ligne
data = [r.strip() for r in data]
# formatage de chaque ligne suivant le format présumé 2 bit / 4 bits (row) / 2 bit / 4 bit (column)
row_column = [format(l) for l in data]
# suppression des doublons, on se retrouve donc avec seulement les valeurs utiles
row_column = list(unique(row_column))
# regroupement des valeurs par bloc de 4 ce qui correspond à une boucle au niveau hardware
row_column = list(block(row_column))
# check de chaque bloque pour ne garder que les blocs correspondants à une touche pressé 
row_column = check(row_column)
# reconstitution du code avec la matrice
secret = ''.join([get_key(r) for r in row_column])

print('Le flag est DGSESIEE{%s}' % secret)


