# ASCII UART

## Description

Un informateur a intercepté un message binaire transmis sur un câble. Il a rapidement enregistré via la carte son d'un PC les données en 8 bits signés (ascii_uart.raw). Dans la précipitation, il a oublié de noter la fréquence d'échantillonnage. Retrouvez le message.

Le flag est de la forme DGSESIEE{X} avec X le message

`ascii_uart.raw (SHA256=0421ace2bbacbb5a812868b0dbb38a23533cda67bf7f00b1031fdbd7a228c8a5)` 

## Solution

Le challenge consiste a retrouver le message d'une communication effectuée avec le protocole UART.

Le fichier peut être ouvert avec audacity pour visualiser la communication.

On se renseigne donc ensuite sur le fonctionnement du protocole UART pour retrouver le flag.

Le script python `decode_ascii_uart.py` implémentent 3 règles importantes du protocoles UART :
- la gestion du LSB
- la gestion des break
- la gestion du bit de parité

On trouve ainsi le flag `DGSESIEE{ d[-_-]b  \_(''/)_/  (^_-)   @}-;---    (*^_^*)  \o/ }`

## Documentation

https://sigrok.org/wiki/Protocol_decoder:Uart

https://www.codrey.com/embedded-systems/uart-serial-communication-rs232/
