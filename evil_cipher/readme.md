# Evil Cipher

## Description

Evil Country a développé et implémenté sur FPGA son propre algorithme de chiffrement par blocs de 45 bits avec une clé de 64 bits. cipher.txt est un message chiffré avec la clé key=0x4447534553494545. Un agent a réussi à récupérer :
- le code VHDL de l'algorithme (evil_cipher.vhd)
- la fin du package VHDL utilisé (extrait_galois_field.vhd)
- le schéma de la fonction permutation15 (permutation15.jpg)
- le schéma du composant key_expansion (key_expansion.jpg)

Un exemple de texte chiffré se trouve dans le fichier evil_example.txt (dans l'archive zip)

Déchiffrez le message.

Le flag est de la forme DGSESIEE{x} avec x un hash

`evil_cipher.zip (SHA256=0b8ade55e61e2e0188cea2a3c004287ca16b9b1ee2951fa4ffe1b27963544434)`

## Solution

Ce challenge n'a pas été résolu.

## Write-up

- [Risk & Co](https://blog-cyber.riskeco.com/brigitte-friang-challenge-write-up/)
