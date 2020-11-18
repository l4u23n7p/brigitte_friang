# Sous l'océan

## Description

Nous pensons avoir retrouvé la trace d'Eve Descartes. Nous avons reçu un fichier anonyme provenant d'un smartphone Android (probablement celui de son ravisseur). Retrouvez des informations dans son historique de position.

Le flag est de la forme DGSESIEE{x} avec x une chaine de caractères

`memdump.txt (SHA256=29c702ff8dc570319e5e8d05fc4cb96c1536b595b9a4e93d6205774f9afd2bff)`

## Solution

On cherche les informatiions de locations dans le fichier `memdump.txt`.

On retrouve la section `Last Known Locations` et `Custom Location History`.

On dessine chaque `Custom Location` sur une carte avec [gpsvisualizer](https://www.gpsvisualizer.com/)
```
name,latitude,longitude
Custom Location 10,-47,1462046,30,9018186
Custom Location 11,-47.1963297,30.9012294
Custom Location 12,-47.1970164,30.8641039
Custom Location 13,-47.1438013,30.8652827
Custom Location 14,-47.1448313,30.9642508

Custom Location 20,-47.0820032,30.8641039
Custom Location 21,-47.1300684,30.8643986
Custom Location 22,-47.1304118,30.9006402
Custom Location 23,-47.0789133,30.9003456
Custom Location 24,-47.0847498,30.8131067
Custom Location 25,-47.1307551,30.8148758
Custom Location 26,-47.1304118,30.8340395
Custom Location 27,-47.1084391,30.8319759

Custom Location 30,-47.0631205,30.8649880
Custom Location 31,-47.0322214,30.9015240
Custom Location 32,-47.0047556,30.8608621
Custom Location 33,-47.0411478,30.8632198

Custom Location 40,-46.9934318,30.8750074
Custom Location 41,-46.9481132,30.874418
Custom Location 42,-46.953263,30.9085939
Custom Location 43,-46.9961784,30.9047644
Custom Location 44,-46.9927451,30.8511361
Custom Location 45,-46.9457099,30.8508414

Custom Location 50,-46.9295737,30.8517256
Custom Location 51,-46.9072578,30.8926859
Custom Location 52,-46.8797919,30.853494
Custom Location 53,-46.9137809,30.8505466

Custom Location 60,-46.8571326,30.8912128
Custom Location 61,-46.856446,30.8484834

Custom Location 70,-46.8173416,30.8745954
Custom Location 71,-46.7703064,30.8743007
Custom Location 72,-46.7778595,30.9096549
Custom Location 73,-46.8242081,30.904058
Custom Location 74,-46.8125351,30.8404074
Custom Location 75,-46.7733963,30.8474818

Custom Location 80,-46.7438706,30.8772474
Custom Location 81,-46.7009552,30.8784261
Custom Location 82,-46.7054184,30.9034689
Custom Location 83,-46.7479904,30.8978716
Custom Location 84,-46.7376908,30.8474818
Custom Location 85,-46.7115982,30.8498398

Custom Location 90,-46.6456803,30.926149
Custom Location 91,-46.6625031,30.9264435
Custom Location 92,-46.6611298,30.8748901
Custom Location 93,-46.6473969,30.8657549
Custom Location 94,-46.6580399,30.8563241
Custom Location 95,-46.6587265,30.8014891
Custom Location 96,-46.6377838,30.7985401

Custom Location 100,-46.5794168,30.8664391
Custom Location 101,-46.5780435,30.9070986
Custom Location 102,-46.617869,30.9082768
Custom Location 103,-46.6213022,30.8463976
Custom Location 104,-46.575297,30.8428605
Custom Location 105,-46.5746103,30.869386

Custom Location 110,-46.5114389,30.9053311
Custom Location 111,-46.5443979,30.904742
Custom Location 112,-46.5395914,30.8351962
Custom Location 113,-46.4997659,30.8351962

Custom Location 120,-46.4729868,30.9006178
Custom Location 121,-46.433848,30.9017961
Custom Location 122,-46.433848,30.8623132
Custom Location 123,-46.4695535,30.8623132
Custom Location 124,-46.433848,30.8629027
Custom Location 125,-46.4297281,30.8222244
Custom Location 126,-46.4674936,30.8269416

Custom Location 130,-46.3644968,30.8204554
Custom Location 131,-46.3727365,30.9076877
Custom Location 132,-46.4214884,30.8682072
Custom Location 133,-46.3425241,30.8629027

Custom Location 140,-46.3184915,30.8198657
Custom Location 141,-46.3219248,30.9041528
Custom Location 142,-46.2752329,30.8169173
Custom Location 143,-46.2793527,30.9035636

Custom Location 151,-46.247767,30.921826
Custom Location 152,-46.2196146,30.9212369
Custom Location 153,-46.2154947,30.8646709
Custom Location 154,-46.2409006,30.8469871
Custom Location 155,-46.2100015,30.8346066
Custom Location 156,-46.2120615,30.7827088
Custom Location 157,-46.2450205,30.7762196
```
On peut exporter la carte dans une imagen qu'on peut alors retourné pour avoir le flag de manière plus lisible.

On trouve le flag `DGSIEE{OC34N}`