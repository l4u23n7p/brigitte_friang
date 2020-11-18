# ChatBot

## Description

EvilGouv a récemment ouvert un service de chat-bot, vous savez ces trucs que personne n'aime. Bon en plus d'être particulièrement nul, il doit forcément y avoir une faille. Trouvez un moyen d'accéder à l'intranet !

Lien : https://challengecybersec.fr/b34658e7f6221024f8d18a7f0d3497e4

Indice : Réseau local

Le flag est de la forme : DGSESIEE{x} avec x un hash

## Solution

On tombe sur un chatbot basique qui nous permet de poser des questions.

La première action a été d'identifier les interactions du site web avec burp.

On remarque vite que 2 type de requête AJAX sont effectué par le bot : une pour envoyer notre message au serveur (`ChatBotMessage.request`) et l'autre pour récupérer des informations sur un site web (`ChatBotProxy.request`).

Notre but étant d'accéder à l'intranet, la requête simulant un proxy est surement notre point d'entrée.

On essaye donc à travers cette requête d'accéder à des IP privées du subnet `192.168.0.0/16`, cependant pour n'importe qu'elle IP de ce subnet on obtient une erreur 503, il semblerait qu'un filtre sur ces IP est en place au niveau du nginx.

L'approche suivante a été de tester des url typiquement utilisé en internes, tel que `http://intranet`, `http://intra.local`, `http://intra.lan`, etc...

Le script `chatbot.py` permet d'automatiser le test d'url.

Après quelques minutes, on obtient un résulat positif sur l'url `http://intra`.

```
Find url http://intra with content {"contents":"<!DOCTYPE html>\n<html>\n\n<head>\n  <meta charset=\"utf-8\">\n  <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n  <link href=\"/35e334a1ef338faf064da9eb5f861d3c/fontawesome/css/all.min.css\" rel=\"stylesheet\">\n  <link href=\"/35e334a1ef338faf064da9eb5f861d3c/bootstrap/css/bootstrap.min.css\" rel=\"stylesheet\">\n  <link href=\"/35e334a1ef338faf064da9eb5f861d3c/css/style_index.css\" rel=\"stylesheet\">\n  <link rel=\"icon\" href=\"/35e334a1ef338faf064da9eb5f861d3c/img/favicon.ico\" />\n  <title>Evil Gouv intranet</title>\n</head>\n\n<body>\n  <div>\n    <h1>FLAG DGSESIEE{2cf1655ac88a52d3fe96cb60c371a838}</h1>\n</div>\n</body>\n<script src=\"/35e334a1ef338faf064da9eb5f861d3c/js/jquery-3.5.1.min.js\"></script>\n<script src=\"/35e334a1ef338faf064da9eb5f861d3c/js/popper.min.js\"></script>\n<script src=\"/35e334a1ef338faf064da9eb5f861d3c/js/bootstrap.min.js\"></script>\n\n</html>","title":"Evil Gouv intranet","icon":"Null"}
```
On récupère le flag dans le contenu de la page : `DGSESIEE{2cf1655ac88a52d3fe96cb60c371a838}`.