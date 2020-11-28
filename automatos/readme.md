# Automatos

## Description

Un de nos agents ne répond plus depuis quelques jours, nous avons reçu un mail avec une photo d'archives de Brigitte Friang. Cela ne peut pas être une coïncidence. Il a certainement cherché à cacher des informations dans l'image. Nous devons le secourir au plus vite, il est certainement en danger et sur écoute.

Le flag est juste une chaîne de caractères

`brigitte.png (SHA256=31b88d96ff54ef15e6c995aac5a1759068ac8ba43d3cbdf561c7ea44ab42d735)`

## Solution

La première approche a été d'analyser l'image `brigitte.png`.

En utilisant l'outil [Aperisolve](https://aperisolve.fr/), on peut visualiser un carré dans le spectre rouge.

Le titre du challenge nous a conduit a faire des recherche sur les automates cellulaires, et notamment sur le jeu de la vie.

Malheureusement ce n'était pas le moyen de résoudre ce challenge.

## Write-up

- [Risk & Co](https://blog-cyber.riskeco.com/brigitte-friang-challenge-write-up/)