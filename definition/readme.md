# Définition

## Description

Un de vos collègues a créé un petite énigme, il est un peu lourd et vous demande depuis des semaines de la résoudre, faites lui plaisir. Voici l'énigme : Quelle heure est-t-il ?

Connectez-vous via `nc challengecybersec.fr 6660`

Le flag est de la forme : DGSESIEE{x} avec x un hash 

## Solution

Le challenge nous demande d'envoyer l'heure.

Cependant de nombreux format existe, donc quelle est celui attendu ?

En réfléchissant un peu, il existe un format universel : le `timestamp`

On réalise donc un script `definition.py` pour envoyer le timestamp au serveur.

On obtient le flag est `DGSESIEE{cb3b3481e492ccc4db7374274d23c659}`