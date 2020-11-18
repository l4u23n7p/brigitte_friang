# Keypad Sniffer

## Description

Le code d'accès d'un centre militaire de télécommunications est saisi sur un clavier. Un agent a accédé au matériel (Cf. photos face avant et face arrière du clavier) et a inséré un dispositif pour enregister les données binaires qui transitent sur le connecteur du clavier. Le fichier joint (keypad_sniffer.txt) comprend les données binaires (échantillonnées à une fréquence de 15 kHz) au moment où une personne autorisée rentrait le code d'accès. Retrouvez le code d'accès.

Le flag est de la forme DGSESIEE{X} où X est le code saisi

`keypad_sniffer.txt (SHA256=f5660a0b1c8877b67d7e5ce85087138cbd0c061b0b244afc516c489b39a7f79d)`

`keypad_face.jpg (SHA256=b39c0d732f645fc73f41f0955233bec3593008334a8796d2f1208346f927fef2)`

`keypad_back.jpg (SHA256=1f5d41c3521d04494779e43a4d5fae7cb14aad44e6e99cf36642ff4e88fab69f)`

## Solution

Il nous faut retrouver le code qui a été saisi sur le keypad. Pour cela nous disposons d'une image de la face et de l'arrière du keypad ainsi que l'enregistrement de la saisie du code en binaire.

La première étape est de comprendre le format de l'enregistrement.
Une ligne comprend 12 bits, et en regardant la face arrière on remarque que le keypad possède 6 * 2 pin, répartie sur deux lignes de la manière suivante, 2 pin pour l'alimentation puis 4 pin pour les data.

On obtient donc le format suivant : `2 bits | 4 bits | 2 bits | 4 bits`

Les parties à `2 bits` correspondent à l'alimentation et à la terre, et les parties à `4 bits` correspondent aux données.

En regardant le contenu de `keypad_sniffer.txt` on se rend compte que le format correspond bien, on retrouve pour chaque ligne `10` + `4 bits` + `10` + `4 bits`.

On connait maintenant les données utiles qui représente une information, mais comment l'interpreter ?

Une recherche google nous fait découvrir la méthode du `column scanning`, qui est souvent utilisé dans ce genre de keypad.

Une partie de 4 bits correspond à la ligne et l'autre à la colonne.

L'application de cette méthode permet de détecter les touches pressées : une touche est pressé lorsqu'un 0 est présent dans chaque partie de 4 bits.

Lorsque c'est le cas on peut retrouver la touche pressé avec l'index du 0 dans chaque partie.

Exemple : `1110` et `0111` correspond à la touche ligne 4 et colonne 1

On utilise la photo de face du keypad pour construire une matrice de correspondance entre les touches et les couples ligne/colonne.

On construit donc un script `sniffer.py` pour nous permettre de retrouver le code.

1. On lit le fichier et on enlève les saut de lignes
2. On formatte chaque ligne pour avoir son couple ligne/colonne
3. On supprime les doublons, dans notre cas cela correspond à toutes valeurs identique qui se suivent.

    Exemple : 
    
    ```
    (1111) (0111)           (1111) (0111)
    (1111) (0111)  ====\    (1111) (1011)       
    (1111) (1011)  ====/    (1111) (0111)
    (1111) (0111)
    ```

4. On regroupe chaque ligne par bloc : un bloc correspond à une boucle du scan, c'est-à-dire lorsque on a testé chaque ligne (`0111`, `1011`, `1101`, `1110`)
5. Pour chaque bloc, on regarde si une touche est pressé. Si une touche est pressé on regarde aussi le nombre de fois que cette touche est pressé consécutivement, si c'est valeur est trop faible cela veut dire que c'est une erreur à ignoré.
6. Pour chaque couple ligne/colonne trouvés, on fait la correspondance avec la matrice pour retrouvé la touche.
7. On reconstitue le code.

Le script permet de trouve le flag `DGSESIEE{AE78F55C666B23011924}`.

## Documentation

https://www.circuitstoday.com/interfacing-hex-keypad-to-8051