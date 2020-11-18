# Alone Muks

## Description

Lors de votre récent séjour à Evil Country, vous êtes parvenu à brancher un dispositif sur le camion effectuant la livraison. Il faut maintenant trouver une faille sur le système pour pouvoir prendre le contrôle du camion autonome de la marque Lates et le rediriger vers un point d'extraction. Un agent a posé un dispositif nous permettant d'accéder au système de divertissement du véhicule. A partir de ce dernier, remontez jusqu'au système de navigation.
Connectez-vous en SSH au camion

Identifiants: user:user

Le serveur est réinitialisé périodiquement

Port : 5004

Le flag est de la forme DGSESIEE{hash} 

## Solution

En se connectant au serveur en SSH, on arrive sur un interpréteur python.

On essaye de sortir de cet interpéteur avec `CTRL-C`, ce qui fonctionne.

On obtient un shell en tant que `user`.

Cette session n'a accès qu'a certaines commande : `python` et `date`.

Cependant en utilisant une console python, on arrive à afficher le script `login.py`. Les identifiants contenus dans ce fichier ne sont néanmoins d'aucune utilité.

On peut aussi utiliser python pour obtenir un shell non limité, ce que l'on fait.

On essaye ensuite de lister nos droits avec la commande `sudo -l`.

On remarque qu'on peut utiliser `vim` en tant que `globalSystem` : on récupère un shell via `vim` en tant que `globalSystem`.

En listant de nouveau nos droit, on peut voir qu'on peut utiliser `/usr/bin/update` en tant que `navigationSystem`.

En regardant les droits sur ce fichier, on peut le modifier. On remplace donc le fichier par un lien symbolique vers `/bin/sh`.

En exécutant `/usr/bin/update`, on obtient donc un shell en tant que `navigationSystem`.

On affiche ensuite le flag `DGSESIEE{44adfb64ff382f6433eeb03ed829afe0}`.