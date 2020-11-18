# L'énigme de la crypte

## Description

Une livraison de souffre doit avoir lieu 47°N 34 2°W 1 39.

Elle sera effectuée par un certain REJEWSKI. Il a reçu des instructions sur un foulard pour signaler à Evil Gouv son arrivée imminente.

Nous avons une photo du foulard, mais celle-ci n'est pas très nette et nous n'avons pas pu lire toutes les informations. Le fichier foulard.txt, est la retranscription du foulard.

Nous avons un peu avancé sur les parties illisibles :

(texte illisible 1) est deux lettres un espace deux lettres. Il pourrait y avoir un lien avec le dernier code d'accès que vous avez envoyé à Antoine Rossignol.

(texte illisible 2) a été totalement effacé et enfin (texte illisible 3) semble être deux lettres.

REJEWSKI vient d'envoyer un message (final.txt). Il faut que vous arriviez à le déchiffrer. Je vous conseille d'utiliser openssl pour RSA.

Le flag est de la forme DGSESIEE{MESSAGE} où MESSAGE correspond à la partie centrale du texte en majuscules sans espace.

`final.txt (SHA256=1e93526cd819aedb8496430a800a610068e95762536b0366ca7c303a74eaab03)`

`foulard.txt (SHA256=9c8b0caf9d72fa68ddb6b4a68e860ee594683f7fe4a01a821914539ef81a1f21)`

## Solution

On commence par regarder ce que contient les deux fichiers :
- `final.txt` est un message chiffré
- `foulard.txt` contient du texte en clair

On s'intéresse donc à `foulard.txt` qui nous indique le chiffrement utilisé sur `final.txt`.

La première partie est peu compréhensible sans plus d'information, on se concentre donc sur la deuxième partie qui nous apprends que le message est chiffré avec RSA et nous donne aussi la clé publique.

Connaissant la clé publique, il est possible de reconstruire une clé privée lorsque le modulus n'est pas assez grand. On s'aide d'un sujet similaire sur [Stackoverflow](https://stackoverflow.com/questions/50053884/use-rsa-public-key-to-generate-private-key-in-openssl) pour recalculer les valeurs de `p`, `q` et `d` qui nous servirons pour génerer une clé privée.

On utilise le format `asn1` pour construire la clé privée avec openssl. Le script `create_privkey.py` permet de genérer le fichier `asn1`.

On utilise ensuite openssl pour générer la clé privée.

```bash
openssl asn1parse -genconf privkey.asn1 -out private.der

openssl rsa -in private.der -inform der -out private.pem -outform pem
```

Une fois la clé privée en notre possession, il ne reste plus qu'a l'utiliser pour déchiffrer `final.txt`.

```bash
openssl rsautl -decrypt -in final.txt -out final.txt.decrypt -inkey private.pem
```

On obtient donc le contenu du fichier `final.txt`.

```
IVQDQT NHABMPSVBYYUCJIYMJBRDWXAXP  THYVCROD
```

Le message est chiffré avec une autre méthode. Une recherche google sur REJEWSKI permet de vite comprendre qu'il s'agit d'un message chiffré avec enigma.

Le fichier `foulard.txt` nous donne la majorité des paramètre de la machine utilisé pour le chiffrement.

On sait qu'une machine M3 à été utilisé avec les paramètres suivant :
- elle utilise les rotors I, III et V, qui correspondent aux rotors impairs en ordre croissant
- la position actuelle du rotor est à `REJ`
- la position initiale du rotor est à `MER`
- il y a 2 plugboard

On sait aussi que chaque message chiffée par enigma utilise une clé qui précèdent le message, et que le nom de l'expéditeur suit le message.

A partir de ces informations, on en déduit que `IVQDQT` correspond à la clé du message, `NHABMPSVBYYUCJIYMJBRDWXAXP` correspond au message et que `THYVCROD` correspond à l'expéditeur, c'est-à-dire REJEWSKI.

On utilise ensuite un outil permettant de brute force la configuration enigma en connaissant un text en clair et sa correspondance chiffrée par enigma : [enigma-bruteforce](https://github.com/risteon/enigma-bruteforce)

On modifie l'outil pour nous permettre d'effectuer un brute force ciblé avec les informations en notre possession. Cette version est disponible sur [github](https://github.com/l4u23n7p/enigma-bruteforce).

On utilise donc la version modifiée avec la configuration connue.

```
python3 brute-force.py --ciphertext=THYVCROD --plaintext=REJEWSKI --rotors I III V --plugboards 2 --ring 'R E J'
[...]
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Solution found! Encrypt REJEWSKI to THYVCROD
{'rotor': ('I', 'III', 'V'), 'ref': 'B', 'ring': 'R E J', 'plug': 'EB ', 'display': 'BFG'}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
On connait ainsi le reflecteur (`B`), le premier plugboard (`EB`) et le display (`BFG`) qui correpond à la clé.

On réutilise l'outil pour vérifier que la clé est correcte.

```
python3 brute-force.py --ciphertext=IVQDQT --plaintext=BFGBFG --rotors I III V --plugboards 2 --ring 'R E J'
[...]
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Solution found! Encrypt BFGBFG to IVQDQT
{'rotor': ('I', 'III', 'V'), 'ref': 'B', 'ring': 'R E J', 'plug': 'BE ', 'display': 'MER'}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

On retouve bien notre display égale à `MER` : la clé est donc correcte.

Il nous manque juste le dernier plugboard, cependant on essaye de decoder le message avec les informations déjà récoltées à l'aide du script `decypher_message.py`.

On obtient le résultat suivant :
```
message key is BFGBFG
flag is DGSESIEE{LEUSZNGLOTSLONGSDESVIOLKNS}
name is REJEWSKI
```

On identifie visuellement le dernier plugboard qui est `AZ`. On l'ajoute dans la configuration et on réexecute le script.

```
message key is BFGBFG
flag is DGSESIEE{LESSANGLOTSLONGSDESVIOLONS}
name is REJEWSKI
```

On obtient ainsi le flag `DGSESIEE{LESSANGLOTSLONGSDESVIOLONS}`.