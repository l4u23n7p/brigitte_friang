
# Steganosaurus

## Description

Nos agents ont trouvé dans le camion de livraison une clef USB. Nous vous transférons le filesystem de cette dernière et espérons que votre grande capacité de réflexion pemettra de révéler les secrets les plus sombres d'Evil Country !

Le flag est de la forme DGSEESIEE{x} avec x une chaine de caractères. (Attention au DGEESIEE, une erreur de typo s'est glissée dans le flag)

`message (SHA256=3889febebd6b1d35c057c3ba3f6f722798f029d6d0321b484305922a3d55d4d8)`

## Solution

On a un fichier `message` qui est un filesystem d'une clé USB.

En le montant avec la commande `mount`, on arrive à récupérer plusieurs fichiers :
- `readme`
- `steganausur.apk`
- `flag.png`
- `flag.png.trahsinfo`

On comprend facilement vu le titre du challenge que le flag est caché dans le fichier `flag.png` et qu'il faut reverse l'application à notre disposition.

Après avoir décompilée l'application avec `jadx`, on obtient les sources en java, cependant elle ne nous apprennent rien d'intéressant à part la présence d'une lib `libflutter.so` qui est anormalement lourde.

Malheureusement, l'analyse de la lib avec `ghidra` ne donne rien de facilement analysable.

Ce challenge n'a pas été résolu.

## Write-up

TBD


