# Le polyglotte

## Description

Nous avons intercepté un fichier top secret émanant d'Evil Country, il est très certainement en rapport avec leur programme nucléaire. Personne n'arrive à lire son contenu.

Pouvez-vous le faire pour nous ? Une archive était dans le même dossier, elle peut vous servir

Le flag est de la forme : DGSESIEE{x} avec x un hash que vous trouverez

`message.pdf (SHA256=e5aa5c189d3f3397965238fbef5bc02c889de6d5eac713630e87377a5683967c)`

`secrets.zip (SHA256=ae5877bb06ac9af5ad92c8cd40cd15785cbc7377c629ed8ec7443f251eeca91f)`

## Solution

On cherche un hash dans le fichier `message.pdf`.

En utilisant l'outil `pdftohtml`, on obtient un fichier html qui contient le texte suivant :
```
Ce document concerne l operation soleil atomique.Cette operation est strictement confidentielle et ne doit en aucun cas Œtre devoilee. Les informations sur l operation sont disseminØes dans ce fichier.Chaque partie de l information est identifiee par un nombre par ex : [0]ae7bca8e correspond a la premiŁre partie de l information qu il faut concatener au reste.Top Secret·
```

Nous savons donc que notre hash est en plusieurs parties dans le fichier `message.pdf`.

D'autre part le titre du challenge nous indique que `message.pdf` est un fichier polyglotte.

On commence par regarder le contenu du fichier `message.pdf` avec la commande `less`. 

On remarque la présence de balise html ainsi qu'une balise pdf contenant des données (`<5b 31 5d 34 64 38 36 32 64 35 61> `). En convertissant les nombres héxadécimaux en lettre avec la table ASCII, avec [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NWIgMzEgNWQgMzQgNjQgMzggMzYgMzIgNjQgMzUgNjE) par exemple, on trouve la partie `[1]4d862d5a`.

On s'occupe maintemant au code javascript contenu dans le fichier `message.pdf`, pour cela on renomme le fichier `message.pdf` en `message.pdf.html` pour qu'un navigateur l'interprète comme un fichier html.

Le fichier contient le code javascript suivant :
```js
var flag = [91,48,93,97,97,57,51,56,97,49,54];
for(i=0;i<flag.length;i++){flag[i] = flag[i]+4} alert(String.fromCharCode.apply(String, flag));
```
Le string qui est affiché n'est pas correct car un décalage par 4 est fait. Néanmoins la partie est affichée en décimal, il suffit juste de convertir les nombres en lettres, comme pour la première on peut utiliser [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Comma',false)&input=OTEsNDgsOTMsOTcsOTcsNTcsNTEsNTYsOTcsNDksNTQ) pour récupérer la partie `[0]aa938a16`.

Pour avancer plus loin, il nous faut plus d'information et pour cela nous avons une archive `secret.zip` à notre disposition.

Malheureusement, il nous faut un mot de passe pour extraire les fichiers.

On utilise donc john pour brute force le mot de passe.

```
zip2john secrets.zip > secrets.zip.hash

john --wordlist=/usr/share/wordlists/rockyou.txt secrets.zip.hash
```

Une correspondance est trouvé avec le mot de passe `finenuke`, on extrait donc l'archive avec ce mot de passe.

```
unzip -P finenuke secrets.zip
```

On obtient 2 fichiers : `info.txt` et `hint.png`.

`info.txt`

```
Ange Albertini
key='\xce]`^+5w#\x96\xbbsa\x14\xa7\x0ei'
iv='\xc4\xa7\x1e\xa6\xc7\xe0\xfc\x82'
[3]4037402d4
```

On obtient la partie 3 du hash, il nous manque donc la partie 2.

L'image `hint.png` représente un blowfish, on suppose donc que `key` et `iv` servent pour chiffrer ou déchiffrer avec l'algorithme blowfish.

La dernière information est `Ange Albertini`. Une recherche google permet de nous éclairer, cette personne fait des recherche sur les fichiers polyglottes.

Après des recherche plus poussées, on tombe sur la méthode `angecryption`, qui consiste à chiffrer un fichier pour obtenir un autre fichier.

On essaye donc de chiffrer le fichier `message.pdf` avec la `key` et l'`iv` en utilisant l'algorithme `blowfish`.

Le script `encrypt_blowfish.py` permet d'obtenir le fichier `message.pdf.blowfish`, qui après inspection est une image au format JPEG.

La commande `binwalk` permet de découvrir un exécutable caché dans l'image. En utilisant `ghidra`, on retrouve dans la fonction `main` la comparaison suivante :

```c
  if (((((((__dest[1] ^ *__dest) == 0x69) && ((__dest[2] ^ __dest[1]) == 0x6f)) &&
        ((__dest[3] ^ __dest[2]) == 0x38)) &&
       (((__dest[4] ^ __dest[3]) == 0x56 && ((__dest[5] ^ __dest[4]) == 0x50)))) &&
      (((__dest[6] ^ __dest[5]) == 0x57 &&
       (((__dest[7] ^ __dest[6]) == 0x50 && ((__dest[8] ^ __dest[7]) == 0x56)))))) &&
     (((__dest[9] ^ __dest[8]) == 6 && (__dest[9] == 0x34)))) {
    puts("Bravo");
    exit(0);
  }
```
Cette comparaison effectue une opération xor sur chaque lettre avec la lettre suivante, à l'exception de la dernière qui est comparé directement.

On connait donc la dernière lettre, et à partir de celle là retrouver les autres.

On développe un script `reverse_pass.py` pour nous faciliter la conversion : on obtient la partie `[2]e3c4d24`.

En remettant les parties dans l'ordre, on obtient donc le flag `DGSESIEE{aa938a164d862d5ae3c4d244037402d4}`.
